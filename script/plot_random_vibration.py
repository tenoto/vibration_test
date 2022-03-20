#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

df_spacex = pd.read_excel('data/Random Vibration Enviroment.xlsx',
	sheet_name='SpaceX',engine='openpyxl',skiprows=[0,1,3])
print(df_spacex)

df_cygnus = pd.read_excel('data/Random Vibration Enviroment.xlsx',
	sheet_name='Cygnus',engine='openpyxl',skiprows=[0,1,3])
print(df_cygnus)

df_slingshot = pd.read_excel('data/Random Vibration Enviroment.xlsx',
	sheet_name='SlingShot',engine='openpyxl',skiprows=[0,1,3])
print(df_slingshot)

plt.style.use('script/default.mplstyle')

fig = plt.figure(figsize=(12,9))
fig.patch.set_alpha(0.0)
ax1 = fig.add_subplot(111)
#ax2 = ax1.twiny()

ax1.minorticks_on()
ax1.grid(True)
ax1.grid(axis='both',which='major', linestyle='--', color='#000000')
ax1.grid(axis='both',which='minor', linestyle='--')	
ax1.tick_params(axis="both", which='major', direction='in', length=5)
ax1.tick_params(axis="both", which='minor', direction='in', length=3)

ax1.plot(df_spacex['Frequency'],df_spacex['MPE PSD'],'r-',
	linewidth=2,label='SpaceX')
ax1.plot(df_cygnus['Frequency'],df_cygnus['PSD'],'b-',
	linewidth=2,label='Cygnus')
ax1.plot(df_slingshot['Frequency'],df_slingshot['MPE PSD'],'k-',
	linewidth=2,label='SlingShot')

ax1.set_xlim(20,2000)
#ax1.set_ylim(1e-4,1e+6)
ax1.set_xlabel("Frequency (Hz)",labelpad=14)
ax1.set_ylabel('PSD (g^2/Hz)',labelpad=14)
#ax2.set_xlabel('Stellar Radius (km)',labelpad=14)
ax1.legend()
plt.setp([ax1], xscale="log", yscale="log")
plt.tight_layout()
#ax1.patch.set_alpha(0.0)  
#ax2.patch.set_alpha(0.0)  
fig.savefig("out/random_vibraiton.pdf")