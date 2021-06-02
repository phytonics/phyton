# phyton
<p align="center">
  <img src="phyton.png" width="720" alt="phyton">
</p>
A physics library based on Python.


## A Dynamics Physics Library
```python
>>> from phyton import *
>>> distance = m[5]
>>> displacement = m[5, 5, 5]
>>> displacement
(5.0, 5.0, 5.0) m
>>> distance
5.0 m
>>> displacement.mag
8.660254037844387 m
>>> print(displacement.unit)
m
>>> print(area.unit)
m^2
>>> length = m[5]
>>> width = m[3]
>>> area = length * width
>>> area
15.0 m^2
```

```py
>>> from phyton.constants import *
>>> v = (m/s)[10, 10]
>>> v.mag
(14.142135623730951+0j) m/s
>>> t = ms(100)
>>> d = v * t
>>> d
(1.0, 1.0) m
>>> B = T(10)
>>> r = m(0.5)
>>> A = pi * r**2
>>> A
0j = (0.7853981633974483+0j) m^2
>>> flux = B * A
>>> flux
0j = (7.853981633974483+0j) Wb
>>> exp3 = e(3)
>>> exp3
(20.085536923187664+0j)
>>> mach
Speed of Sound = (340+0j) m/s
Speed of Sound at 0℃ = (331+0j) m/s
Speed of Sound at 20℃ = (343+0j) m/s
>>> mach2 = mach(2)
>>> mach2
(680+0j) m/s
>>> g
Average Gravitational Field Strength of the Earth = (9.80665+0j) m/s^2
                                           GM/R^2 = (9.81997563319173+0j) m/s^2
                   Minimum g at the Earth Surface = (9.764+0j) m/s^2
                   Maximum g at the Earth Surface = (9.834+0j) m/s^2
                                School g Constant = (9.81+0j) m/s^2
                                  SJPO g Constant = (9.8+0j) m/s^2
                      Secondary School g Constant = (10+0j) m/s^2
            Gravitational Field Strength at poles = (9.832+0j) m/s^2
          Gravitational Field Strength at φ = 45° = (9.806+0j) m/s^2
          Gravitational Field Strength at equator = (9.78+0j) m/s^2
>>> g(10)
Gravitational Field Strength on Earth (at φ = 10°) = (9.781567991859564+0j) m/s^2
```
