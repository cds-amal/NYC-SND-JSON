import json
import cowdef

class B10sc:
    def __init__(self, dic, rec):
        self.boroughCode = cowdef.extract(rec, dic, 'boroughCode')
        self.streetCode = cowdef.extract(rec, dic, 'streetCode')
        self.localGroupCode = cowdef.extract(rec, dic, 'localGroupCode')
        self.spellingVariation = cowdef.extract(rec, dic, 'spellingVariation')

    def borough(self):
        return cowdef.boroughMap[self.boroughCode]

    def b5sc(self):
        # borough + 5-digit street code
        return '%s%s' % (self.boroughCode, self.streetCode)

    def b7sc(self):
        # borough + 7-digit street code
        return '%s%s%s' % \
            (self.boroughCode, self.streetCode, self.localGroupCode)


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
        names = [{'name': '%s %s %s' % (self.progenitor1.word,
                                        self.vsam.geographicFeatureName,
                                        self.progenitor1.b10sc.borough()),
                  'b10sc': self.progenitor1.b10sc}]
        if self.progenitor2:
            names.append({'name': '%s %s %s' % (self.progenitor2.word,
                                                self.vsam.geographicFeatureName,
                                                self.progenitor2.b10sc.borough()
                                                ),
                          'b10sc': self.progenitor2.b10sc})
        return names

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class NonSType:

    def __init__(self, rec):
        self.vsam = VSam(rec)
        dic = cowdef._type_non_s_keys

        self.primaryStreetNameIndicator = cowdef.extract(rec, dic,
                                                         'primaryStreetNameIndicator')
        self.principalLocalGroupNameIndicator = cowdef.extract(rec, dic,
                                                               'principalLocalGroupNameIndicator')
        self.filler1 = cowdef.extract(rec, dic, 'filler1')
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
        self.filler2 = cowdef.extract(rec, dic,'filler2')

        self.b10sc = B10sc(cowdef._type_non_s_b10sc, rec)

    def streets(self):
        return [{'name': self.vsam.geographicFeatureName,
                 'b10sc': self.b10sc}]

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
