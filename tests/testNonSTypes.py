import sys
sys.path.append('..')

import unittest
from nose.plugins.skip import SkipTest
from nose.plugins.attrib import attr

from cow import NonSType

class NonSTypeTest(unittest.TestCase):

    def setUp(self):
        rec = "11   1 AVENUE                     PF11001001010  N 11   1 AVENUE      " \
              "                                                                      " \
              "                                                            \r\n"
        self.rec = NonSType(rec)

    def test_filler(self):
        self.assertEqual(self.rec.filler1, " " * 2)
        self.assertEqual(self.rec.filler2, " " * 92)

    def test_geographicFeatureType(self):
        self.assertEqual(self.rec.geographicFeatureType, " ")

    def test_horizontalTypologyTypeCode(self):
        self.assertEqual(self.rec.horizontalTypologyTypeCode, " ")

    def test_minimumStreetNameLength(self):
        self.assertEqual(self.rec.minimumStreetNameLength, "  ")

    def test_primaryStreetNameIndicator(self):
        self.assertEqual(self.rec.primaryStreetNameIndicator, "P")

    def test_principalLocalGroupNameIndicator(self):
        self.assertEqual(self.rec.principalLocalGroupNameIndicator, "F")

    def test_progenitorFullStreetName(self):
        self.assertEqual(self.rec.progenitorFullStreetName,
                         "   1 AVENUE                     ")

    def test_progenitorLength(self):
        self.assertEqual(self.rec.progenitorLength, "11")

    def test_twentyByteStreetName(self):
        self.assertEqual(self.rec.twentyByteStreetName, " " * 20)

    def test_numericNameIndicator(self):
        self.assertEqual(self.rec.numericNameIndicator, "N")

    def test_vsam(self):
        v = self.rec.vsam
        self.assertEqual(v.boroughCode, "1")
        self.assertEqual(v.filler, "1")
        self.assertEqual(v.geographicFeatureName,
                         "   1 AVENUE                     ")

    def test_b10sc(self):
        b = self.rec.b10sc
        self.assertEqual(b.boroughCode, "1")
        self.assertEqual(b.localGroupCode, "01")
        self.assertEqual(b.spellingVariation, "010")
        self.assertEqual(b.streetCode, "10010")
