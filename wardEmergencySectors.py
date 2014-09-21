import io
import os
import stat
import sys
import time


UNKNOWN_INFO_TAG    = '<Unknown>'

def genTitle(date_string, ward_name):
    titleStrings = []
    titleString1 = '%s Ward Emergency Contact Sectors' % ward_name
    titleStrings.append(' '*(40-len(titleString1)/2))
    titleStrings.append(titleString1)
    titleStrings.append('\n')
    if date_string:
        titleStrings.append(' '*(40 - len(date_string)/2))
        titleStrings.append(date_string)
        titleStrings.append('\n')
    titleStrings.append(' '*(40-len(titleString1)/2))
    titleStrings.append('-'*len(titleString1))
    titleStrings.append('\n')
    titleStrings.append('\n')
    title = ''.join(titleStrings)
    return title

def splitQuotedCSV(line):
    """
    Yields something very close to split(',')
    except that quoted strings which carry an interior ',' are not broken up.
    """
    #elems = line.split(',')
    elems = []
    i = 0
    while i < len(line):
        if line[i] == '"':
            j = line.index('"', i+1)
            elems.append(line[i+1:j])
            k = line.find(',', j+1)
            i = max(j, k)
        else:
            j = line.find(',', i)
            if j > i:
                elems.append(line[i:j])
                i = j
        i += 1
    return tuple(elems)


def isInside(graphs, position):
    """
    Determines whether the point defined by 'position' is wholely
    contained within the polygon defined by 'graphs'.
    """
    cross_count = 0
    for g in graphs:
        x = None
        if min(g[0][1], g[1][1]) >= position[1]:
            x = position[0]
            y = position[1]
        elif max(g[0][1], g[1][1]) >= position[1] and g[2] is not None:
            # We have to figure out if this point is below the line segment.
            x = position[0]
            y = g[2]*x + g[3]
            if y < position[1]:
                # It's outside of the line segment in this case.
                x = None
        if x is not None:
            if g[0][0] < g[1][0]:
                if g[0][0] <= x and x < g[1][0]:
                    cross_count += 1
            elif g[0][0] > g[1][0]:
                if g[1][0] < x and x <= g[0][0]:
                    cross_count += 1
    return ((cross_count & 0x1) == 1)

def genLineDef(pos0, pos1):
    if pos0[0] == pos1[0]:
        m = None
        b = None
    else:
        m = (pos1[1] - pos0[1])/(pos1[0] - pos0[0])
        b = pos0[1] - (m * pos0[0])
    return (pos0, pos1, m, b)

def genSectorDefs(gpsSectorDefs):
    sectorDefs = []
    for gpsSectorDef in gpsSectorDefs:
        sectorDef = []
        for i in range(len(gpsSectorDef[1])-1):
            line = genLineDef(gpsSectorDef[1][i], gpsSectorDef[1][i+1])
            sectorDef.append(line)
        # Loop back around to the first point, unless the last one ended there.
        i = len(gpsSectorDef[1]) - 1
        if gpsSectorDef[1][i][0] != gpsSectorDef[1][0][0] \
                or gpsSectorDef[1][0][1] != gpsSectorDef[1][0][1]:
            line = genLineDef(gpsSectorDef[1][i], gpsSectorDef[1][0])
            sectorDef.append(line)
        sectorDefs.append((gpsSectorDef[0], sectorDef))
    return sectorDefs

def owningSector(sectorDefs, position):
    for sectorDef in sectorDefs:
        if isInside(sectorDef[1], position):
            return sectorDef[0]
    return None

def displayableName(name, idTag=None, taggedNames=[]):
    if name[0] == '"' and name[-1] == '"':
        name = name[1:-1]
    prefixStr = ''
    if idTag:
        prefixStr = idTag
    for tags in reversed(taggedNames):
        isaTag = False
        for tn in tags[0]:
            if tn[1] == name[:len(tn[1])] and name[len(tn[1])] == ',':
                i = name.find(tn[2])
                if i > 0:
                    i += len(tn[2])
                    if True:
#                   if len(name) < i+1 or name[i] in [' ', '"']:
                        isaTag = True
                        name = name[:i] + '[%s]'%tn[0] + name[i:]
        if isaTag:
            if tags[1] not in prefixStr:
                prefixStr += tags[1]
    prefixStr = ' '*(6-len(prefixStr)) + prefixStr
    name = prefixStr + name
    return name

def displaySector(ofd, sectorName, groupings):
    global SectorCaptains
    ofd.write('\n')
    oline = "%s Sector\n" % str(sectorName)
    ofd.write(oline)
    oline = '-'*(len(oline)-1) + '\n'
    ofd.write(oline)
    ofd.write('\n')
    captains = SectorCaptains.get(sectorName, [])
    if captains:
        ofd.write('\tSector Captains:\n')
        ofd.write('\t---------------\n')
        for captain in captains:
            ofd.write('\t%s, %s, %s, %s\n' % captain)
    for groupName, grouping in groupings:
        if groupName is not None:
            ofd.write('\n\t\t%s:\n\t\t' % groupName)
            ofd.write('-'*(len(groupName)+1))
            ofd.write('\n')
        for family in grouping:
            oline = '    %s, %s, %s, %s\n' % (family[:3] + family[5:6])
            ofd.write(oline)
    ofd.write('\n\n')

def addIntoSector(sectors, sectorName, familyInfo, errorInfo=None):
    if errorInfo is None:
        errorInfo = repr(familyInfo)
    try:
        if not sectors.has_key(sectorName):
            sectors[sectorName] = []
        sectors[sectorName].append(familyInfo)
    except:
        sectors[UNKNOWN_INFO_TAG].append(errorInfo)
    return sectors

def organizeSectors(ifn, sectorDefs, idTag=None):
    global NameTags
    ifd = open(ifn, 'r')

    sectors = {UNKNOWN_INFO_TAG: []}
    for line in ifd:
        try:
            family = splitQuotedCSV(line)
            #
            # family :== (Longitude, Latitude, Household,
            #      Street, City, State, Zip, Phone, Email, Location-Status)
            #
            longitude = float(family[0])
            latitude = float(family[1])
            position = (latitude, longitude)
            sectorName = owningSector(sectorDefs, position)
            name = displayableName(family[2], idTag, NameTags)
            familyInfo = (name,)+family[3:]+position
            sectors = addIntoSector(sectors, sectorName, familyInfo, line)
        except:
            sectors[UNKNOWN_INFO_TAG].append(line)
    ifd.close()
    return sectors

def genSectors(ofn, sectors, sectorDefs, ts=None):
    global WARD_NAME
    ofd = open(ofn, 'w')
    if ts is None:
        dateString = None
    else:
        dateString = time.strftime('%B %d, %Y', ts)

    # Include a title at the top of the output file
    titleStrings = genTitle(dateString, WARD_NAME)
    ofd.write(titleStrings)

    sectorNames = sectors.keys()
    sectorNames.sort()
    if None in sectorNames:
        # Display the None groupings at the end of the normal Sectors
        sectorNames.remove(None)
        sectorNames.append(None)
    name = None
    groupings = []
    unknown_addresses = None
    for sectorName in sectorNames:
        if sectorName == UNKNOWN_INFO_TAG:
            unknown_addresses = sectors[sectorName]
            continue
        if sectorName is None:
            next_name = 'None'
            groupName = None
        else:
            next_name = str(sectorName[0])
            groupName = str(sectorName[1])
        if name != next_name:
            if groupings:
                displaySector(ofd, name, groupings)
            name = next_name
            groupings = []
        groupings.append((groupName, sectors[sectorName]))
    if groupings:
        displaySector(ofd, name, groupings)
    if unknown_addresses:
        ofd.write('Unknown\n')
        ofd.write('-------\n')
        for family in unknown_addresses:
            ofd.write(family)
    ofd.close()

def main(defFileName, inFileName, outFileName, extras=[]):
    #
    # Set up the global variables which define the boundaries, etc.
    #
    globalNames = 'global WARD_NAME, GpsSectorDefs, SectorCaptains, SpecialLocations\n'
    defs = open(defFileName, 'r').read()
    c = compile(globalNames+defs, defFileName, 'exec')
    eval(c)
    global EXTRA_WARD_TAG

    #
    # Organize the membership according to the global definitions.
    #
    sectorDefs = genSectorDefs(GpsSectorDefs)
    allSectors = organizeSectors(inFileName, sectorDefs)
    for specialLocation in SpecialLocations:
        sectorName = specialLocation[1]
        name = ' '*4 + specialLocation[0]
        familyInfo = (name,) + specialLocation[2:]
        allSectors = addIntoSector(allSectors,
                                                        sectorName,
                                                        familyInfo,
                                                        repr(specialLocation))
    for fname in extras:
        sectors = organizeSectors(fname, sectorDefs, EXTRA_WARD_TAG)
        try:
            del sectors[UNKNOWN_INFO_TAG]
        except:
            pass
        try:
            del sectors[None]
        except:
            pass
        for sector in sectors.keys():
            try:
                allSectors[sector] += sectors[sector]
            except KeyError:
                allSectors[sector] = sectors[sector]
    ts = time.localtime(os.stat(inFileName)[stat.ST_MTIME])
    genSectors(outFileName, allSectors, sectorDefs, ts)

def defaultFileExtension(fn, exts=[]):
    x = os.path.splitext(fn)[1]
    if not x:
        fn += ext[0]
    else:
        assert(x in exts)
    return fn

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage:")
        print("    python %s definitions, members, report[, extraMembers1[, extraMembers2[, ...]]]" % sys.argv[0])
        print
        print("Where:")
        print("    definitions     The .py filename which contains the Sector organization")
        print("                      definitions.")
        print("    members         The .csv filename which contains the Ward Membership")
        print("                      information.")
        print("    report          The filename to receive the generated Ward Sector report.")
        print("    extraMembers    Additional optional Membership information files.")
        print("                      The additional membership files differ from the main")
        print("                      membership file in that members lying outside of any")
        print("                      Sector will be omitted from the generated report.")
        sys.exit(1)
    parameterDefName = defaultFileExtension(sys.argv[1], ['.py', '.pyc', '.PY', '.PYC'])
    fn = defaultFileExtension(sys.argv[2], ['.csv', '.CSV'])
    if len(sys.argv) > 3:
        ofn = defaultFileExtension(sys.argv[3], ['.txt', '.TXT'])
    else:
        ofn = os.path.splitext(fn)[0] + '.txt'
    extras = []
    if len(sys.argv) > 4:
        for extraFn in sys.argv[4:]:
            extras.append(defaultFileExtension(extraFn, ['.csv', '.CSV']))

    main(parameterDefName, fn, ofn, extras)
