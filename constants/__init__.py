
# phyton.constants
from phyton.constants.quantity import *
from phyton.constants.unit import *
import math


# Math
pi = Quantity(math.pi, rad, "The PI Constant")
e = Quantity(math.e, Unit(), "Euler's Number")

δ = feigenbaum = Quantity(4.669201609102990671853203820466, (m/m), "First Feigenbaum Constant")
α_f = feigenbaum_alpha = Quantity(2.502907875095892822283902873218, (m/m), "Feigenbaum's Alpha Constant")


# Chem
NA = Quantity(6.02214076e23, 1/mol, "Avogadro's constant")
R = Quantity(8.314462618, J/(K*mol), "Molar gas constant")
M_u = Quantity(0.9999999996530e-3, kg/mol, "Molar mass constant")


# Gases
atm = Quantity(1.01325e5, Pa, "Atmospheric Pressure")
D_d = Quantity(1, (cm**2)/s, 'Diffusivity Coefficient')


# Speeds
c = Quantity(299792458, m/s, 'Speed of Light')
mach = Quantity(340.0, m/s, 'Speed of Sound')

# Gravitation and Cosmology
G = Quantity(6.6743015e-11, (N*m**2)/(kg**2), 'Universal Gravitational Constant')
g = Quantity(9.80665, m/(s**2), 'Average Gravitational Field Strength of the Earth')
kappa = κ = Quantity(2.071e-43, s**2/(m*kg), 'Einstein\'s Gravitational Constant (Scaled G)')
#kG = Quantity(, rad, 'Gaussian Gravitational Constant')


ME = Quantity(5.972e24, kg, "Mass of Earth")
MS = MSun = Quantity(1.989e30, kg, "Mass of Sun")
MVenus = Quantity(4.868e24, kg, "Mass of Venus")
MMoon = Quantity(7.347e22, kg, "Mass of Moon")
MMars = Quantity(6.417e23, kg, "Mass of Mars")
MJupiter = Quantity(1.898e27, kg, "Mass of Jupiter")
MSaturn = Quantity(5.683e26, kg, "Mass of Saturn")



RE = Quantity(6.371e6, m, "Mean Radius of Earth")
RS = RSun = Quantity(6.957e8, m, "Mean Radius of Sun")
RVenus = Quantity(6.052e6, m, "Mean Radius of Venus")
RMoon = Quantity(1.737e6, m, "Mean Radius of Moon")
RMars = Quantity(3.390e6, m, "Mean Radius of Mars")
RJupiter = Quantity(6.991e7, m, "Mean Radius of Jupiter")
RSaturn = Quantity(5.823e7, m, "Mean Radius of Saturn")




atm_Mercury = Quantity(0, Pa, "Atmospheric Pressure on Mercury")
atm_Moon = Quantity(0, Pa, "Atmospheric Pressure on Moon")
atm_Venus = Quantity(90*atm, Pa, "Atmospheric Pressure on Venus")
atm_Earth = Quantity(1.01325e5, Pa, "Atmospheric Pressure on Earth")




temp_Venus = T_Venus = Quantity(465, degC, "Temperature in Venus")



AU = Quantity(1.495978707e11, m, "Mean distance between Earth and Sun")


H0 = Quantity(2.25e-18, 1/s, "Hubble Constant")
Λ = cosmological = Quantity(9.182736455463728191001, 1/(m**2), "Einstein's Cosmological Constant")


# Atomics
m_u = u = Quantity(1.6605390666050e-27, kg, 'Atomic mass constant')
m_e = Quantity(9.109383701528e-31, kg, 'Rest mass of electron')
m_p = Quantity(1.6726219236951e-27, kg, 'Rest mass of proton')
m_n = Quantity(1.6749274980495e-27, kg, 'Rest mass of neutron')
m_α = 4.003*u
qe = Quantity(1.602176634e-19, C, 'Elementary Charge')
epsilon0 = ε0 = Quantity(8.854187812813e-12, (C**2)/(N*m**2), 'Electric constant, Vacuum Electric Permittivity')
mu0 = μ0 = Quantity(1.2566370621219e-6, T*m/A, 'Magnetic constant, Vacuum Magnetic Permeability')

p_m = Quantity(2.1765113e-8, kg, 'Planck mass')
p_t = Quantity(5.3910632e-44, s, 'Planck time')
p_l = Quantity(1.61619997e-35, m, 'Planck length')
p_temp = Quantity(1.41683385e32, K, 'Planck temperature')

R_inf = Quantity(10973731.56816021, 1/m, 'Rydberg constant')
E_H = Quantity(4.359744722207185e-18, J, "Hartree energy")
a0 = r_Bohr = Quantity(5.2917721090380e-11, m, 'Bohr radius')
re = Quantity(2.817940326213e-15, m, 'classical electron radius')
ge = Quantity(-2.0023193043625635, name='electron g-factor')
μB = Quantity(9.2740096820e-24, J/T, 'Bohr magneton')
μN = Quantity(5.050783746115e-27, J/T, 'nuclear magneton')
G_F = Quantity(1.1663787e-5, 1/(GeV**2), 'Fermi coupling constant')

# Fluids
ρ_w = Quantity(1000, kg/(m**3), "Density of water")
c_w = Quantity(4.19e3, J/(kg*K), "Specific Heat Capacity of water")
P_e = Quantity(10, Unit(''), 'Peclet Number')
μ = Quantity(1.2e-3, Pa*s, 'Viscosity of water')
c_f = Quantity(1e-9, 1/Pa, 'Compressibility of water')


# Solids
ρ_s = Quantity(2650, kg/(m**3), "Grain Density")

# Extra constants
h = Quantity(6.62607015e-34, J*s, 'Planck Constant')
ℏ = hbar = Quantity(1.05457172647e-34, J*s, 'Reduced/Angular Planck Constant')
stefan_boltzmann = σ = Quantity(5.670374419e-8, W/(m**2*K**4), "Stefan-Boltzmann constant")
boltzmann = kB = Quantity(1.3806504e-23, J/K, "Boltzmann constant")
k = Quantity(8.987551792314e9, (N*m**2)/(C**2), "Coloumb's constant")
b = Quantity(2.897771955e-3, m*K, "Wien wavelength displacement constant")
bprime = Quantity(5.878925757e10, Hz/K, "Wien frequency displacement constant")
Swien = Quantity(3.002916007, J/K, "Wien entropy in a DLC")
c1 = Quantity(3.741771852e-16, W*(m**2), "First radiation constant")
c2 = Quantity(1.438776877e-2, m*K, "Second radiation constant")



# Electromagnetic constants
Z0 = Quantity(376.73031366857, Ω, "Characteristic Impedance of vacuum")
Φ0 = Quantity(2.06783375846e-15, Wb, "Magnetic flux quantum")
K_J = Quantity(4.8359787011e14, Hz/V, 'Josephson constant')
R_K = Quantity(2.5812807443484e4, Ω, "von Klitzing constant")
G0 = Quantity(7.748091734625e-5, S, 'Conductance quantum')
α = Quantity(7.297352569311e-3, name='fine structure constant')
QoC = Quantity(3.6369475516e-4, m**2/s, 'quantum of circulation')
σe = σ_e = Quantity(6.652458732160e-29, m**2, 'Thomson cross section')
θw = θ_w = Quantity(0.2229030, rad, 'Weak mixing angle')
F = Quantity(96485.33212, C/mol, 'Faraday constant')


# Modulus
E = Quantity(5, GPa, 'Young Modulus')
Kmod = Quantity(3.33, GPa, 'Bulk Modulus')
Mmod = Quantity(4.73, GPa, 'Biot Modulus')


# Complex Constants
Δv_Cs = Quantity(9192631770, Hz, 'Hyperfine Transtition Frequency of Caesium Atom')
K_cd = Quantity(683, lm/W, 'Luminous Efficacy of Monochromatic Radiation of Frequency 540 THz')


# Fundamental Constants (Courtesy of Domain of Science)
p_m = Quantity(GeV(1.220896e19)/c**2, kg, "Planck Mass")
m_c = Quantity(GeV(1.27)/c**2, kg, "Mass of Charm Quark")
m_s = Quantity(MeV(101)/c**2, kg, "Mass of Strange Quark")
m_t = Quantity(GeV(172)/c**2, kg, "Mass of Top Quark")
m_b = Quantity(GeV(4.19)/c**2, kg, "Mass of Bottom Quark")
m_μ = m_mu = Quantity(MeV(105.658)/c**2, kg, "Mass of Muon")
m_τ = m_tau = Quantity(MeV(1776.82)/c**2, kg, "Mass of Tau")
α = alpha = fs = Quantity((e**2)/(hbar*c*4*pi*ε0), kg/kg, "Fine-structure constant")



def gfs(φ=Quantity(45, deg)):
    if type(φ) == Quantity: φ = φ.val * (180/math.pi if φ.unit == rad else 1)
    return Quantity(9.806 - 0.5*(9.832-9.780)*math.cos(2*φ*math.pi/180), m/(s**2), name=f"Gravitational Field Strength on Earth (at φ = {φ}°)")

def multiplier(n):
    return lambda multiple=1: multiple * n

def _cFunc(times, n = 1):
    return times * (c / n)

def _exp(x=1, n=None):
    euler = math.e if n is None else (1 + 1/n)**n
    return Quantity(euler ** x)

def _pi(d=1, iters=None):
    if iters is None:
        return pi*d;

    try:
        iters = int(iters)
    except:
        return pi * d;

    sign = 1
    x = 1
    y = 0
    series = 0
    for i in range (iters):
        series = series + (sign/(x * 3**y))
        x += 2
        y += 1
        sign *= -1

    myPi = math.sqrt(12) * series

    return Quantity(myPi, rad) * d


# Fill up
e.setfunc(_exp)
e.exp = _exp

pi.setfunc(_pi)
pi.my = _pi


g.addvalue(G*ME/(RE**2), 'GM/R^2').addvalue(9.764, 'Minimum g at the Earth Surface').addvalue(9.834, 'Maximum g at the Earth Surface').addvalue(9.81, 'School g Constant').addvalue(9.80, 'SJPO g Constant').addvalue(10, 'Secondary School g Constant')
g.addvalue(9.832, 'Gravitational Field Strength at poles').addvalue(9.806, 'Gravitational Field Strength at φ = 45°').addvalue(9.780, 'Gravitational Field Strength at equator')
g.setfunc(gfs)
g.gfs = gfs


k.addvalue(1/(4*pi*ε0), '1/4πε0').addvalue(9e9, 'AP Constant')

kB.addvalue(R/NA, "R/A")

κ.addvalue(8*pi*G/(c**4), "8πG/c^4")

ε0.addvalue(1/(4*pi*k), '1/4πk')
mu0.addvalue(pi * 4.0e-7, "4.0πe-7", T*m/A)

c.addvalue(3.0e8, "Approximated Speed of Light")
c.setfunc(_cFunc)

mach.addvalue(331, "Speed of Sound at 0℃").addvalue(343, "Speed of Sound at 20℃")
mach.setfunc(multiplier(mach))

qe.setfunc(multiplier(qe)) # Quantization of Charges
