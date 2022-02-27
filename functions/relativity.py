# relativity.py
from phyton.constants import c

def beta(v):
	"""
	Beta is a impt variable, defined basically as v / c

	:param v: Velocity of Current object

	"""
	return v / c

def gamma(v):
	return 1 / (1-beta(v)**2)**0.5

def dilate(v, dt):
	return gamma(v)*dt

def contract(v, l):
	return l / gamma(v)

def meff(m0, v):
	return m0 * gamma(v)

def restE(m0):
	return m0 * c ** 2

def totalE(v, m0):
	return restE(meff(m0, v))

def p(v, m0):
	return beta(v) * totalE(v, m0) / c


def betaFromContraction(factor):
        (1/factor**2)
