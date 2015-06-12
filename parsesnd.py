import json
import pprint
from cow import SType, NonSType
from cowdef import isAddressType


def sndFileData(sndFile):
    lines = open(sndFile).readlines()
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


def processSND(sndFile):

    header, records = sndFileData(sndFile)
    pprint.pprint(header)

    dSCode2Names = {}
    for rec in records:
        gft = rec[50:51]
        parsedGeoFT = ' '

        if gft == 'S':
            entry = SType(rec) 
            parsedGeoFT = entry.progenitor1.geographicFeatureType
        else:
            entry = NonSType(rec)
            parsedGeoFT = entry.geographicFeatureType

            if entry.primaryStreetNameIndicator == 'V' or \
                entry.principalLocalGroupNameIndicator == 'S':
                continue

        if not isAddressType(parsedGeoFT):
            continue

        for loc in entry.streets():
            dSCode2Names.setdefault(loc['b10sc'].b7sc(),[]).append(loc)

    for k in sorted(dSCode2Names.keys()):
        group = sorted(dSCode2Names[k], key=lambda e: e['name'])
        for g in group:
            print ('{}\t{}\t{}\t'.format(k, 
                                         g['name'], 
                                         g['b10sc'].borough()), 
                                         g['trace'])
        print( '\n')


if __name__ == '__main__':
    processSND('snd15Bcow.txt')
