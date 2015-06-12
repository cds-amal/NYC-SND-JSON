import json
import pprint
from cow import SType, NonSType
from cowdef import isAddressType


def sndFileData():
    lines = open('snd15Bcow.txt').readlines()
    header = lines[0]  # file header

    headerId = header[:8]
    dateFileCreated = header[8:14]
    geoSupportRelease = header[14:18]
    numberOfRecords = header[18:26]

    # print '[%s]' % headerId
    # print '[%s]' % dateFileCreated
    # print '[%s]' % geoSupportRelease
    # print '[%s]' % numberOfRecords

    return dict(
        headerId=headerId,
        dateFileCreated=dateFileCreated,
        geoSupportRelease=geoSupportRelease,
        numberOfRecords=numberOfRecords
    ), lines[1:]


header, records = sndFileData()
pprint.pprint(header)

streets = []
nons = {}
for rec in records:
    gft = rec[50:51]
    if gft == 'S':
        entry = SType(rec) 
        geoFeatureType = entry.progenitor1.geographicFeatureType
        if not isAddressType(geoFeatureType):
            continue
    else:
        entry = NonSType(rec)
        if not isAddressType(entry.geographicFeatureType):
            continue

        if entry.primaryStreetNameIndicator == 'V' or \
            entry.principalLocalGroupNameIndicator == 'S':
            continue

        geoFeatureType = entry.geographicFeatureType

    for loc in entry.streets():
        nons.setdefault(loc['b10sc'].b7sc(),[]).append(loc)

for k in sorted(nons.keys()):
    group = sorted(nons[k], key=lambda e: e['name'])
    for g in group:
        print ('{}\t{}\t{}\t'.format(k, g['name'], g['b10sc'].borough()), g['trace'])
    print( '\n')
