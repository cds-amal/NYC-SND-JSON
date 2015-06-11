import pprint


def sndFileData():
    lines = open('snd15Bcow.txt').readlines()
    header = lines[0]  # file header

    headerId = header[:8]
    dateFileCreated = header[8:14]
    geoSupportRelease = header[14:18]
    numberOfRecords = header[18:26]

    print '[%s]' % headerId
    print '[%s]' % dateFileCreated
    print '[%s]' % geoSupportRelease
    print '[%s]' % numberOfRecords

    return dict(
        headerId=headerId,
        dateFileCreated=dateFileCreated,
        geoSupportRelease=geoSupportRelease,
        numberOfRecords=numberOfRecords
    ), lines[1:]


header, records = sndFileData()
import json
from cow import SType, NonSType

pprint.pprint(header)
for rec in records:
    gft = rec[50:51]
    entry = SType(rec) if gft == 'S' else NonSType(rec)

    print entry.to_JSON()

