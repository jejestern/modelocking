# -*- coding: utf-8 -*-
"""
The aim of this script is to plot the photodiode current of a GaP diode and Si diode of an incoming beam, which is either in continuous or in modelocking. We plot this against the power of the incoming laser beam.

@author: Jennifer

"""

import numpy as np
import matplotlib.pyplot as plt

R = 10000 #Ohm

#Daten in mV
Gap_con = np.array([1750, 1600, 1300, 1040, 740, 615, 275, 183, 26.5, 4.2, 0.57])
Si_con = np.array([6800, 6100, 5000, 3450, 2640, 2000, 1000, 620, 90, 11, 1.04])

Gap_ml = np.array([62.4, 63, 61, 54.95, 51.9, 47.25, 36.05, 27.20, 6.39, 1.38, 0.45])

# the OD steps
OD_Ga = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.0, 2.0, 3.0, 4.0])
OD_Si = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.0, 2.0, 3.0, 4.0]) + 3.0


plt.figure()
plt.semilogy(OD_Ga, Gap_con, 'ro', label='Measured data')
plt.xlabel('OD')
plt.ylabel(r'Photodiode voltage $V_{PD}$ [log(mV)]')
plt.legend()
plt.title('Measured photodiode voltage of a GaP diode, Continuous')
plt.savefig('Gap_con1.pdf')

plt.figure()
plt.semilogy(OD_Si, Si_con, 'ro', label='Measured data')
plt.xlabel('OD')
plt.ylabel(r'Photodiode voltage $V_{PD}$ [log(mV)]')
plt.legend()
plt.title('Measured photodiode voltage of a Si diode, Continuous')
plt.savefig('Si_con1.pdf')

plt.figure()
plt.semilogy(OD_Ga, Gap_ml, 'ro', label='Measured data')
plt.xlabel('OD')
plt.ylabel(r'Photodiode voltage $V_{PD}$ [log(mV)]')
plt.legend()
plt.title('Measured photodiode voltage of a GaP diode, Mode-locking')
plt.savefig('Gap_ml1.pdf')

 
### We also create the same plots with different axis and we create a fit for these plots
P_tot = 550
T_Ga = 10**(-OD_Ga)
T_Si = 10**(-OD_Si)

x_range_Ga = np.linspace(0, 600, 1000)
x_range_Si = np.linspace(0, 0.6, 1000)

#GaP continuous
P_Ga = T_Ga*P_tot
Curr_Gac = Gap_con/R

fit_Gac = np.poly1d(np.polyfit(P_Ga, Curr_Gac, 1))

plt.figure()
plt.plot(P_Ga, Curr_Gac, 'rx', label='Measured data') 
plt.plot(x_range_Ga, fit_Gac(x_range_Ga), 'k--', label='Fit')
plt.xlabel('Transmitted power P [mW]')
plt.ylabel(r'Photodiode current $i_{PD}$ [mA]')
plt.legend()
plt.title('Measured photodiode current of a GaP diode, Continuous')
plt.savefig('Gap_con.pdf')

#Si continuous
P_Si = T_Si*P_tot
Curr_Si = Si_con/R

fit_Si = np.poly1d(np.polyfit(P_Si, Curr_Si, 1))

plt.figure()
plt.plot(P_Si, Curr_Si, 'rx', label='Measured data') 
plt.plot(x_range_Si, fit_Si(x_range_Si), 'k--', label='Fit')
plt.xlabel('Transmitted power P [mW]')
plt.ylabel(r'Photodiode current $i_{PD}$ [mA]')
plt.legend()
plt.title('Measured photodiode current of a Si diode, Continuous')
plt.savefig('Si_con.pdf')

#GaP continuous
P_Ga = T_Ga*P_tot
Curr_Gaml = Gap_ml/R

fit_Gaml = np.poly1d(np.polyfit(P_Ga, Curr_Gaml, 2))

plt.figure()
plt.plot(P_Ga, Curr_Gaml, 'rx', label='Measured data') 
plt.plot(x_range_Ga, fit_Gaml(x_range_Ga), 'k--', label='Fit')
plt.xlabel('Transmitted power P [mW]')
plt.ylabel(r'Photodiode current $i_{PD}$ [mA]')
plt.legend()
plt.title('Measured photodiode current of a GaP diode, Modelocking')
plt.savefig('Gap_ml.pdf')
plt.show()
