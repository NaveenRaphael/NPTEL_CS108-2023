

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

x = np.linspace(0, 10, endpoint=True)
y = np.sin(x) + rand.normal(0, 0.01, size=len(x))

print(y)
