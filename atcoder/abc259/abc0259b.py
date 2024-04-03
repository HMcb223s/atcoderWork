#!/usr/local/python
import numpy as np
a, b, d = map(int, input().split())

rad = np.deg2rad(d)

cos = np.cos(rad)
sin = np.sin(rad)

print(a * cos - b * sin, a * sin + b * cos)
