import sys
sys.path.append('..')

import unittest
from nose.plugins.skip import SkipTest
from nose.plugins.attrib import attr

from cow import SType,NonSType
import json

def sndFileData():
    lines = open('../snd15Bcow.txt').readlines()
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


@SkipTest
class BoroughsTest(unittest.TestCase):

    def setUp(self):
        _, self.records = sndFileData()

    def testNonSType(self):
        for rec in self.records:
            if rec[50] != 'S':
                print( 'Entry:[{}]'.format(json.dumps(rec)))
                entry = NonSType(rec)
                print (entry.to_JSON())
                self.assertIn(entry.vsam.boroughCode, ['1','2','3', '4', '5'])



