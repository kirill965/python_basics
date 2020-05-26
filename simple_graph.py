#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as ppl

sin_a_list = np.sin(np.radians(np.arange(0,360,0.1)))
angles = np.arange(0,360,0.1)

ppl.plot(angles, sin_a_list)
ppl.show()
