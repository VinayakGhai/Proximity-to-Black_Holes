import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

x = np.linspace(0, 10, 500)
y = np.zeros_like(x)
O = 2
inside_bh = x >= O

plt.figure(figsize=(10,5))
plt.plot(x, y, color='cyan', linewidth=2, label='Photon Path')
plt.fill_between(x[inside_bh], y[inside_bh]-0.1, y[inside_bh]+0.1, color='purple', alpha=0.4, label='BH Interior')
plt.scatter([0,O,10],[0,0,0], color='yellow', s=80)
plt.text(0,0.1,'A',color='yellow',fontsize=12)
plt.text(O,0.1,'O (BH Entry)',color='yellow',fontsize=12)
plt.text(10,0.1,'B',color='yellow',fontsize=12)

plt.xlabel('Distance [arbitrary units]')
plt.ylabel('Transverse displacement')
plt.title('Photon Transit Near a Black Hole')
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("../figures/photon_bh_trajectory.png", dpi=300)
plt.show()
