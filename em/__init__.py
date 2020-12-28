#phyton.em
from phyton.constants import *

## Electrostatics
class PointCharge:
    def __init__(self, multiple=1, name='', mass=kg(0)):
        self.Q = qe(multiple)
        self.name = ' '.join(['Point Charge', name]) if name else 'a Point Charge'
        self.mass = mass

    def FE(self, other, r):
        return Quantity((k*self.Q*other.Q/(r**2)).value, N, 'Electric Force of '+self.name+' and '+other.name)

    def E(self, r):
        return Quantity((k*self.Q/(r**2)).value, N/C, 'Electric Field of '+self.name)

    def UE(self, other, r):
        return Quantity((k*self.Q*other.Q/r).value, J, 'Electric Potential Energy of '+self.name+' and '+other.name)

    def V(self, r):
        return Quantity((k*self.Q/r).value, J/C, 'Electric Potential of '+self.name)

class Electron(PointCharge):
    def __init__(self):
        super().__init__(-1, 'Electron', m_e)

class Proton(PointCharge):
    def __init__(self):
        super().__init__(1, 'Proton', m_p)

class Neutron(PointCharge):
    def __init__(self):
        super().__init__(0, 'Neutron', m_n)

class Molecule(PointCharge):
    def __init__(self, p=0, n=0, e=0, name=''):
        super().__init__(p-e, name, m_p*p + m_n*n + m_e*e)


class Circuit:
    def __init__(self, *components, I=A(0)):
        self.components = list(components)
        self.I = I

    def add(self, component):
        self.components.append(component)
        component.parent = self
        return self


class Series:
    def __init__(self, *components, I=A(0)):
        self.components = list(components)

    @property
    def R(self):
        sum(c.R for c in self.components)

class Parallel:
    def __init__(self, *series):
        self.series = []
        for i in series:
            if type(i) != Series:
                self.series.append(Series(i))
            else: self.series.append(i)


class Component:
    Vdef = Pdef = Rdef = Idef = False
    def __init__(self, *args,parent=None):
        self.parent = parent
        for i in args:
            if i.unit == V and not self.Vdef:
                self.V, self.Vdef = i, True
            elif i.unit == W and not self.Pdef:
                self.P, self.Pdef = i, True
            elif i.unit == Ω and not self.Rdef:
                self.R, self.Rdef = i, True
            elif i.unit == A and not self.Idef:
                self.I, self.Idef = i, True

        if self.Vdef and self.Pdef:
            self.R = (self.V**2)/self.P
            self.I = self.P/self.V
        elif self.Idef and self.Pdef:
            self.R = self.P/(self.I ** 2)
            self.V = self.P/self.I
        elif self.Rdef and self.Pdef:
            self.I = (self.P/self.R)**0.5
            self.V = (self.P*self.R)**0.5
        elif self.Vdef and self.Idef:
            self.R = self.V/self.I
            self.P = self.V*self.I
        elif self.Vdef and self.Rdef:
            self.I = self.V/self.R
            self.P = (self.V**2)/self.R
        else:
            self.V = self.I*self.R
            self.P = (self.I**2)*self.R

    def time(self, t):
        return self.P*t

class Lamp(Component): pass

