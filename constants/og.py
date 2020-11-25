class Unit:
    def __init__(self, name, unitname=''):
        self.si = self.SIit(name)
        if '/' in self.si: [self.numer, self.denom] = self.si.split('/')
        else: self.numer, self.denom = self.si, ''
        self.basename = name
        self.realname = unitname

    def __repr__(self): return f"{self.realname}, {self.si}"
    def __str__(self): return self.realname if self.realname else self.si

    def SIit(self, string):
        if string in ['Nm']: return string
        count = string.count('^')
        # base units : m, s, kg, cd, mol, A, K
        for i in range(count):
            ind = string.index('^')
            if string[ind-1] in 'smNJWCΩVFSTHAK':
                unit, start = string[ind-1], ind-1
            elif string[ind-2: ind] in 'HzPaWbkgcd':
                unit, start = string[ind-2:ind], ind-2
            else:
                unit, start = 'mol', ind-3
            end = ind+1
            while string[end+1].isnumeric():
                if end >= len(string): break
                end += 1
            power = eval(string[ind+1:end]) if string[ind+1:end] else 1
            string = string[:start] + power*unit + string[end:]
        si = self.distribute(string)
        #if si == '1/s': return 'Hz'
        #if si == 'kgm/s^2': return 'N'
        #if si == 'kg/ms^2': return 'Pa'
        #if si == 'kgm^2/s^2': return 'J'
        #if si == 'kgm^2/s^3': return 'W'
        #if si == 'sA': return 'C'
        #if si == 'kgm^2/s^3A': return 'V'
        #if si == 's^4A^2/kgm^2': return 'F'
        #if si == 'kgm^2/s^3A^2': return 'Ω'
        #if si == 's^3A^2/kgm^2': return 'S'
        #if si == 'kg/s^2A': return 'T'
        #if si == 'kgm^2/s^2A': return 'Wb'
        #if si == 'kgm^2/s^2A^2': return 'H'
        return si
        

    def distribute(self, string):
        # string = string.replace('N', 'kgm/s^2')
        # string = string.replace('J', 'kgm^2/s^2')
        # string = string.replace('Pa', 'kg/ms^2')
        if '/' in string:
            [numer, denom] = string.split('/')

        else: numer, denom = string,''
        Tnum = Wbnum = Hnum = Snum = Ωnum = Cnum = Vnum = Fnum = cdnum = molnum = Anum = kgnum = mnum = snum = Knum = Nnum = Jnum = Hznum = Wnum = Panum = 0


        Cnum += numer.count('C') - denom.count('C')
        self.C = Cnum
        Anum += Cnum
        snum += Cnum

        Vnum += numer.count('V') - denom.count('V')
        self.V = Vnum
        kgnum += Vnum
        mnum += Vnum*2
        Anum -= Vnum
        snum -= 3*Vnum

        Fnum += numer.count('F') - denom.count('F')
        self.F = Fnum
        kgnum -= Fnum
        mnum -= Fnum*2
        Anum += 2*Fnum
        snum += 4*Fnum

        Ωnum += numer.count('Ω') - denom.count('Ω')
        self.Ω = Ωnum
        kgnum += Ωnum
        mnum += Ωnum*2
        Anum -= 2*Ωnum
        snum -= 3*Ωnum

        Snum -= numer.count('S') - denom.count('S')
        self.S = Snum
        kgnum += Snum
        mnum += Snum*2
        Anum -= 2*Snum
        snum -= 3*Snum

        Tnum += numer.count('T') - denom.count('T')
        self.T = Tnum
        kgnum += Tnum
        Anum -= Tnum
        snum -= 2*Tnum

        Wbnum -= numer.count('Wb') - denom.count('Wb')
        self.Wb = Wbnum
        mnum += Wbnum*2
        kgnum += Wbnum
        Anum -= Wbnum
        snum -= 2*Wbnum

        Hnum -= numer.count('H') - denom.count('H')
        self.H = Hnum
        mnum += Hnum*2
        kgnum += Hnum
        Anum -= 2*Hnum
        snum -= 2*Hnum
        
        Nnum += numer.count('N') - denom.count('N')
        self.N = Nnum
        kgnum += Nnum
        mnum += Nnum
        snum -= 2*Nnum

        Jnum += numer.count('J') - denom.count('J')
        self.J = Jnum
        kgnum += Jnum
        mnum += 2*Jnum
        snum -= 2*Jnum

        Hznum += numer.count('Hz') - denom.count('Hz')
        self.Hz = Hznum
        snum -= Hznum

        Knum += numer.count('K') - denom.count('K')

        Panum += numer.count('Pa') - denom.count('Pa')
        self.Pa = Panum
        kgnum += Panum
        mnum -= Panum
        snum -= 2*Panum

        Wnum += numer.count('W') - denom.count('W')
        self.W = Wnum
        kgnum += Wnum
        mnum += 2*Wnum
        snum -= 3*Wnum

        snum += numer.count('s') - denom.count('s')
        molnum += numer.count('mol') - denom.count('mol')
        numer = numer.replace('mol', '')
        denom = denom.replace('mol', '')
        mnum += numer.count('m') - denom.count('m')
        kgnum += numer.count('kg') - denom.count('kg')
        Knum += numer.count('K') - denom.count('K')
        Anum += numer.count('A') - denom.count('A')
        molnum += numer.count('mol') - denom.count('mol')
        cdnum += numer.count('cd') - denom.count('cd')

        finalnumer = finaldenom = ''
        #base units : m, s, kg, cd, mol, A, K
        self.m = mnum
        self.s = snum
        self.kg = kgnum
        self.cd = cdnum
        self.mol = molnum
        self.A = Anum
        self.K = Knum
        
        if kgnum < -1: finaldenom += f'kg^{-kgnum}'
        elif kgnum == -1: finaldenom += 'kg'
        elif kgnum == 1: finalnumer += 'kg'
        elif kgnum > 1: finalnumer += f'kg^{kgnum}'
        
        if molnum < -1: finaldenom += f'mol^{-molnum}'
        elif molnum == -1: finaldenom += 'mol'
        elif molnum == 1: finalnumer += 'mol'
        elif molnum > 1: finalnumer += f'mol^{molnum}'
        
        if mnum < -1: finaldenom += f'm^{-mnum}'
        elif mnum == -1: finaldenom += 'm'
        elif mnum == 1: finalnumer += 'm'
        elif mnum > 1: finalnumer += f'm^{mnum}'
        
        if snum < -1: finaldenom += f's^{-snum}'
        elif snum == -1: finaldenom += 's'
        elif snum == 1: finalnumer += 's'
        elif snum > 1: finalnumer += f's^{snum}'

        if Knum < -1: finaldenom += f'K^{-Knum}'
        elif Knum == -1: finaldenom += 'K'
        elif Knum == 1: finalnumer += 'K'
        elif Knum > 1: finalnumer += f'K^{Knum}'

        if cdnum < -1: finaldenom += f'cd^{-cdnum}'
        elif cdnum == -1: finaldenom += 'cd'
        elif cdnum == 1: finalnumer += 'cd'
        elif cdnum > 1: finalnumer += f'cd^{cdnum}'

        if Anum < -1: finaldenom += f'A^{-Anum}'
        elif Anum == -1: finaldenom += 'A'
        elif Anum == 1: finalnumer += 'A'
        elif Anum > 1: finalnumer += f'A^{Anum}'
        
        if denom == numer == '': return ''
        if denom == '': return numer
        if numer == '': return f'1/{denom}'
        return f'{numer}/{denom}'

    def __truediv__(self, other):
        return Unit(self.numer+other.denom+'/'+self.denom+other.numer)

    def __mul__(self, other):
        return Unit(self.numer+other.numer+'/'+self.denom+other.denom)

    def __imul__(self, other):
        self = self * other

    def __rtruediv__(self, other):
        if other == 1:
            return Unit(self.denom+'/'+self.numer)

        return other / self

    def __pow__(self, other):
        value = Unit(self.si)
        for i in range(other-1):
            value = value * Unit(self.si)
        return value


class Quantity(float):
    def __new__(cls, value, unit, name=''):
        return float.__new__(cls, value)
    
    def __init__(self, value, unit='', name=''):
        self.value = value
        self.unit = unit
        self.name = name

    def __repr__(self): return str(self)

    def __str__(self):
        if self.name == '' and self.unit == '':
            return str(self.value)
        if self.name == '':
            return f"{self.value} {self.unit}"
        if self.unit == '':
            return f"{self.name}  =  {self.value}"
        return f"{self.name}  =  {self.value} {self.unit}"

    def __add__(self, other):
        if type(other) in [float, int]:
            return Quantity(self.value+other, self.unit)
        if other.unit == self.unit:
            return Quantity(self.value+other.value, self.unit)
        return Quantity(self.value+other.value)

    def __mul__(self, other):
        if type(other) in [float, int]:
            return Quantity(self.value*other, self.unit)
        return Quantity(self.value*other.value, self.unit*other.unit)

    def __div__(self, other):
        if type(other) in [float, int]:
            return Quantity(self.value/other, self.unit)
        return Quantity(self.value/other.value, self.unit/other.unit)

    def __rdiv__(self, other):
        if type(other) in [float, int]:
            return Quantity(other/self.value, 1/self.unit)
        return Quantity(other.value/self.value, other.unit/self.unit)
# units
m = Unit('m', 'metre')
s = Unit('s', 'second')
kg = Unit('kg', 'kilogram')
cd = Unit('cd', 'candela')
mol = Unit('mol', 'mole')
A = Unit('A', 'ampere')
K = Unit('K', 'kelvin')
Hz = Unit('1/s', 'hertz')
N = Unit('N', 'newton')
Pa = Unit('Pa', 'pascal')
J = Unit('J', 'joule')
W = Unit('J/s', 'watt')
C = Unit('As', 'coulomb')
V = Unit('J/As', 'volt')
F = Unit('A^2s^2/J', 'farad')
Ω = Unit('Ω', 'ohm')
S = Unit('S', 'siemens')
T = Unit('T', 'tesla')
Wb = Unit('Wb', 'weber')
H = Unit('H', 'henry')
L = Unit('L')
Gy = Unit('J/kg', 'gray')
Sv = Unit('J/kg', 'sievert')
kat = Unit('mol/s', 'katal')
