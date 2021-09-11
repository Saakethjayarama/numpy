# sin, cos, tan

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10*np.pi, 0.1)
y = np.sin(x)
# y = np.cos(x)
# y = np.tan(x)
# y = 1/np.sin(x)
# y = 1/np.cos(x)
# y = 1/np.tan(x)
plt.plot(x, y)
plt.show()
