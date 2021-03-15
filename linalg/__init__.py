import np
import math
from inspect import getmro as inspect

def check(obj, cls):
    return cls in inspect(type(obj))

def isnumeric(val):
    if type(val) in [np.generic, int, float, complex]: return True
    try: return bool(set(inspect(type(val))) & set([np.generic, int, float, complex]))
    except: return False

def _mag(*args):
    return sum([i**2 for i in args]) ** 0.5

def convert(value):
    if check(value, SpatialVector):
        if len(value) == 1: return Scalar(value.x)
        return value
    if type(value) == Scalar: return value
    elif isnumeric(value): return Scalar(value)



class Scalar(complex):
    @property
    def mag(self):
        return _mag(self.real, self.imag)

    def __str__(self):
        s = ""
        if self.real != 0 and self.imag != 0: s += "("
        if self.real != 0: s += f"{self.real}"
        if self.real != 0 and self.imag != 0: s += " + "
        if self.imag != 0: s += f"{self.imag}i"
        if self.real != 0 and self.imag != 0: s += ")"

        return s

    def _repr__(self):
        s = ""
        if self.real != 0 and self.imag != 0: s += "("
        if self.real != 0: s += f"{self.real}"
        if self.real != 0 and self.imag != 0: s += " + "
        if self.imag != 0: s += f"{self.imag}i"
        if self.real != 0 and self.imag != 0: s += ")"

        return s


Scalar.__repr__ = lambda self: int(self.real != 0 and self.imag != 0)*"(" + int(self.real != 0)*f"{self.real}" + int(self.real != 0 and self.imag != 0)*" + " + int(self.imag != 0)*f"{self.imag}i" + int(self.real != 0 and self.imag != 0)*")"
Scalar.__str__ = lambda self: int(self.real != 0 and self.imag != 0)*"(" + int(self.real != 0)*f"{self.real}" + int(self.real != 0 and self.imag != 0)*" + " + int(self.imag != 0)*f"{self.imag}i" + int(self.real != 0 and self.imag != 0)*")"


class SpatialVector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = convert(x)
        self.y = convert(y)
        self.z = convert(z)
        self.vec = (self.x, self.y, self.z)

    def dot(self, other):
        if check(other, SpatialVector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else: return self * other

    def cross(self, other):
        if check(other, SpatialVector):
            return SpatialVector(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        else: return self * other

    def angleFrom(self, other):
        if check(other, SpatialVector):
            return math.acos(self.dot(other) / (self.mag *  other.mag))

    @property
    def mag(self):
        return _mag(*self.vec)

    @property
    def unitVector(self):
        return self / self.mag

    @property
    def arg(self):
        return self.angleFrom(SpatialVector(1))

    def __len__(self):
        if self.z == 0 and self.y == 0: return 1
        if self.z == 0: return 2
        return 3

    def ndim(self):
        return len(self)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return int(not(self.y == 0 and self.z == 0))*"("+f"{self.x}"+int(not(self.y == 0 and self.z == 0))*f", {self.y}"+int(self.z != 0)*f", {self.z}"+int(not(self.y == 0 and self.z == 0))*")"


    def __add__(self, other):
        if check(other, SpatialVector):
            return SpatialVector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isnumeric(other):
            return SpatialVector(self.x + convert(other), self.y, self.z)
        else: return self

    def __radd__(self, other):
        if check(other, SpatialVector):
            return SpatialVector(self.x + other.x , self.y + other.y , self.z + other.z)
        elif isnumeric(other):
            return SpatialVector(self.x + convert(other), self.y, self.z)
        else: return self

    def __sub__(self, other):
        if check(other, SpatialVector):
            return SpatialVector(self.x - other.x , self.y - other.y , self.z - other.z)
        elif isnumeric(other):
            return SpatialVector(self.x - convert(other), self.y, self.z)
        else: return self

    def __rsub__(self, other):
        if check(other, SpatialVector):
            return SpatialVector(other.x - self.x , other.y - self.y , other.z - self.z)
        elif isnumeric(other):
            return SpatialVector(convert(other) - self.x, -self.y, -self.z)
        else: return self

    def __mul__(self, other):
        if isnumeric(other): return SpatialVector(convert(other)*self.x, convert(other)*self.y, convert(other)*self.z)
        elif check(other, SpatialVector): return self.dot(other)

    def __truediv__(self, other):
        if check(other, SpatialVector):
            if other.x != 0 and other.y != 0 and other.z != 0:
                if self.x / other.x == self.y / other.y == self.z / other.z: return self.x / other.x
                else: return SpatialVector(self.x / other.mag, self.y / other.mag, self.z / other.mag)

            else: return SpatialVector(self.x / other.mag, self.y / other.mag, self.z / other.mag)

        else:
            other = convert(other)
            return SpatialVector(self.x / other, self.y / other, self.z / other)

    def __eq__(self, other):
        if check(other, SpatialVector):
            return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self == other

    def __pos__(self):
        return self

    def __neg__(self):
        return SpatialVector(-self.x, -self.y, -self.z)

    def __round__(self, n):
        return SpatialVector(round(self.x, n), round(self.y, n), round(self.z,n))

    def __floor__(self):
        return SpatialVector(math.floor(self.x), math.floor(self.y), math.floor(self.z))

    def __ceil__(self):
        return SpatialVector(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z))

    def __trunc__(self):
        return SpatialVector(math.trunc(self.x), math.trunc(self.y), math.trunc(self.z))

    def __pow__(self, other):
        return SpatialVector(self.x * convert(other), self.y * convert(other), self.z * convert(other))

    def __getitem__(self, key):
        return self.vec.__getitem__(key)



class ArgandVector(SpatialVector):
    def __init__(self, real=0, imag=0):
        """if column:
            super().__init__(self, [[x], [y], [z]], dtype=float)
        else:
            super().__init__(self, [x, y, z], dtype=float)

        self.column = column
        self.row = not row """

        self.complex = complex(real, imag)
        self.real = convert(self.complex.real)
        self.imag = convert(self.complex.imag)

        super().__init__(self.real, self.imag)

        self.vec = (self.real, self.complex)

    @property
    def conjugate(self):
        return ArgandVector(self.real, -self.complex)

    @property
    def polarCoordinate(self):
        return ArgandVector(self.real, -self.complex)

    def dot(self, other):
        if check(other, SpatialVector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else: return self * other

    def cross(self, other):
        if check(other, SpatialVector):
            return SpatialVector(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        else: return self * other

    def angleFrom(self, other):
        if check(other, ArgandVector):
            return math.acos(self.dot(other) / (self.mag *  other.mag))
