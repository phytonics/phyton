# phyton.vectors
from math import *
from inspect import getmro as inspect
from sympy import Symbol
from phyton.constants import *


π = Symbol('π')

class VectorError(Exception): pass

class Vector:
    def __init__(self, *args):
        self.vec = []
        true = True
        for i in args[::-1]:
            if true and i == 0: continue
            true = False
            self.vec.append(i)

        self.vec = self.vec[::-1]

        if len(args) >= 1: self.x = args[0]
        else: self.x = 0
        if len(args) >= 2: self.y = args[1]
        else: self.y = 0
        if len(args) >= 3: self.z = args[2]
        else: self.z = 0

    def __getitem__(self, index):
        if type(index) == int: return self.vec[index]
        if type(index) == str: return eval('self.'+str)
        raise VectorError('Not a possible index')



class SpatialVector(Vector):
    def __init__(self, x, y=0, z=0):
        self.ndim = 3
        if SpatialVector in inspect(type(x)): super().__init__(self, x.x, x.y, x.z)
        else: super().__init__(x, y, z)


    @property
    def magnitude(self):
        return sqrt(self.x**2+self.y**2+self.z**2)

    @property
    def angle(self):
        if self.y == 0 and self.z == 0: return 0
        if self.x == 0 and self.z == 0: return π/2 * (self.y/abs(self.y))
        if self.x == 0 and self.y == 0: return π/2 * (self.z/abs(self.z))
        if self.x == 0: return π/(pi/atan(self.z/self.y))
        if self.y == 0: return π/(pi/atan(self.z/self.x))
        if self.z == 0: return π/(pi/atan(self.y/self.x)) 
        return π/(pi/sqrt(atan(self.y/self.x)**2 + atan(self.z/self.x)**2))

    @property
    def normalised(self):
        if not self.magnitude: raise VectorError('The magnitude of this vector is zero.')
        return SpatialVector(self.x/self.magnitude, self.y/self.magnitude, self.z/self.magnitude)

    def normalise(self):
        if not self.magnitude: raise VectorError('The magnitude of this vector is zero.')
        self.x /= self.magnitude
        self.y /= self.magnitude
        self.z /= self.magnitude
        return self

    @property
    def copy(self):
        self.__class__(self.x, self.y, self.z)

    @property
    def tuple(self):
        return (self.x, self.y, self.z)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other): return not (self == other)

    def __bool__(self): return self.magnitude != 0

    def __add__(self, vec): return self.__class__(self.x+vec.x, self.y+vec.y, self.z+vec.z)
    def __iadd__(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z
        return self

    def __sub__(self, vec): return self.__class__(self.x-vec.x, self.y-vec.y, self.z-vec.z)
    def __isub__(self, vec):
        self.x -= vec.x
        self.y -= vec.y
        self.z -= vec.z
        return self

    def distance(self, vec): return sqrt((self.x-vec.x)**2 + (self.y-vec.y)**2 + (self.z-vec.z)**2)
    def anglebw(self, vec): return acos(self.dot(vec)/(self.magnitude*vec.magnitude))
    def dot(self, vec): return self.x*vec.x + self.y*vec.y + self.z*vec.z
    def cross(self, vec): return self.__class__(self.y*vec.z-self.z*vec.y, self.z*vec.x-self.x*vec.z, self.x*vec.y-self.y*vec.x)
    def product(self, vec): return self.cross(self)
    def __mul__(self, other):
        if len(set(inspect(type(other))).union({int, float})): return self.__class__(self.x*other, self.y*other, self.z*other)
        if SpatialVector in inspect(type(other)): return self.cross(other)
        raise VectorError("Unsupported Value Type")

    def __rmul__(self, other):
        if len(set(inspect(type(other))).union({int, float})): return self.__class__(self.x*other, self.y*other, self.z*other)
        if SpatialVector in inspect(type(other)): return other.cross(self)
        raise VectorError("Unsupported Value Type")

    def __imul__(self, other):
        if len(set(inspect(type(other))).union({int, float})):
            self.x *= other
            self.y *= other
            self.z *= other
        elif SpatialVector in inspect(type(other)):
            self.x, self.y, self.z = self.y*vec.z-self.z*vec.y, self.z*vec.x-self.x*vec.z, self.x*vec.y-self.y*vec.x
        else: raise VectorError("Unsupported Value Type")

    def __truediv__(self, other):
        if len(set(inspect(type(other))).union({int, float})): return self.__class__(self.x/other, self.y/other, self.z/other)
        raise VectorError("Unsupported Value Type")

    def __rdiv__(self, other):
        raise VectorError("Vectors cannot simply divide anything")

    def __idiv__(self, other):
        if len(set(inspect(type(other))).union({int, float})):
            self.x /= other
            self.y /= other
            self.z /= other
        else: raise VectorError("Unsupported Value Type")

    def __iter__(self): return iter(self.x, self,y, self.z)

    def __neg__(self): return self.__class__(-self.x, -self.y, -self.z)
    def __pos__(self): return self.copy

    __radd__ = __add__

    @staticmethod
    def zero():
        return self.__class__(0)


i = SpatialVector(1)
j = SpatialVector(0, 1)
k = SpatialVector(0, 0, 1)
zero = SpatialVector(0)

def mult(a,b):
    if type(a) in [int, float] and SpatialVector in inspect(type(b)): return SpatialVector(b.x*a, b.y*a, b.z*a)
    if type(b) in [int, float] and SpatialVector in inspect(type(a)): return SpatialVector(a.x*b, a.y*b, a.z*b)
    if SpatialVector in inspect(type(a)): return self.cross(other)
    raise VectorError("Unsupported Value Type")


class BaseVectorClass(SpatialVector):
    unit = ''
    def __init__(self, x, y=0, z=0):
        super().__init__(x, y, z)
    def __add__(self, vec): return type(self)(self.x+vec.x, self.y+vec.y, self.z+vec.z)
    def __sub__(self, vec): return type(self)(self.x-vec.x, self.y-vec.y, self.z-vec.z)
    def distance(self, vec): return sqrt((self.x-vec.x)**2 + (self.y-vec.y)**2 + (self.z-vec.z)**2)
    def anglebw(self, vec): return acos(self.dot(vec)/(self.magnitude*vec.magnitude))
    def dot(self, vec): return self.x*vec.x + self.y*vec.y + self.z*vec.z
    def cross(self, vec): return self * vec
    def product(self, vec): return self * vec
    def __str__(self): return f"{self.magnitude} {self.unit} {self.angle} radians above the positive x-axis"
    def __repr__(self): return str(self)

class BaseScalarClass:
    unit = ''
    def __init__(self, value):
        self.value = float(value)
    def __str__(self): return f"{self.value} {self.unit}"
    def __repr__(self): return str(self)
    def __float__(self): return self.value



class Time(BaseScalarClass): unit = s
class Mass(BaseScalarClass):
    unit = kg
    def __mul__(self, other):
        if type(other) is Acceleration:
            print(other.x, other.y, other.z)
            return Force(self.value*other.x, self.value*other.y, self.value*other.z)
class Inertia(BaseScalarClass):
    unit = kg * m * m
    def __init__(self, β, mass, radius):
        super().__init__(β * float(mass) * radius.magnitude)

class Energy(BaseScalarClass): unit = J

class Power(BaseScalarClass):
    unit = W
    def __mul__(self, other):
        if type(other) == Time: return Energy(float(self)*float(other))
        if type(other) in [int, float]: return self.__class__(other*float(self))
        return float(self) * float(other)

class SpecificEnergy(BaseScalarClass):
    unit = J/kg # m^2/s^2
    def __mul__(self, other):
        if type(other) == Mass: return Energy(float(self)*float(other))
        if type(other) in [int, float]: return self.__class__(other*float(self))
        return float(self) * float(other)

class Displacement(BaseVectorClass):
    unit = m

    def __mul__(self, other):
        if type(other) in [int, float]: return Displacement(self.x*other, self.y*other, self.z*other)
        cross = (self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
        if type(other) == Displacement: return Area(*cross)
        if type(other) == Force: return Energy(self.x*other.x + self.y*other.y + self.z*other.z)
        raise VectorError("Unsupported Value Type")

    def __truediv__(self, other):
        if type(other) in [int, float]: return Displacement(self.x/other, self.y/other, self.z/other)
        if type(other) in Time: return Velocity(self.x/other, self.y/other, self.z/other)

    def __pow__(self, other):
        if other == 2: return Area(self.y*self.z-self.z*self.y, self.z*self.x-self.x*self.z, self.x*self.y-self.y*self.x)
        if other == 3:
            other = Area(self.y*self.z-self.z*self.y, self.z*self.x-self.x*self.z, self.x*self.y-self.y*self.x)
            return Volume(self.x*other.x + self.y*other.y + self.z*other.z)

class Radius(Displacement): pass

class Area(BaseVectorClass):
    unit = m**2

class Volume(BaseScalarClass):
    unit = m**3

class Velocity(BaseVectorClass):
    unit = m/s

    def __mul__(self, other):
        if type(other) == Time: return Displacement(self.x*float(other), self.y*float(other), self.z*float(other))
        if type(other) == Mass: return Momentum(self.x*float(other), self.y*float(other), self.z*float(other))
        #cross = (self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
        if type(other) == Momentum: return Energy(self.x*other.x + self.y*other.y + self.z*other.z)
        if type(other) == Velocity: return SpecificEnergy(self.x*other.x + self.y*other.y + self.z*other.z)
        if type(other) == Force: return Power(self.x*other.x + self.y*other.y + self.z*other.z)

class Acceleration(BaseVectorClass):
    unit = m/(s**2)

    def __mul__(self, other):
        if type(other) == Time: return Velocity(self.x*float(other), self.y*float(other), self.z*float(other))
        if type(other) == Mass:
            return Force(self.x*float(other), self.y*float(other), self.z*float(other))
        #dot = self.x*other.x + self.y*other.y + self.z*other.z
        #cross = (self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)

    def __rmul__(self, other):
        if type(other) == Time: return Velocity(self.x*other, self.y*other, self.z*other)
        if type(other) == Mass: return Force(self.x*float(other), self.y*float(other), self.z*float(other))
        if type(other) in [int, float]: return Acceleration(self.x*other, self.y*other, self.z*other)
        #dot = self.x*other.x + self.y*other.y + self.z*other.z
        #cross = (self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)


class Momentum(BaseVectorClass):
    unit = kg*m/s
    def __mul__(self, other):
        #cross = (self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
        if type(other) == Radius: return AngularMomentum(self.x*other.x + self.y*other.y + self.z*other.z)
        if type(other) == Velocity: return Energy(self.x*other.x + self.y*other.y + self.z*other.z)

    def __truediv__(self, other):
        if type(other) == Velocity: return Mass(self.magnitude/other.magnitude)
        if type(other) == Mass: return Velocity(self.x/float(other), self.y/float(other), self.z/float(other))
        if type(other) == Time: return Force(self.x/float(other), self.y/float(other), self.z/float(other))

class Impulse(Momentum): unit = N*s


class Force(BaseVectorClass):
    unit = N
    def __mul__(self, other):
        if type(other) == Radius: return Torque(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
        if type(other) == Displacement: return Energy(self.x*other.x + self.y*other.y + self.z*other.z)
        if type(other) == Velocity: return Power(self.x*other.x + self.y*other.y + self.z*other.z)
        if type(other) == Time: return Impulse(self.x*other, self.y*other, self.z*other)

    def __truediv__(self, other):
        if type(other) == Mass: return Acceleration(self.x/float(other), self.y/float(other), self.z/float(other))



class Torque(BaseVectorClass):
    unit = N*m
    def __mul__(self, other):
        if type(other) == AngularDisplacement: return Energy(self.x*other.x + self.y*other.y + self.z*other.z)
        if type(other) == AngularVelocity: return Power(self.x*other.x + self.y*other.y + self.z*other.z)
        if type(other) == Time: return AngularImpulse(self.x*other, self.y*other, self.z*other)

    def __div__(self, other):
        if type(other) == Inertia: return AngularAcceleration(self.x/float(other), self.y/float(other), self.z/float(other))



class AngularDisplacement(BaseVectorClass):
    unit = 'rad'
    def __mul__(self, other):
        if type(other) == Torque: return Energy(self.x*other.x + self.y*other.y + self.z*other.z)
        if type(other) == Radius: return Displacement(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)



class AngularVelocity(BaseVectorClass):
    unit = 'rad/s'
    def __mul__(self, other):
        if type(other) == Inertia: return AngularMomentum(self.x*other, self.y*other, self.z*other)
        if type(other) == Radius: return Velocity(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)


class AngularAcceleration(BaseVectorClass):
    unit = 'rad/s^2'
    def __mul__(self, other):
        if type(other) == Inertia: return Torque(self.x*float(other), self.y*float(other), self.z*float(other))
        if type(other) == Radius: return Acceleration(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)


class AngularMomentum(BaseVectorClass):  unit = kg*m**2/s
class AngularImpulse(AngularMomentum): unit = N*m*s

g = Acceleration(0, -9.81)
