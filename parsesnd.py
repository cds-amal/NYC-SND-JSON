import json
import pprint
from cow import SType, NonSType


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
    entry = SType(rec) if gft == 'S' else NonSType(rec)

    if gft != 'S':
        nons.setdefault(entry.b10sc.b5sc(), []).append(entry)
    # streets += entry.streets()
    # for s in streets:
    #     print s

for k in nons.keys():
    group = sorted(nons[k], key=lambda e: e.primaryStreetNameIndicator)
    geoFeatureType = group[0].geographicFeatureType
    # if geoFeatureType in ['Z', 'X', 'U', 'T', 'S', 'R', 'P', 'O', 'N',
    #                       'J', 'I', 'G', 'C', 'B']:
    #     continue

    # useful list to print later
    # if geoFeatureType in ['M', 'H', 'F', 'E', 'D', 'A', '']:
    #     continue

    # if group[0].geographicFeatureType != '':
    #     continue
    print(k)
    # print json.dumps(group[0].to_JSON())
    for entry in group:
        if entry.primaryStreetNameIndicator == 'P':
            print('{} {}s'.format(entry.streets()[0]['name'], entry.vsam.borough()))
        else:
            print('\t{}'.format(entry.streets()[0]['name']))
    print
