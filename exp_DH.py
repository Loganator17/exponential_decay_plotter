import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import matplotlib.axes as axes
import datetime
import scipy as scipy
from scipy import optimize

from scipy.optimize import curve_fit
from matplotlib.ticker import FormatStrFormatter

# dT = dh / (gamma * alpha * h)

# h: thickness of lava flow (m)
# dT: temperature change (K)
# gamma: 1.7 (contraction coefficient for Poisson ratio - 0.25 (-)
# alpha: thermal expansivity (1/K), 
#        use values between 8.3e-6 to 3e-6 (Hekla lava to Hawaii basalt), 
#        the latter may be more appropriate.

fname = "/InSAR/Bardarbunga/time_series_analysis/path09/SBAS/TSD_flattened6.txt"
cero = np.genfromtxt(fname, names="Date, orbit, point1, point2, point3, point4, point5, zorbit", dtype=None)
z_orb = cero["zorbit"]


#        -16.679473877   64.8623477221   0  15.474
#        -16.6933241189  64.8700596094   1  23.3546
#        -16.7331955731  64.8851835728   2  26.657
#        -16.7734464705  64.8979182243   3  23.457
#        -16.7877210081  64.9057420492   4  8.434

#1 0.13076046838479194 -0.003000758253598645 -0.14071758653123795
#2 0.44428864460887296 -0.0017612391010967854 -0.4539747884202855
#3 0.5415786048385329 -0.002032052789405266 -0.6333440380830205
#4 0.2625693845647385 -0.0016403344662608346 -0.2743621841206463
#5 0.05382819347229119 -0.0010318574269728633 -0.045564474858142974


#dh = a*np.exp(x*k) + b

a=0.13076046838479194
k=-0.001800758253598645
b=-0.14071758653123795
h=15.474
gamma=1.7
alpha=8.3e-6

for x in z_orb:
     dh = a*np.exp(x*k) + b
     dT = dh / (gamma * alpha * h)
     print(dT)


#EOF
