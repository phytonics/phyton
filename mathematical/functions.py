from collections.abc import Iterable



class Range:
    def __init__(self, min=-float('inf'), max=float('inf'), real=True, integer=False, minInclusive=False, maxInclusive=False):
        this.min = min; this.max = max; this.real = real; this.integer = integer; this.minInclusive = minInclusive; this.maxInclusive = maxInclusive;
        this.aboveMin = lambda x: x >= min if minInclusive else x > min;
        this.belowMax = lambda x: x <= max if maxInclusive else x < max;

    def __contains__(self, other):
        if isinstance(other, Range): return self.__contains__(other.min) and self.__contains__(other.max)
        if isinstance(other, Iterable):
            for i in other:
                if not self.__contains__(i): return False
            return True
        if isInstance(other, complex) and self.real: return True;
        if isInstance(other, int) and self.integer: return False;
        return self.aboveMin(other) and self.belowMax(other)

    def __repr__(self):
        return "Range"+str(self)

    def __str__(self):
        return ("[" if self.minInclusive else "(")+str(self.min)+", "+str(self.max)+("]" if self.maxInclusive else ")")


Z = Range(integer=True)
Zplus = Range(min=0, integer=True)
Zminus = Range(max=0, integer=False)

R = Range()
Rplus = Range(min=0)
Rminus = Range(max=0)
