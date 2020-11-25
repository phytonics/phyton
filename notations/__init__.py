# phyton.notations
from phyton.constants import *
import np

def _isnumeric(val):
    if type(val) in [np.generic, int, float, complex]: return True
    try: return bool(set(inspect(val)) & set([np.generic, int, float, complex]))
    except: return False


def A(*args, name=''):
    if len(args) == 1:
        if _isnumeric(args[0]): # Amplitude
            return Quantity(args[0], m, name)
        else: return args[0]
    if len(args) == 2: # Area
        if args[0].unit == m and args[1].unit == m: return Quantity((args[0]*args[1]).value, m**2, name)
        if args[0].unit == m**3 and args[1].unit == m: return Quantity((args[0]/args[1]).value, m**2, name)
        if args[0].unit == m and args[1].unit == m**3: return Quantity((args[1]/args[0]).value, m**2, name)

def a(*args, name=''):
    if len(args) == 1:
        if _isnumeric(args[0]):
            return Quantity(args[0], m/(s**2), name)
        else: return args[0]
    if len(args) == 2: # Area
        return Quantity(args[0]*args[1], m**2, name)
