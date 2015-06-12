_type_non_s_b10sc = {
    'boroughCode': (36, 37),
    'streetCode': (37, 42),
    'localGroupCode': (42, 44),
    'spellingVariation': (44, 47)
}

_progen_1_b10sc = {
    'boroughCode': (56, 57),
    'streetCode': (57, 62),
    'localGroupCode': (62, 64),
    'spellingVariation': (64, 67)
}

_progen_2_b10sc = {
    'boroughCode': (72, 73),
    'streetCode': (73, 78),
    'localGroupCode': (78, 80),
    'spellingVariation': (80, 83)
}

_vsam_keys = {
    'filler': (0, 1),
    'boroughCode': (1, 2),
    'geographicFeatureName': (2, 34)
}

_type_s_keys = {
    'filler1': (34, 49),
    'numericNameIndicator': (49, 50),
    'geographicFeatureName': (50, 51),
    'fullNameLength': (51, 53),
    'progenitorCount': (53, 54),
    'filler2': (86, 200)
}

_progenitor1 = {
    'word': (54, 55),
    'geographicFeatureType': (55, 56),
    'horizontalTopologyFlag': (67, 68)
}

_progenitor2 = {
    'word': (70, 71),
    'geographicFeatureType': (71, 72),
    'horizontalTopologyFlag': (83, 84)
}

_type_non_s_keys = {
    'primaryStreetNameIndicator': (34, 35),
    'principalLocalGroupNameIndicator': (35, 36),
    'filler1': (47, 49),
    'numericNameIndicator': (49, 50),
    'geographicFeatureType': (50, 51),
    'progenitorLength': (51, 53),
    'progenitorFullStreetName': (53, 85),
    'minimunStreetNameLength': (85, 87),
    'twentyByteStreetName': (87, 107),
    'horizontalTypologyTypeCode': (107, 108),
    'filler2': (108, 200)
}


boroughMap = {
    '1': 'Manhattan',
    '2': 'Bronx',
    '3': 'Brooklyn',
    '4': 'Queens',
    '5': 'Staten Island'
}


stype__geographic_feature_types = {
    'A': 'Addressable place name',
    'B': 'Name of bridge',
    'C': 'Business Improvement Districts',
    'D': 'Duplicate Address Pseudo-Street name (DAPS)',
    'E': 'Street is entirely within Edgewater Park',
    'F': 'Street is partially within Edgewater Park',
    'G': 'Non-Addressable Place name (NAP) of a complex',
    'H': 'All house numbers on this street are hyphenated',
    'I': 'Intersection Name',
    'J': 'Non-Physical Boundary Features',
    'M': 'Some house numbers on this street are hyphenated, some ' \
          'are not',
    'N': 'NAP of a "stand-alone" geographic feature (not a complex) ' \
         'or a constituent entity of a complex)',
    'O': 'Shore Line',
    'P': 'Pseudo-street name (BEND, CITY LIMIT, DEAD END and their ' \
         ' aliases)',
    'R': 'Rail line',
    'S': 'Front-truncated street name',
    'T': 'Tunnel',
    'U': 'Miscellaneous Structures',
    'X': 'NAP of a constituent entity of a complex Z Ramp'
}

def isAddressType(featureType):
    return featureType in ['A', 'E', 'F', 'H', 'M', 'S']

def extract(rec, dic, key):
    start, end = dic[key]
    return rec[start:end]


