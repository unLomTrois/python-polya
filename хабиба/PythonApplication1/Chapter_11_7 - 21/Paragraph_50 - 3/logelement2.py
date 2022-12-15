# -*- coding: cp1251 -*-

from abc import ABCMeta, abstractmethod

class TLogElement(metaclass=ABCMeta):
    def __init__(self):
        self.__in1 = False
        self.__in2 = False
        self._res = False
        self.__nextEl = None
        self.__nextIn = 0
        pass
    def __setIn1(self, in1):
        self.__in1 = in1
        self.calc()
        if self.__nextEl: 
            if self.__nextIn == 1: 
                self.__nextEl.In1 = self._res 
            elif self.__nextIn == 2: 
                 self.__nextEl.In2 = self._res 
    def __setIn2(self, in2):
        self.__in2 = in2
        self.calc()
    def link(self, nextEl, nextIn):
        self.__nextEl = nextEl
        self.__nextIn = nextIn

    @abstractmethod
    def calc(self):
        pass

    In1 = property(lambda x: x.__in1, __setIn1)
    In2 = property(lambda x: x.__in2, __setIn2)
    Res = property(lambda x: x._res)
    
    pass

class TNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def calc(self):
        self._res = not self.In1

class TLog2In(TLogElement):
    pass

class TAnd(TLog2In):
    def __init__(self):
        TLog2In.__init__(self)
    def calc(self):
        self._res = self.In1 and self.In2

class TOr(TLog2In):
    def __init__(self):
        TLog2In.__init__(self)
    def calc(self):
        self._res = self.In1 or self.In2

class TXor(TLog2In):
    def __init__(self):
        TLog2In.__init__(self)
    def calc(self):
        self._res = self.In1 == (not self.In2)

class TNotAnd(TLog2In):
    def __init__(self):
        TLog2In.__init__(self)
    def calc(self):
        self._res = not (self.In1 and self.In2)

class TNotOr(TLog2In):
    def __init__(self):
        TLog2In.__init__(self)
    def calc(self):
        self._res = not (self.In1 or self.In2)