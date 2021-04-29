"""
self, other

self = (-2, -1, 3)
other = (1, 1, 1)

A = [
    0, -other.z, -other.y
    other.z, 0, other.x
    -other.y, other.x, 0
}

a, e, i = 0

other.z(other.x * other.y) - other.y(other.x * other.z) = 0  --> det will always be zero.

Therefore, this divCross does not work.
"""

# code:
import np
from numpy.linalg import det
from phyton.linalg import SpatialVector

def _divCross(self, other):
    """
    |u x v| = |u||v|sin(theta)
    """
    A = np.array([
        [0, -other.z, -other.y],
        [other.z, 0, other.x],
        [-other.y, other.x, 0]
    ])

    if not det(A):
        return SpatialVector()

    b = np.array(self.vec)

    return SpatialVector(*A.inv().dot(b))
