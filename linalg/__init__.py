import np
from math import *
from inspect import getmro as inspect
from numpy.linalg import *
from phyton.constants import Quantity as Scalar
from phyton.constants import Unit

def _check(obj, cls):
    return cls in inspect(type(obj))

def _mag(*args):
    return sum([i**2 for i in args]) ** 0.5

def _convert(value, unit=Unit()):
    if type(value) == Scalar: return Scalar(value, unit)
    else: return Scalar(value, unit)


def _divCross(other, self):
    """
    |u x v| = |u||v|sin(theta)
    """
    A = np.array([
        [0, -self.z, -self.y],
        [self.z, 0, self.x],
        [-self.y, self.x, 0]
    ])

    if not det(A):
        return

    b = np.array(other.vec)

    return SpatialVector(*A.inv().dot(b))


class SpatialVector:
    def __init__(self, x = 0, y = 0, z = 0, unit=Unit()):
        """if column:
            super().__init__(self, [[x], [y], [z]], dtype=float)
        else:
            super().__init__(self, [x, y, z], dtype=float)

        self.column = column
        self.row = not row """

        self.x = _convert(x)
        self.y = _convert(y)
        self.z = _convert(z)
        self.vec = (self.x, self.y, self.z)
        self.unit = unit

    def dot(self, other):
        if _check(other, SpatialVector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else: return

    def cross(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(
                self.y.value * other.z.value - self.z.value * other.y.value,
                self.z.value * other.x.value - self.x.value * other.z.value,
                self.x.value * other.y.value - self.y.value * other.x.value
            )
        else: return

    def angleFrom(self, other):
        if _check(other, SpatialVector):
            return acos(self.dot(other) / (self.mag *  other.mag))

    @property
    def mag(self):
        return _mag(*self.vec)

    def __repr__(self):
        return f"SpatialVector({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(self.x.value + other.x.value, self.y.value + other.y.value, self.z.value + other.z.value)
        else: return

    def __radd__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(self.x.value + other.x.value, self.y.value + other.y.value, self.z.value + other.z.value)
        else: return

    def __sub__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(self.x.value - other.x.value, self.y.value - other.y.value, self.z.value - other.z.value)
        else: return

    def __rsub__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(other.x.value - self.x.value, other.y.value - self.y.value, other.z.value - self.z.value)
        else: return

    def __truediv__(self, other):
        if _check(other, SpatialVector):
            if other.x.value != 0 and other.y.value != 0 and other.z.value != 0:
                if self.x.value / other.x.value == self.y.value / other.y.value == self.z.value / other.z.value:return self.x / other.x
            else:
                return _divCross(self, other)


        other = _convert(other)
        return SpatialVector(self.x / other, self.y / other, self.z / other)

    def __rtruediv__(self, other):
        if _check(other, SpatialVector):
            if self.x.value != 0 and self.y.value != 0 and self.z.value != 0:
                if other.x / self.x == other.y / self.y == other.z / self.z:
                    return other.x / self.x
            return _divCross(other, self)

        return
    
    def __eq__(self, other):
        if _check(other, SpatialVector):
            return self.x.value == other.x.value and self.y.value == other.y.value and self.z.value == other.z.value and self.unit == other.unit
        
    def __ne__(self, other):
        return not self == other
    