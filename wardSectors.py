#
# Define the values for:
#       WARD_NAME   to contain the name of the Ward.
#       EXTRA_WARD_TAG  to contain the identifier for members from extra Wards.
#       HAM_OPERATOR_TAG    to contain the identifier for a HAM Radio Operator.
#       GpsSectorDefs   to define the GPS coordinates defining the outlines of
#       the Sectors.
#       SectorCaptains to define the set of Sector Captains for each Sector.
#       HamOperators    to define the set of HAM Radio Operators in the Ward.
#
#   Additional definitions are useful for helping to define the values
#   designated above, but have no other harmful nor helpful effect with
#   regards to the successful execution of the wardEmergencySectors program.
#
# NOTE: Blank lines and any line which starts with # is ignored.
#
# Leave the following two lines unchanged:
global GpsSectorDefs, SectorCaptains, SpecialLocations, NameTags
global WARD_NAME, EXTRA_WARD_TAG
#

WARD_NAME       = 'YOUR WARD NAME GOES HERE'
EXTRA_WARD_TAG      = '.'


#
# List all of the cross-streets which form the corners of your
# neighborhood & Sector boundaries.
# This list of cross-streets can grow as long as you wish, in addition
# they don't have to all be utilized, or even street corners, for that matter.
# These names will be utilized in the next section and must be spelled
# and capitalized in exactly the same way that you chose them for this section.
#
# Here are two web-sites that make latitude & longitude easy to determine:
#       http://universimmedia.pagesperso-orange.fr/geo/loc.htm
#       http://itouchmap.com/latlong.html
#
_405_55                 = (33.68796, -117.87167)
_Alton_Culver           = (33.68089, -117.81159)
_Alton_Jamboree     = (33.68846, -117.83210)
_Alton_PaseoW           = (33.68246, -117.81768)
_Armstrong_Warner   = (33.70810, -117.83283)
_Barranca_PaseoW    = (33.68674, -117.81375)
_Culver_405             = (33.66946, -117.82283)
_Culver_5                   = (33.71113, -117.78142)
_Culver_Barranca        = (33.68396, -117.80811)
_Culver_IrvineCtr       = (33.69350, -117.79889)
_Culver_Main            = (33.67593, -117.81631)
_HarvSq_5               = (33.71274, -117.78528)
_HarvSq_Walnut      = (33.71008, -117.79432)
_Harvard_405            = (33.67246, -117.83189)
_Harvard_Alton          = (33.68455, -117.82646)
_Harvard_Barranca   = (33.68835, -117.81846)
_Harvard_Edinger        = (33.70101, -117.80256)
_Harvard_Moffett        = (33.69812, -117.80539)
_Harvard_Poplar     = (33.70669, -117.79753)
_Harvard_SanCarlo   = (33.68025, -117.82991)
_Harvard_SanLeon    = (33.68590, -117.82466)
_Harvard_Walnut     = (33.71117, -117.79640)
_Harvard_estAlton       = (33.68403, -117.82682)
_Hearthst_IrvineCtr = (33.69735, -117.80107)
_Jamboree_405           = (33.67671, -117.84373)
_Jamboree_5             = (33.71956, -117.79532)
_Jamboree_Barranca  = (33.69408, -117.82676)
_Jamboree_Edinger   = (33.70424, -117.80622)
_Jamboree_McGaw = (33.68557, -117.83502)
_Jamboree_Moffett   = (33.70127, -117.80974)
_Jamboree_Walnut    = (33.71174, -117.80133)
_MacArthur_405      = (33.68278, -117.85772)
_Main_Harvard           = (33.67762, -117.83118)
_Main_Jamboree      = (33.68075, -117.83953)
_Main_PaseoW            = (33.67864, -117.82059)
_Main_SM2Harvard    = (33.67691, -117.82841)
_Main_SanMateo      = (33.67739, -117.82609)
_Manchester_405     = (33.67219, -117.83086)
_McGaw_Armstrong    = (33.69349, -117.84614)
_PaseoW_405         = (33.67071, -117.82640)
_RR_Culver              = (33.69906, -117.79335)
_RR_Harvard             = (33.70371, -117.79992)
_RR_Jamboree            = (33.70649, -117.80416)
_StaMaria_IrvineCtr = (33.69918, -117.80148)
_Walnut_Culver          = (33.70463, -117.78764)
_Walnut_TheMall     = (33.70860, -117.79204)
_Warner_55              = (33.71563, -117.84489)
_Warner_Culver      = (33.68842, -117.80416)
_Warner_Harvard     = (33.69250, -117.81266)
_Warner_Park            = (33.70110, -117.82000)
_Warner_Jamboree    = (33.69839, -117.81914)
_Warner_PaseoW      = (33.69000, -117.81060)
_Warner_StaYnez     = (33.68942, -117.80728)


#
# In this section the actual Sectors and Neighborhoods within the Sectors are
# defined.
#
# List the Sector name, then the Neighborhood name, followed by the set of
# corners which define this Neighborhood within the Sector.  The set of
# corners do not need to conform to a square, but can be a polygon of any
# number (>=3) of corners.  The corners must be listed in a contiguous order
# (either going around clock-wise or counter-clock-wise, it doesn't matter).
# The connections between each corner are assumed to be an entirely
# straight line, so if a street is curvy it may be necessary to have several
# intermediate corners, proceeding along up the street.  (For that matter
# the boundary doesn't even need to be a street, it just needs to be specified
# by the actual geo-code (i.e., latitude and longitude) values).
#
GpsSectorDefs = [           \
    (('Walnut', 'Harvard Square'), (_HarvSq_Walnut, _Jamboree_Walnut, _Jamboree_5, _HarvSq_5)),
    (('Walnut', 'Colony'), (_Walnut_Culver, _HarvSq_Walnut, _HarvSq_5, _Culver_5)),
    (('Walnut', 'College Park'), (_RR_Culver, _RR_Harvard, _Harvard_Poplar, _Harvard_Walnut, _Walnut_Culver)),
    (('Walnut', 'Park Lane'), (_RR_Harvard, _RR_Jamboree, _Jamboree_Walnut, _Harvard_Walnut, _Harvard_Poplar)),
    (('Walnut', '*Unknown Section Within Walnut Sector*'), (_RR_Culver, _RR_Jamboree, _Jamboree_5, _Culver_5)),
    (('Center', 'Tustin Fields'), (_Harvard_Moffett, _Jamboree_Moffett, _RR_Jamboree, _RR_Harvard)),
    (('Center', 'Tustin Fields'), (_Warner_Harvard, _Warner_Jamboree, _Jamboree_Moffett, _Harvard_Moffett)),        # 'Columbus Grove'
    (('Center', 'Windwood'), (_Culver_IrvineCtr, _Hearthst_IrvineCtr, _Harvard_Edinger, _RR_Harvard, _RR_Culver)),
    (('Center', 'Plaza Vista'), (_Warner_Culver, _Warner_StaYnez, _Warner_PaseoW, _Warner_Harvard, _Harvard_Edinger, _StaMaria_IrvineCtr, _Hearthst_IrvineCtr, _Culver_IrvineCtr)),
    (('Center', '*Unknown Section Within Center Sector*'), (_Warner_Culver, _Warner_PaseoW,  _Warner_Harvard, _Warner_Jamboree, _RR_Jamboree, _RR_Culver)),
    (('Barranca', 'Santa Ynez'), (_Culver_Barranca, _Barranca_PaseoW, _Harvard_Barranca, _Warner_Harvard, _Warner_PaseoW, _Warner_StaYnez, _Warner_Culver)),
    (('Barranca', 'Sweet Shade'), (_Harvard_Barranca, _Jamboree_Barranca, _Warner_Park, _Warner_Harvard)),
    (('Barranca', 'San Remo'), (_Alton_Culver, _Alton_PaseoW, _Harvard_estAlton, _Harvard_SanLeon, _Harvard_Barranca, _Barranca_PaseoW, _Culver_Barranca)),
    (('Barranca', 'City Hall'), (_Harvard_estAlton, _Alton_Jamboree, _Jamboree_Barranca, _Harvard_Barranca)),
    (('Barranca', '*Unknown Section Within Barranca Sector*'), (_Alton_Culver, _Alton_PaseoW, _Harvard_estAlton,  _Alton_Jamboree, _Warner_Jamboree, _Warner_Harvard,  _Warner_PaseoW, _Warner_Culver)),
    (('Main', 'San Carlo'), (_Culver_Main, _Main_PaseoW, _Main_SanMateo, _Main_SM2Harvard, _Main_Harvard, _Harvard_estAlton, _Alton_PaseoW, _Alton_Culver)),
    (('Main', 'San Leandro'), (_Culver_405, _Manchester_405, _Main_SanMateo, _Main_PaseoW, _Culver_Main)),
    (('Main', 'Coronado'), (_Manchester_405, _Harvard_405, _Main_Harvard, _Main_SanMateo)),
    (('Main', 'Coronado'), (_Harvard_405, _Jamboree_405, _Main_Jamboree, _Main_Harvard, _Main_SanMateo)),
    (('Main', 'San Marco'), (_Main_Harvard, _Main_Jamboree, _Alton_Jamboree, _Harvard_Alton, _Harvard_estAlton, _Harvard_SanCarlo)),
    (('Main', 'Kelvin'), (_Jamboree_405, _MacArthur_405, _McGaw_Armstrong, _Jamboree_McGaw, _Alton_Jamboree)),
    (('Main', '*Unknown Section Within Main Sector*'), (_Culver_405, _PaseoW_405,  _Harvard_405, _Jamboree_405, _Alton_Jamboree, _Harvard_estAlton, _Alton_PaseoW, _Alton_Culver)),
    (('Corporate', 'Business District'), (_MacArthur_405, _405_55, _Warner_55, _Armstrong_Warner, _McGaw_Armstrong)),
    (('Corporate', '*Unknown Section Within Corporate Sector*'), (_Jamboree_405, _MacArthur_405, _McGaw_Armstrong, _Jamboree_McGaw)),
    (('Corporate', '*Unknown Section Within Corporate Sector*'), (_MacArthur_405, _405_55, _Warner_55, _Armstrong_Warner)),
]

#
# If you wish to assign Sector Captains, then they can be defined in this section.
#
# The Sector name must match the same spelling and capitalization as used in the
# preceding section (for the GpsSectorDefs).
# The name, address, phone, and email information can be any values you wish
# to have listed as part of the Sector Captain information for that Sector.
#
# Here's an example involving 2 Sectors (Mountain Sector and River Sector),
# with 2 Captains each:
#
#   SectorCaptains = {      \
#       'Mountain': [("Smith, Joseph & Emma","123 Maple Str.","111-222-3333","smith@lds.com"),
#                       ("Young, Brigham","99 Temple Way","111-223-4444",""),
#       ],
#       'River':    [("Brown, David & Lisa","29 Creek Way","111-222-5678","brownfamily@abc.com"),
#                       ("Jones, Fred & Sue","76 Trombones","111-333-4444","jones2195@gmail.com"),
#       ],
#   }
#
SectorCaptains = {      \
    'Barranca': [("Scott, Jared & Chelsea","429 Durazno","949-322-0256","jared@jaredscottmusic.com"),
                        ("Reese, Pat & Deborah","300 Santa Barbara","949-653-8570","gaylord.reese@cox.net"),
                        ("Moody, Steven & Jenna","1105 Abelia Street","949-378-3780","smoody263@yahoo.com")],
    'Center':       [ ("Knutson, Gregg & Stephanie","1 Marseille","949-654-4304","gregg.knutson@gmail.com"),
                        ("Robertson, Michael & Holly","3306 Columbus Grove Dr.","949-748-6861","mgrobertson@gmail.com"),
                        ("Jordan, Jason & Katie", "2 Flagstone, Apt. 214", "714-365-6158", "jordantex@gmail.com")],
    'Main':     [("Hicken, Doug & Rosanna","399 Giotto","801-669-6647","dghicken@gmail.com"),
                        ("Durham, Eric & Kira","2552 Kelvin Ave. #213","909-282-7298","etdurham@gmail.com"),
                        ("Remington, Richard & Andrea","7 Bormes","949-629-1187","richardremington@mac.com"),
                        ("Kimball, David & Karen","17541 Manchester Ave","949-552-7877","cakimballs7@cox.net"),
                        ("Esselman, Michael & Kirsten","14 Marbella","801-592-4318","michaelesselman@gmail.com")],
    'Walnut':       [("Dudley, Jim & Janine","14802 Yucca Ave","949-246-3243","jim_dudley@ahm.honda.com"),
                        ("Robinson, Greg & Jillair","","949-552-0965","ger@rrlawyers.com"),
                        ("Bush, Elijah & Marinda","33 Rhode Island","801-505-1468","elijahbush@gmail.com"),
                        ("Espinili, Riz & Kathe","85 St. James","949-263-0922","rizrn@mac.com")],
}

#
# In this section you can list special locations to be included each time
# even though this information will not be found in any of the input files
# of membership information.  You will determine which neighborhood
# each location is to appear in.
#
# For example, Church Buildings and/or Missionaries living within your
# Ward.
# Each line of special location information contains:
#   ("Name", ("SectorName", "Neighborhood"), "Address", "City", "State", "Zip", "Phone")
# NOTE: The name can be preceded with special characters to set it apart.
# By default the name will be outdented by 2 spaces to allow it to stand apart
# from the other names easily.  If you do not wish the name to stand out then
# insert two blanks in front of the text of the name.
#
SpecialLocations = [        \
    ("MISSIONARIES", ("Main", "Kelvin"), "2760 Kelvin Ave #3115","Irvine","California","92614", "714-612-4528"),
]

NameTags = [        \
    #
    # In this section HAM Radio operators can be listed, together with
    # their call sign.
    # The last name must match the spelling and capitalization of the person's
    # last name in the Ward List to be processed.  The same is true for the
    # person's first names.  I say first names, because sometimes the person
    # has more than a single name listed.  For example, suppose that
    # Sue Henry has a HAM Radio license: KA6AAA, and suppose that
    # she is found in the Ward List information as follows:
    #       Henry, John & Susan May.
    # Then she would be listed as follows:
    #       ('KA6AAA', 'Henry', 'Susan May'),
    #
    ([      \
        ('KJ6TNG', 'Bianchini', 'Richard Anthony'),
        ('KI6SXC', 'Durham', 'Eric'),
        ('KI6GLQ', 'Espinili', 'Riz'),
        ('KB6OHC', 'Fraser', 'Barbara'),
        ('KI6SKD', 'Jensen', 'Jon'),
        ('KI6GMK', 'Kennedy', 'Elizabeth'),
#       ('KI6HXH', 'Kimball', 'Stephen'),
        ('KI6HXI', 'Kimball', 'David'),
        ('KI6HXJ', 'Kimball', 'Cameron'),
#       ('KI6QJW', 'Kimball', 'Rose'),
        ('KI6QJX', 'Kimball', 'Karen'),
        ('KI6SJP', 'Kimball', 'Rebecca'),
        ('KG6CCY', 'Knutson', 'Gregg'),
        ('KG6JYZ', 'Knutson', 'Stephanie'),
        ('KI6GMM', 'Lawrence', 'Cliff'),
        ('KI6CUZ', 'Marchese', 'Frank'),
#       ('KI6GMR', 'McDougle', 'Scott'),
        ('KI6SJY', 'Moon', 'Greg'),
        ('KG6YXL', 'Nelson', 'Allison'),
        ('KG6YXM', 'Nelson', 'Philip'),
        ('KI6GNK', 'Reese', 'Deborah'),
        ('KI6GNL', 'Reese', 'Pat'),
        ('KI6QJY', 'Remington', 'Michael'),
        ('KJ6UFC', 'Robertson', 'Michael'),
        ('KI6GNN', 'Robinson', 'Greg'),
        ('KI6GNO', 'Robinson', 'Jillair'),
        ('KE6LJH', 'Scott', 'Jared'),
        ('KI6GNR', 'Smith', 'Kevin'),
        ('KI6HWV', 'Smith', 'Ammon'),
    ], '*'),
    # I would like to list people with Medical training here.
    ([      \
    ], '+')
]
