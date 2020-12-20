# phyton.constants.quantity

from phyton.constants.unit import *
from math import *

def _isnumeric(val):
    if type(val) in [np.generic, int, float, complex]: return True
    try: return bool(set(inspect(val)) & set([np.generic, int, float, complex]))
    except: return False

class Quantity:
    def __init__(self, value, unit=Unit(), name=''):
        if type(unit) == Quantity: unit = Unit(unit=unit.unit.unit, unitname=unit.unit.unitname, unitfunc=unit.unit.unitfunc, mul=unit.unit.mul*unit.value, add=unit.unit.add)
        elif type(unit) != Unit: unit = Unit(unit)

        if type(value) == Quantity: value = value.value;

        self.val, self.value = (float(value) * unit.mul) + unit.add, value
        self.unit = unit
        self.name = str(name)
        self.vals = []
        self.func = None

    def __str__(self): return (f"{self.val}" + bool(self.unit)*f" {self.unit}").strip()
    def __repr__(self):
        s = bool(self.name)*f"{self.name} = " + str(self)
        for i in self.vals:
            s += '\n'+(f'%{len(self.name)}s' % i[-1])*bool(self.name) + f' = {i[0]}'
            #s += '\n'+' '*(bool(self.name)*len(f"{self.name}")) + bool(self.name)*' = '+str(i)
        return s.strip()

    def __add__(self, other):
        if _isnumeric(other):
            return Quantity(self.value+float(other), self.unit)
        if type(other) == Quantity:
            return Quantity(self.value+other.value, self.unit + other.unit)

    def __radd__(self, other):
        if _isnumeric(other):
            return Quantity(self.value+float(other), self.unit)
        if type(other) == Quantity:
            return Quantity(self.value+other.value, self.unit + other.unit)

    def __sub__(self, other):
        if _isnumeric(other):
            return Quantity(self.value-float(other), self.unit)
        if type(other) == Quantity:
            return Quantity(self.value-other.value, self.unit - other.unit)

    def __rsub__(self, other):
        if _isnumeric(other):
            return Quantity(float(other)-self.value, self.unit)
        if type(other) == Quantity:
            return Quantity(other.value-self.value, other.unit-self.unit)

    def __mul__(self, other):
        if _isnumeric(other):
            return Quantity(self.value*float(other), self.unit)
        if type(other) == Quantity:
            return Quantity(self.value*other.value, self.unit*other.unit)

    def __rmul__(self, other):
        if _isnumeric(other):
            return Quantity(self.value*float(other), self.unit)
        if type(other) == Quantity:
            return Quantity(self.value*other.value, self.unit*other.unit)

    def __truediv__(self, other):
        if _isnumeric(other):
            return Quantity(self.value/float(other), self.unit)
        if type(other) == Quantity:
            return Quantity(self.value/other.value, self.unit/other.unit)

    def __rtruediv__(self, other):
        if _isnumeric(other):
            return Quantity(float(other)/self.value, 1/self.unit)
        if type(other) == Quantity:
            return Quantity(other.value/self.value, other.unit/self.unit)

    def __pow__(self, other):
        return Quantity(self.value**float(other), self.unit**other)

    def addvalue(self, val, name=''):
        if _isnumeric(val):
            val = Quantity(val, self.unit)
        self.vals.append((val, name))
        return self

    def setfunc(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if self.func: return self.func(*args, **kwargs)
