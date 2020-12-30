import np
from math import *
from inspect import getmro as inspect
from numpy.linalg import *

def _check(obj, cls):
    return cls in inspect(type(obj))

def _mag(*args):
    return sum([i**2 for i in args]) ** 0.5

def _convert(value):
    if type(value) == Scalar: return value
    else: return Scalar(value)


def _divCross(self, other):
    """
    |u x v| = |u||v|sin(theta)
    """
    A = np.array([
        [0, -other.z, -other.y],
        [other.z, 0, other.x],
        [-other.y, other.x, 0]
    ])

    if not det(A):
        return SpatialVector()

    b = np.array(self.vec)

    return SpatialVector(*A.inv().dot(b))

class Scalar(float): pass
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

    def angleFrom(self, other):
        if _check(other, SpatialVector):
            return acos(self.dot(other) / (self.mag *  other.mag))

    @property
    def mag(self):
        return _mag(*self.vec)

    @property
    def unitVector(self):
        return self / self.mag

    def __repr__(self):
        return f"SpatialVector({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(self.x + other.x, self.y + other.y, self.z + other.z)
        else: return

    def __radd__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(self.x + other.x , self.y + other.y , self.z + other.z)
        else: return

    def __sub__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(self.x - other.x , self.y - other.y , self.z - other.z)
        else: return

    def __rsub__(self, other):
        if _check(other, SpatialVector):
            return SpatialVector(other.x - self.x , other.y - self.y , other.z - self.z)
        else: return

    def __truediv__(self, other):
        if _check(other, SpatialVector):
            if other.x != 0 and other.y != 0 and other.z != 0:
                if self.x / other.x == self.y / other.y == self.z / other.z: return self.x / other.x
                else: return _divCross(self, other) #doesn't work, see Proof.
            else:
                return _divCross(self, other)

        else:
            other = _convert(other)
            return SpatialVector(self.x / other, self.y / other, self.z / other)

    """
    def __rtruediv__(self, other):
        if _check(other, SpatialVector):
            if self.x != 0 and self.y != 0 and self.z != 0:
                if other.x / self.x == other.y / self.y == other.z / self.z:
                    return other.x / self.x
            return _divCross(other, self)

        return 0
    """

    def __eq__(self, other):
        if _check(other, SpatialVector):
            return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self == other

    def __float__(self):
        return self
