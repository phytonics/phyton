# phyton.constants.quantity

from phyton.constants.unit import *
import math
from inspect import getmro as inspect
import np
from phyton.linalg import *
from collections.abc import Iterable

def angleBetween(self, other):
    if check(other, SpatialVector) and check(self, SpatialVector):
        return rad(math.acos(self.dot(other) / (self.mag *  other.mag)))

SpatialVector.angleFrom = angleBetween

class Quantity:
    def __init__(self, value, unit=Unit(), name='', uncertainty=0):
        if type(unit) == Quantity: unit = Unit(unit=unit.unit.unit, unitname=unit.unit.unitname, unitfunc=unit.unit.unitfunc, mul=unit.unit.mul*unit.value, add=unit.unit.add)
        elif type(unit) != Unit: unit = Unit(unit)

        if isinstance(value, Iterable):
            if all(isnumeric(i) for i in value):
                val = list(iter(value))
                value = SpatialVector(*val[:3])

        if type(value) == Quantity: value = value.value;

        if isnumeric(value): value = convert(value)

        self.value = convert(value)
        self.val = convert(self.value * unit.mul) + unit.add
        self.unit = unit
        self.name = str(name)
        self.vals = []
        self.func = None
        self.uncertain = convert(abs(uncertainty))
        self.uncertainty = convert(self.uncertain * unit.mul) + unit.add

    def __str__(self): return (str(self.val) + bool(self.unit)*f" {self.unit}").strip()
    def __repr__(self):
        s = bool(self.name)*f"{self.name} = " + str(self)
        for i in self.vals:
            s += '\n'+(f'%{len(self.name)}s' % i[-1])*bool(self.name) + ' = '+str(i[0])
            #s += '\n'+' '*(bool(self.name)*len(f"{self.name}")) + bool(self.name)*' = '+str(i)
        return s.strip()

    def __add__(self, other):
        if isnumeric(other):
            return Quantity(self.value+convert(other), self.unit, uncertainty=self.uncertain)
        if check(other, Quantity):
            if str(self.unit) == str(other.unit):
                return Quantity(self.val+other.val, Unit(str(self.unit)), uncertainty=self.uncertainty+other.uncertainty)

    def __radd__(self, other):
        if isnumeric(other):
            return Quantity(self.value+convert(other), self.unit, uncertainty=self.uncertain)
        if check(other, Quantity):
            if str(self.unit) == str(other.unit):
                return Quantity(self.val+other.val, Unit(str(self.unit)), uncertainty=self.uncertainty+other.uncertainty)

    def __sub__(self, other):
        if isnumeric(other):
            return Quantity(self.value-convert(other), self.unit, uncertainty=self.uncertain)
        if check(other, Quantity):
            if str(self.unit) == str(other.unit):
                return Quantity(self.val-other.val, Unit(str(self.unit)), uncertainty=self.uncertainty+other.uncertainty)

    def __rsub__(self, other):
        if isnumeric(other):
            return Quantity(convert(other)-self.value, self.unit, uncertainty=self.uncertain)
        if check(other, Quantity):
            if str(self.unit) == str(other.unit):
                return Quantity(other.val-self.val, Unit(str(self.unit)), uncertainty=self.uncertainty+other.uncertainty)

    def __mul__(self, other):
        if isnumeric(other):
            return Quantity(self.value*convert(other), self.unit)
        if check(other, Quantity):
            return Quantity(self.value*other.value, self.unit*other.unit, self.value*other.uncertain+self.uncertain*other.value)

    def __rmul__(self, other):
        if isnumeric(other):
            return Quantity(self.value*convert(other), self.unit)
        if check(other, Quantity):
            return Quantity(self.value*other.value, self.unit*other.unit, self.value*other.uncertain+self.uncertain*other.value)

    def __truediv__(self, other):
        if isnumeric(other):
            return Quantity(self.value/convert(other), self.unit)
        if check(other, Quantity):
            return Quantity(self.value/other.value, self.unit/other.unit, self.value*other.uncertain+self.uncertain*other.value)

    def __rtruediv__(self, other):
        if isnumeric(other):
            return Quantity(convert(other)/self.value, 1/self.unit)
        if check(other, Quantity):
            return Quantity(other.value/self.value, other.unit/self.unit, self.value*other.uncertain+self.uncertain*other.value)

    def __pow__(self, other):
        if isnumeric(other): return Quantity(self.value**convert(other), self.unit**other, other * self.uncertain * self.value**(other-1))

    def addvalue(self, val, name='', unit=None):
        if unit is None: unit = self.unit
        if isnumeric(val):
            val = Quantity(convert(val), unit)
        elif check(val, SpatialVector):
            val = Quantity(convert(val), unit)
        elif check(val, Quantity):
            val = Quantity(val.val, unit)

        self.vals.append((val, name))
        return self

    def setfunc(self, func):
        self.func = func

    @property
    def mag(self):
        return self.unit(self.value.mag)

    @property
    def arg(self):
        return rad(self.value.arg)

    def __call__(self, *args, **kwargs):
        if self.func: return self.func(*args, **kwargs)
        else:
            mul = self
            for i in args:
                if isnumeric(i) or check(i, Quantity) or check(i, SpatialVector):
                    mul = mul * i

            return mul

    def __neg__(self):
        return self.unit(-self.value)

    def __pos__(self):
        return self.unit(self.value)
