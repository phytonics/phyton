# phyton.astro


class _SolarSystemObject(object):
    m = 'unknown'
    R = 'unknown'
    type = 'unknown'


class Sun(_SolarSystemObject):
    m = 1.989e30
    R = 6.957e8
    type = 'star'

class Planet(_SolarSystemObject):
    semi_major_axis = 'unknown'
    sidereal_rotation_period = 
