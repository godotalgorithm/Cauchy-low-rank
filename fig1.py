import numpy as np
import matplotlib.pyplot as plt
import Zolotarev

n = 200
x = 1e-9
roots = Zolotarev.Z_roots(n, x)
extrema = Zolotarev.Z_extrema(n, x)
m = 30
y = [ (1-j/m)*extrema[i] + (j/m)*extrema[i+1] for i in range(n) for j in range(m)]
y.append(1)
func = [Zolotarev.Z_func(z, roots) for z in y]

plt.figure(figsize=(7,4))
plt.semilogx(y, func, color='black', lw=0.5)
plt.semilogx(y, [np.sqrt(Zolotarev.Z(roots))]*len(y), color='red', lw=0.5)
plt.semilogx(y, [-np.sqrt(Zolotarev.Z(roots))]*len(y), color='red', lw=0.5)
plt.savefig("fig1.pdf",bbox_inches='tight',pad_inches=0.01)

