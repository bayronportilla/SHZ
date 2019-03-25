#Para determinar condiciones iniciales adecuadas.

import numpy as np
import matplotlib.pyplot as plt

RS=6.957000e8
Year=365.25*86400
Myr=Year*1.0e6 
Day=86400.0
InDeg=180.0/np.pi
AU=149.6e9



############################################################
# Data from simulations
data_file_1="/Users/bportilla/SecDev3B_V2.0/ejemplo_3.dat"
info_file_1="/Users/bportilla/SecDev3B_V2.0/ejemplo_3.log"
data_1=np.loadtxt(data_file_1)
info_1=np.genfromtxt(info_file_1,dtype=None)

uT=float(info_1[34][2])
uL=float(info_1[33][2])

time_1     = data_1[:,0]
a_in_1     = data_1[:,1:2]
a_out_1    = data_1[:,2:3]
e_in_1     = data_1[:,3:4]
e_out_1    = data_1[:,4:5]
I_in_1     = data_1[:,5:6]
I_out_1    = data_1[:,6:7]
W_in_1     = data_1[:,7:8]
W_out_1    = data_1[:,8:9]
w_in_1     = data_1[:,9:10]
w_out_1    = data_1[:,10:11]
Om_Ax_in_1 = data_1[:,11:12]
Om_Ay_in_1 = data_1[:,12:13]
Om_Az_in_1 = data_1[:,13:14]
Om_Bx_in_1 = data_1[:,14:15]
Om_By_in_1 = data_1[:,15:16]
Om_Bz_in_1 = data_1[:,16:17]
R_A_1      = data_1[:,19:20]
R_B_1      = data_1[:,20:21]



# axes rect in relative 0,1 coords left, bottom, width, height.  Turn
# off xtick labels on all but the lower plot

############################################################
# Fancy style
plt.rc('font', **{'family': 'family', 'family': ['serif']})
plt.rc('text', usetex=True) #uses Latex instead of Tex to compile axes labels

fig,((ax_1),(ax_2),(ax_3),(ax_4)) = plt.subplots(4, 1,figsize=(8,10),sharex=True)
plt.subplots_adjust(hspace=0.0)

############################################################
# Plot on each axes

ax_1.plot(time_1*uT/Myr, a_in_1*uL/AU)
ax_2.plot(time_1*uT/Myr, e_in_1*uL/AU)
ax_3.plot(time_1*uT/Myr, (I_in_1)*InDeg)
ax_4.plot(time_1*uT/Myr, (I_out_1)*InDeg)
#ax_3.plot(time_1*uT/Myr, e_in_1)
#ax_4.plot(time_2*uT/Myr, e_in_2)

############################################################
# vertical line
#ax_1.vlines(41.9,-0.1,2.7,color='grey')


############################################################
# Limits
"""
ax_1.set_xlim(0,76.2)
ax_2.set_xlim(0,76.2)
"""
#ax_1.set_ylim(-0.1,2.7)
ax_2.set_ylim(0.0,0.9)
ax_3.set_ylim(0.0,90.0)
ax_4.set_ylim(0.0,90.0)

############################################################
# Add Text 
#ax_1.text(43,1.6,'$t_{a,\mathrm{half}} = 41.9$ Myr',fontsize=22)
#ax_1.text(43,1.6,'$t_{a,1/2} = 41.9$ Myr',fontsize=22)


############################################################
# ticks params
tamanolabel=20
ax_1.tick_params(direction='in',labelsize=tamanolabel,axis='both')
ax_2.tick_params(direction='in',labelsize=tamanolabel,axis='both')
ax_3.tick_params(direction='in',labelsize=tamanolabel,axis='both')
ax_4.tick_params(direction='in',labelsize=tamanolabel,axis='both')


############################################################
# labels
labels=23

ax_1.set_ylabel("$a_1$ (AU)",fontsize=labels)
ax_4.set_xlabel("$t$ (Myr)",fontsize=labels)
ax_2.set_ylabel("$e_1$",fontsize=labels)
ax_3.set_ylabel("$i_{\mathrm{in}}$ (deg)",fontsize=labels)
ax_4.set_ylabel("$i_{\mathrm{out}}$ (deg)",fontsize=labels)

fig.savefig("ejemplo_3.png")
