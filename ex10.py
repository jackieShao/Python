import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arrange(0.0, 2.0, 0.01)
y = (np.sin(x-2)**2) * (np.exp(-x**2))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Exercise 10')
plt.grid(True)
plt.show()
