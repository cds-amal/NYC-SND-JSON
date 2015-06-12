import json
import cowdef
import pdb

class B10sc:
    def __init__(self, dic, rec):
        self.boroughCode = cowdef.extract(rec, dic, 'boroughCode')
        self.streetCode = cowdef.extract(rec, dic, 'streetCode')
        self.localGroupCode = cowdef.extract(rec, dic, 'localGroupCode')
        self.spellingVariation = cowdef.extract(rec, dic, 'spellingVariation')
        # if self.boroughCode not in ['1', '2', '3', '4', '5']:
        #     pdb.set_trace()

    def borough(self):
        return cowdef.boroughMap[self.boroughCode]

    def b5sc(self):
        # borough + 5-digit street code
        return '%s%s' % (self.boroughCode, self.streetCode)

    def b7sc(self):
        # borough + 7-digit street code
        return '%s%s%s' % \
            (self.boroughCode, self.streetCode, self.localGroupCode)

    def __str__(self):
        return '%s%s%s%s' % \
            (self.boroughCode, self.streetCode, 
             self.localGroupCode, self.spellingVariation)


class Progenitor:
    def __init__(self, num, rec):
        _p = None
        if num == 1:
            _p = cowdef._progenitor1
            _b = cowdef._progen_1_b10sc
        elif num == 2:
            _p = cowdef._progenitor2
            _b = cowdef._progen_2_b10sc

        if _p:
            self.word = cowdef.extract(rec, _p, 'word')
            self.geographicFeatureType = cowdef.extract(
                                            rec, _p, 'geographicFeatureType')
            self.horizontalTopologyFlag = cowdef.extract(
                                            rec, _p, 'horizontalTopologyFlag')
            self.b10sc = B10sc(_b, rec)
        else:
            raise Exception('Unknown Progenitor number')

    def word(self):
        if self.word == 'E':
            return 'East'
        elif self.word == 'W':
            return 'West'
        else:
            raise Exception('Invalid word value: %s' % self.word)

    def __str__(self):
        return 'gft:{}, htf:{}'.format(self.geographicFeatureType,
                                       self.horizontalTopologyFlag)


class VSam:

    def __init__(self, rec):
        dic = cowdef._vsam_keys
        self.filler = cowdef.extract(rec, dic, 'filler')
        self.boroughCode = cowdef.extract(rec, dic, 'boroughCode')
        self.geographicFeatureName = cowdef.extract(rec, dic, 
                                                    'geographicFeatureName')

    def borough(self):
        return cowdef.boroughMap[self.boroughCode]


class SType:

    def __init__(self, rec):
        self.vsam = VSam(rec)
        dic = cowdef._type_s_keys

        self.filler1 = cowdef.extract(rec, dic, 'filler1')
        self.numericNameIndicator = cowdef.extract(rec, dic, 'numericNameIndicator')
        self.geographicFeatureName = cowdef.extract(rec, dic, 'geographicFeatureName')
        self.fullNameLength = cowdef.extract(rec, dic, 'fullNameLength')
        self.progenitorCount = cowdef.extract(rec, dic, 'progenitorCount')
        self.filler2 = cowdef.extract(rec, dic, 'filler2')

        self.progenitor1 = Progenitor(1, rec)
        self.progenitor2 = None
        if self.progenitorCount == '2':
            self.progenitor2 = Progenitor(2, rec)

    def streets(self):
        names = [{'name': '%s %s' % (self.progenitor1.word,
                                     self.vsam.geographicFeatureName),
                  'b10sc': self.progenitor1.b10sc,
                  'trace': str(self.progenitor1)}]

        if self.progenitor2:
            names.append({'name': '%s %s' % (self.progenitor2.word,
                                             self.vsam.geographicFeatureName),
                          'b10sc': self.progenitor2.b10sc,
                          'trace': str(self.progenitor2)})

        return names

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class NonSType:

    def __init__(self, rec):
        self.vsam = VSam(rec)
        self.b10sc = B10sc(cowdef._type_non_s_b10sc, rec)

        dic = cowdef._type_non_s_keys
        self.filler1 = cowdef.extract(rec, dic, 'filler1')
        self.filler2 = cowdef.extract(rec, dic,'filler2')

        self.primaryStreetNameIndicator = cowdef.extract(rec, dic,
                                                         'primaryStreetNameIndicator')
        self.principalLocalGroupNameIndicator = cowdef.extract(rec, dic,
                                                               'principalLocalGroupNameIndicator')
        self.numericNameIndicator = cowdef.extract(rec, dic,
                                                   'numericNameIndicator')
        self.geographicFeatureType = cowdef.extract(rec, dic,
                                                    'geographicFeatureType')
        self.progenitorLength = cowdef.extract(rec, dic, 'progenitorLength')
        self.progenitorFullStreetName = cowdef.extract(rec, dic,
                                                       'progenitorFullStreetName')
        self.minimumStreetNameLength = cowdef.extract(rec, dic,
                                                      'minimunStreetNameLength')
        self.twentyByteStreetName = cowdef.extract(rec, dic,
                                                   'twentyByteStreetName')
        self.horizontalTypologyTypeCode = cowdef.extract(rec, dic,
                                                         'horizontalTypologyTypeCode')

    def borough(self):
        return self.vsam.borough()

    def streets(self):
        return [{'name': self.vsam.geographicFeatureName,
                 'b10sc': self.b10sc,
                 'trace': 'gft:{}, htf:{}'.format(self.geographicFeatureType,
                                       self.horizontalTypologyTypeCode)}]
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

rec = " 15FATHER SPYRIDON MACRIS PARK     VS53734801030    27FATHER SPYRIDON MACRIS PARK                                                                                                                        "
rec = "11   1 AVENUE                     PF11001001010  N 11   1 AVENUE                                                                                                                                        \n"
gft = rec[50:51]
rec = SType(rec) if gft == 'S' else NonSType(rec)
print (rec.to_JSON())
