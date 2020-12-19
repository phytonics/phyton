import np
from math import *
from inspect import getmro as inspect

def _check(obj, cls):
    return cls in inspect(type(obj))

def _mag(*args):
    return sqrt(sum([i**2 for i in args]))

class Scalar(complex):
    def mag(self):
        return _mag(self.real, self.imag)

def _convert(value):
    if type(value) == Scalar: return value
    else: return Scalar(value)


class SpatialVector:
    def __init__(self, x = 0, y = 0, z = 0):
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

    def dot(self, other):
        if _check(other, SpatialVector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else: return

    def cross(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        else: return

    @property
    def mag(self):
        return _mag(*self.vec)

    def __repr__(self):
        return f"SpatialVector({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(self.x + other.x, self.y + other.y, self.z + other.z)
        else: return

    def __radd__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(self.x + other.x, self.y + other.y, self.z + other.z)
        else: return

    def __sub__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(self.x - other.x, self.y - other.y, self.z - other.z)
        else: return

    def __rsub__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(other.x - self.x, other.y - self.y, other.z - self.z)
        else: return

    def __div__(self, other):
        if _check(other, SpatialVector):
            if self.x / other.x == self.y / other.y == self.z / other.z:
                return self.x / other.x
            
