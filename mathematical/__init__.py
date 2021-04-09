# phyton.mathematical
from sympy import Symbol, symbols

def _divide(a, b):
  '''Returns the decimal representation of the fraction a / b in three parts:
  integer part, non-recurring fractional part, and recurring part.'''
  assert b != 0
  integer = a // b
  remainder = a % b
  seen = {remainder: 0}  # Holds position where each remainder was first seen.
  digits = []
  while(True):  # Loop executed at most b times (as remainders must be distinct)
    remainder *= 10
    digits.append(remainder // b)
    remainder = remainder % b
    if remainder in seen:  # Digits have begun to recur
      where = seen[remainder]
      return (integer, digits[:where], digits[where:])
    else:
      seen[remainder] = len(digits)

def round_div(a, b, round=1):
   (i, f, r) = _divide(a, b)
   return eval("%d.%s%s" % (i, ''.join(list(map(str, f))),''.join(list(map(str,r)))))

class Quadratic:
    def __init__(self, *args, type='examples'):
        if type.replace(' ', '').replace(',', '') == 'examples':
            self.examples = {}
            h_found = False
            for x, y in args:
                if x in self.examples:
                    self.examples[y].append(x)
                    if not h_found:
                        self.h = sum(self.examples[y])/2
                        h_found = not h_found
                
                else: self.examples[y] = [x]

            a, h = symbols('a h')
            # iter(self.examples)[0] =
            # y = a(x-h)**2 + k
            self.examples[y][0]

            
            

        elif type.replace(' ', '').replace(',', '') == 'abc':
            self.a, self.b, self.c = args[0], args[1], args[2]
            self.discriminant = self.b**2 - 4*self.a*self.c
            self.h, self.k = -self.b/(2*self.a), -self.discriminant/(4*self.a*self.c)
            if self.

        elif type.replace(' ', '').replace(',', '') == 'ahk':
            self.a, self.h, self.k = args[0], args[1], args[2]
            self.b, self.c = -2*self.a*self.h, self.a*self.h**2 + self.k

        elif type.replace(' ', '').replace(',', '') == 'aroots':
            self.a, self.alpha, self.beta = args[0], args[1], args[2]
            self.b, self.c = self.a * (-self.alpha - self.beta), self.a * (self.alpha * self.beta)
            self.h = (self.alpha + self.beta) / 2
