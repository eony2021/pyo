from _core import *

class TrigRand(PyoObject):
    def __init__(self, input, min=0.05, max=0.05, mul=1, add=0):
        self._input = input
        self._min = min
        self._max = max
        self._mul = mul
        self._add = add
        self._in_fader = InputFader(input)
        in_fader, min, max, mul, add, lmax = convertArgsToLists(self._in_fader, min, max, mul, add)
        self._base_objs = [TrigRand_base(wrap(in_fader,i), wrap(min,i), wrap(max,i), wrap(mul,i), wrap(add,i)) for i in range(lmax)]

    def setInput(self, x, fadetime=0.05):
        self._input = x
        self._in_fader.setInput(x, fadetime)
        
    def setMin(self, x):
        self._min = x
        x, lmax = convertArgsToLists(x)
        [obj.setMin(wrap(x,i)) for i, obj in enumerate(self._base_objs)]

    def setMax(self, x):
        self._max = x
        x, lmax = convertArgsToLists(x)
        [obj.setMax(wrap(x,i)) for i, obj in enumerate(self._base_objs)]

    @property
    def input(self): return self._input
    @input.setter
    def input(self, x): self.setInput(x)
    @property
    def min(self): return self._min
    @min.setter
    def min(self, x): self.setMin(x)
    @property
    def max(self): return self._max
    @max.setter
    def max(self, x): self.setMax(x)

class TrigEnv(PyoObject):
    def __init__(self, input, table, dur=1, mul=1, add=0):
        self._input = input
        self._table = table
        self._dur = dur
        self._mul = mul
        self._add = add
        self._in_fader = InputFader(input)
        in_fader, table, dur, mul, add, lmax = convertArgsToLists(self._in_fader, table, dur, mul, add)
        self._base_objs = [TrigEnv_base(wrap(in_fader,i), wrap(table,i), wrap(dur,i), wrap(mul,i), wrap(add,i)) for i in range(lmax)]

    def setInput(self, x, fadetime=0.05):
        self._input = x
        self._in_fader.setInput(x, fadetime)

    def setTable(self, x):
        """Replace the `table` attribute.
        
        **Parameters**

        x : float or PyoObject
            new `table` attribute.
        
        """
        self._table = x
        x, lmax = convertArgsToLists(x)
        [obj.setTable(wrap(x,i)) for i, obj in enumerate(self._base_objs)]
        
    def setDur(self, x):
        self._dur = x
        x, lmax = convertArgsToLists(x)
        [obj.setDur(wrap(x,i)) for i, obj in enumerate(self._base_objs)]

    @property
    def input(self): return self._input
    @input.setter
    def input(self, x): self.setInput(x)
    @property
    def table(self): return self._table
    @table.setter
    def table(self, x): self.setTable(x)
    @property
    def dur(self): return self._dur
    @dur.setter
    def dur(self, x): self.setDur(x)