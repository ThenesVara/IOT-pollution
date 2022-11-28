# https://courspython.com/introduction-courbes.html
import numpy as np
import matplotlib.pyplot as plt

#x = np.linspace(0, 1, 10)
x = [1,2,3,4,5,6,7,8,9,10] #temps
y1 = [5,7,8,2,6,8,10,8,5,1] #capteur1
y2 = [1,5,7,8,2,6,8,10,8,5] #capteur2

plt.xlabel("temps")
plt.ylabel("Capteur")

plt.plot(x, y1, "r--", label="capteur1")
plt.plot(x, y2, "b:o", label="capteur2")
plt.legend()

plt.show()