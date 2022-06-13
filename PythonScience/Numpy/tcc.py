import numpy as np
import matplotlib.pyplot as plt
dados_base = np.loadtxt('base.CSV').reshape((-1,7))

x = dados_base[:,0]
y = dados_base[:,1]
plt.plot(x,y)
plt.xlabel('Tempo (s)')
plt.ylabel('Concentração (kg/m^3)')
plt.show()