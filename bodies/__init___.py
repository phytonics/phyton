from phyton.constants import *
from phyton.vectors import *

class Location:
    def __init__(self, M=ME, h=RE, μ=0):
        self.M = Mass(M.value)
        self.h = Displacement(0, h.value)
        print(self.M, self.h)
        self.μ = 0

    @property
    def g(self):
        return Acceleration(0, -(G*float(self.M))/(self.h.magnitude**2))

    @property
    def potential(self):
        return -(G*self.M)/self.h

class SoftBody:
    def __init__(self, mass, location, force=0, velocity=Velocity(0)):
        self.loc = location
        self.v = velocity
        self.Fnet = force
        self.m = mass

    @property
    def KE(self):
        return 0.5 * self.p * self.v

    @property
    def GPE(self):
        return self.loc.potential * self.m

    @property
    def p(self):
        return self.m*self.v

    @property
    def a(self):
        return (self.Fnet/m)

    def apply(self, force):
        self.Fnet += force
        return self

    def friction(self, magnitude = None):
        if self.v == 0 and self.Fnet.magnitude < magnitude:
            self.Fnet = 0
            return self
        if magnitude is None:
            magnitude = self.loc.μ * self.m * self.loc.g
            
        self.apply(-magnitude)
        return self

    def timepass(self, t):
        vi = self.v
        self.v = vi + self.a * t
        self.loc.h += vi*t + 0.5*self.a*t*t

class RigidBody:
    betas = {
        'sphere': 2/5,
        'hollow sphere': 2/3,
        'cylinder': 0.5,
        'disc': 0.5,
        'disk': 0.5,
        'hoop': 1
    }
    def __init__(self, location, mass, radius, beta=1, forces=[], pivotdist=Displacement(0), angularvel=AngularVelocity(0), velocity=Velocity(0)):
        self.loc = location
        self.v_com = velocity
        self.omega = angularvel
        self.forces = forces
        self.Fnet = sum([i[0] for i in forces])
        self.τnet = sum([i[0]*i[1] for i in forces])
        self.pivot = pivotdist
        self.m = mass
        self.radius = radius

    @property
    def I(self):
        return Inertia(self.beta, self.mass, self.radius) + Inertia(1, self.mass, self.pivot)

    @property
    def α(self):
        return self.τnet/self.I

    @property
    def L(self):
        return self.I * self.angularvel

    @property
    def p(self):
        return self.L/self.radius

    @property
    def v(self):
        return self.v_com + self.angularvel*(self.radius-self.pivot)

    @property
    def KE(self):
        return 0.5*self.p*self.v

Earth = Location()
m = Mass(68.0)
Prannaya = SoftBody(m, Earth, m*Earth.g)
print('vi = ', Prannaya.v)
print('hi = ', Earth.h)
print('a = ', Prannaya.a)
Prannaya.timepass(Time(3))
print(Prannaya.v, Earth.h, sep='\n')
