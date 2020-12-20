import np
from math import *
from inspect import getmro as inspect
from numpy.linalg import *
from phyton.constants import Quantity, Unit

def _check(obj, cls):
    return cls in inspect(type(obj))

def _mag(*args):
    return sqrt(sum([i**2 for i in args]))

class Scalar(Quantity): pass

def _convert(value, unit=Unit()):
    if type(value) == Scalar: return Scalar(value, unit)
    else: return Scalar(value, unit)


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
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        else: return

    def angleBetween(self, other):
        if _check(other, SpatialVector):
            return acos(self.dot(other) / (self.mag *  other.mag))

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
            else:
                """
                |u x v| = |u||v|sin(theta)
                """
                A = np.array([
                    [0, -other.z, -other.y],
                    [other.z, 0, other.x],
                    [-other.y, other.x, 0]
                ])

                if not det(A):
                    return

                b = np.array(self.vec)

                return SpatialVector(*A.inv().dot(b))


        other = _convert(other)
        return SpatialVector(self.x / other, self.y / other, self.z / other)

    def __rdiv__(self, other):
        if _check(other, SpatialVector):
            if other.x / self.x == other.y / self.y == other.z / self.z:
                return other.x / self.x
            else:
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


        other = _convert(other)
        return SpatialVector(self.x / other, self.y / other, self.z / other)
