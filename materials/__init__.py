from np import pi
import np

# [6]
mu0 = pi * 4.0e-7

class Material:
    μ = magnetic_permeability = 1.00000037 * mu0
    ε = electrical_conductivity = 0.0
    _dense = 1.292

    @staticmethod
    def density(T): return _dense * 273.15/T

    @staticmethod
    def magnetic_permeability(*args): return μ

    @staticmethod
    def electrical_conductivity(*args): return ε

class Air(Material):
    @staticmethod
    def shc(T):
        return 2.196e-13 * T**4 - 8.916e-10 * T**3 + 1.234e-06 * T**2 - 0.0004807 * T + 1.06

    @staticmethod
    def thermal_conductivity(T):
        return 1.5207e-11 * T**3 - 4.8574e-8 * T**2 + 1.0184e-4 * T - 0.00039333


class Argon(Material):
    μ = mu0
    _dense = 1.784
    specific_heat_capacity = 523.0
    λ = 0.0172

    @staticmethod
    def shc(*args):
        return specific_heat_capacity

    @staticmethod
    def thermal_conductivity(*args):
        return λ

class BoronTrioxide(Material):
    μ = mu0
    ε = 1.0 / 2.2e6
    mp = 723.0
    bp = 2133.0
    ρ = 1.5e3
    c = specific_heat_capacity = 1.802e3

    @staticmethod
    def density(*args): return ρ

    @staticmethod
    def shc(*args): return specific_heat_capacity

class CarbonSteel(Material):
    μ = 100*mu0
    ε = 1.180e6
    c = specific_heat_capacity = 0.466e3
    ρ = 7.85e3
    λ = 50.0

    @staticmethod
    def shc(*args): return specific_heat_capacity

    @staticmethod
    def thermal_conductivity(*args): return λ

    @staticmethod
    def density(*args): return ρ

class Copper(Material):
    μ = 0.999994*mu0
    #resistivity =

    @staticmethod
    def electrical_conductivity(T): return 1.0 / (-3.033e-9 + 68.85e-12*T - 6.72e-15*T**2 + 8.56e-18*T**3)

    @staticmethod
    def thermal_conductivity(T): return 420.75 - 6.8493e-2 * T

    @staticmethod
    def density(T):
        return 8.9975852012753705e3 * np.exp(-1.0e-6 * (+ 13.251 * T+ 6.903e-3 / 2.0 * T**2+ 8.5306e-7 / 3.0 * T**3))

    @staticmethod
    def shc(T): return 316.21 + 0.3177*T - 3.4936e-4*T**2 + 1.661e-7*T**3


class Graphite(Material):
    μ = 0.999984 * mu0
    mp = 3900.0
    @staticmethod
    def electrical_conductivity(T):
        return 1e6 / (28.9 - 18.8 * np.exp(-(np.log(T/1023.0)/2.37)**2))

    @staticmethod
    def thermal_conductivity(T): return 1.0 / (-9.797e-08*T**2 + 0.0007809*T - 0.05741)

    @staticmethod
    def density(T):
        return 2.267e3 / (1 + 30.0e-6*(T-298.0))

    @staticmethod
    def shc(T): return 4.184e3 * (+ 0.538657 + 9.11129e-6 * T - 90.2725 / T - 43449.3 / T**2 + 1.59309e7 / T**3 - 1.43688e9 / T**4)