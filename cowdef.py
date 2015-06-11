_vsam_keys = [
    ('filler', 0, 1),
    ('boroughCode', 1, 2),
    ('geographicFeatureName', 2, 34)
]

_type_s_keys = [
    ('filler1', 34, 49),
    ('numericNameIndicator', 49, 50),
    ('geographicFeatureName', 50, 51),
    ('fullNameLength', 51, 53),
    ('progenitorCount', 53, 54),
    ('filler2', 86, 200)
]

_type_non_s_b10sc = [
    ('boroughCode', 36, 37),
    ('streetCode', 37, 42),
    ('localGroupCode', 42, 44),
    ('spellingVariation', 44, 47)
]

_progen_1_b10sc = [
    ('boroughCode', 56, 57),
    ('streetCode', 57, 62),
    ('localGroupCode', 62, 64),
    ('spellingVariation', 64, 67)
]

_progen_2_b10sc = [
    ('boroughCode', 73, 74),
    ('streetCode', 74, 79),
    ('localGroupCode', 79, 81),
    ('spellingVariation', 81, 84)
]

_progenitor1 = [
    ('word', 54, 55),
    ('geographicFeatureType', 55, 66),
    ('horizontalTopologyFlag', 67, 68)
]

_progenitor2 = [
    ('word', 70, 71),
    ('geographicFeatureType', 71, 72),
    ('horizontalTopologyFlag', 83, 84)
]

_type_non_s_keys = [
    ('primaryStreetNameIndicator', 34, 35),
    ('principalLocalGroupNameIndicator', 35, 36),
    ('filler1', 47, 49),
    ('numericNameIndicator', 49, 50),
    ('geographicFeatureType', 50, 51),
    ('progenitorLength', 51, 53),
    ('progenitorFullStreetName', 53, 85),
    ('minimunStreetNameLength', 85, 87),
    ('twentyByteStreetName', 87, 107),
    ('horizontalTypologyTypeCode', 107, 108),
    ('filler2', 108, 200)

]


# oh boy
def process(obj, lAttributes, rec):
    for atr, start, end in lAttributes:
        obj.__dict__[atr] = rec[start:end].strip()


boroughMap = {
    '1': 'Manhattan',
    '2': 'Bronx',
    '3': 'Brooklyn',
    '4': 'Queens',
    '5': 'Staten Island'
}
