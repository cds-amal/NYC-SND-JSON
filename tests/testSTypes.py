import sys
sys.path.append('..')

import unittest
from nose.plugins.skip import SkipTest
from nose.plugins.attrib import attr

from cow import SType

class STypeTest(unittest.TestCase):

    def setUp(self):
        rec = "11   1 STREET                                    NS161E 11701001010   " \
              "                                                                      " \
              "                                                            \r\n"
        self.rec = SType(rec)

    def test_filler(self):
        self.assertEqual(self.rec.filler1, " " * 15)
        self.assertEqual(self.rec.filler2, " " * 114)

    def test_fullNameLength(self):
        self.assertEqual(self.rec.fullNameLength, "16")

    def test_geographicFeatureName(self):
        self.assertEqual(self.rec.geographicFeatureName, "S")

    def test_numericNameIndicator(self):
        self.assertEqual(self.rec.numericNameIndicator, "N")

    def test_progenitorCount(self):
        self.assertEqual(self.rec.progenitorCount, "1")

    def test_progenitorCount(self):
        self.assertEqual(self.rec.progenitorCount, "1")

    def test_progenitor2(self):
        self.assertEqual(self.rec.progenitor2, None)

    def test_vsam(self):
        v = self.rec.vsam
        self.assertEqual(v.boroughCode, "1")
        self.assertEqual(v.filler, "1")
        self.assertEqual(v.geographicFeatureName, 
                         "   1 STREET                     ")

    def test_progenitor1(self):
        p = self.rec.progenitor1
        self.assertEqual(p.geographicFeatureType, " ")
        self.assertEqual(p.horizontalTopologyFlag, " ")
        self.assertEqual(p.word, "E")

        b = p.b10sc
        self.assertEqual(b.boroughCode, "1")
        self.assertEqual(b.localGroupCode, "01")
        self.assertEqual(b.spellingVariation, "010")
        self.assertEqual(b.streetCode, "17010")



# rec = "11   1 AVENUE                     PF11001001010  N 11   1 AVENUE      " \
#       "                                                                      " \
#       "                                                            \r\n"
# nstype = NonSType(rec)
# print 'nonSType.to_JSON() = %s' % nstype.to_JSON()
