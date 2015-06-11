import json
import cowdef


class B10sc:

    def __init__(self, lAttributes, rec):
        cowdef.process(self, lAttributes, rec)

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
            cowdef.process(self, _p, rec)
            self.b10sc = B10sc(_b, rec)
        else:
            raise Exception('Unknown Progenitor number')


class VSam:

    def __init__(self, rec):
        cowdef.process(self, cowdef._vsam_keys, rec)

    def __str__(self):
        keys = sorted(self.__dict__.keys())
        return '\n'.join(['%s: %s' % (k, self.__dict__[k]) for k in keys])

    def borough(self):
        return cowdef.boroughMap[self.boroughCode]


class SType:

    def __init__(self, rec):
        self.vsam = VSam(rec)
        cowdef.process(self, cowdef._type_s_keys, rec)
        self.progenitor1 = Progenitor(1, rec)
        self.progenitor2 = None
        if self.progenitorCount == '2':
            self.progenitor2 = Progenitor(2, rec)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class NonSType:

    def __init__(self, rec):
        self.vsam = VSam(rec)
        cowdef.process(self, cowdef._type_non_s_keys, rec)
        self.b10sc = B10sc(cowdef._type_non_s_b10sc, rec)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

rec = "11   1 STREET                                    NS161E 11701001010   " \
      "                                                                      " \
      "                                                            \r\n"
stype = SType(rec)
print 'stype.to_JSON() = %s\n\n\n' % stype.to_JSON()

rec = "11   1 AVENUE                     PF11001001010  N 11   1 AVENUE      " \
      "                                                                      " \
      "                                                            \r\n"
nstype = NonSType(rec)
print 'nonSType.to_JSON() = %s' % nstype.to_JSON()
