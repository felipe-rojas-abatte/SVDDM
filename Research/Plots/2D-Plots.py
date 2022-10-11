import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import interp1d
import sys
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
import os


current_dir = os.getcwd()
this_file = current_dir+'/data/'

#Data with Direct Detection limits (LUX experiment)
#(MDM,SIG)=np.genfromtxt(this_file+'LUX.dat', dtype=float,unpack=True,skip_header=False) 
#LUX_SIG=interp1d(MDM, SIG, kind='linear')

#Data with Direct Detection limits (XENON1T experiment)
#(MDM2,SIG2)=np.genfromtxt(this_file+'XENON1T.dat', dtype=float,unpack=True,skip_header=False) 
#XENON_SIG=interp1d(MDM2, SIG2, kind='linear')

#PLANCK measurements
Mv = np.linspace(10, 1000, 1000)
omega = np.linspace(0.1184,0.1184,1000)

#Mv_LEP = np.linspace(45, 45, 1000)
#omega_LEP = np.linspace(1E-7,1E3,1000)
#omega_LEP_DD = np.linspace(1E-15,1E-3,1000)

#Read data for no-degenerate values of Masses
Mv1a, Mv2a, Mvpa, MSa, lamLa, lamSa, lamSVa, lamHSa, Ome1a, Ome2a, prt1a, prt2a, phfla, Brv1a, Brv2a, Brsa, Brhaa, WHa = np.genfromtxt(this_file+"scan_grid_ldHS=0.1_ldSV=0.1_MS=100.dat", dtype=float, unpack=True, skip_header=True) 
Mv1b, Mv2b, Mvpb, MSb, lamLb, lamSb, lamSVb, lamHSb, Ome1b, Ome2b, prt1b, prt2b, phflb, Brv1b, Brv2b, Brsb, Brhab, WHb = np.genfromtxt(this_file+"scan_grid_ldHS=0.1_ldSV=0.1_MS=300.dat", dtype=float, unpack=True, skip_header=True, comments='#') 
Mv1c, Mv2c, Mvpc, MSc, lamLc, lamSc, lamSVc, lamHSc, Ome1c, Ome2c, prt1c, prt2c, phflc, Brv1c, Brv2c, Brsc, Brhac, WHc = np.genfromtxt(this_file+"scan_grid_ldHS=0.1_ldSV=0.1_MS=500.dat", dtype=float, unpack=True, skip_header=True, comments='#') 
Mv1d, Mv2d, Mvpd, MSd, lamLd, lamSd, lamSVd, lamHSd, Ome1d, Ome2d, prt1d, prt2d, phfld, Brv1d, Brv2d, Brsd, Brhad, WHd = np.genfromtxt(this_file+"scan_grid_ldHS=0.1_ldSV=0.1_MS=800.dat", dtype=float, unpack=True, skip_header=True, comments='#') 
Mv1e, Mv2e, Mvpe, MSe, lamLe, lamSe, lamSVe, lamHSe, Ome1e, Ome2e, prt1e, prt2e, phfle, Brv1e, Brv2e, Brse, Brhae, WHe = np.genfromtxt(this_file+"scan_grid_ldL=0.1_ldSV=0.1_MS=500.dat", dtype=float, unpack=True, skip_header=True, comments='#') 
Mv1f, Mv2f, Mvpf, MSf, lamLf, lamSf, lamSVf, lamHSf, Ome1f, Ome2f, prt1f, prt2f, phflf, Brv1f, Brv2f, Brsf, Brhaf, WHf = np.genfromtxt(this_file+"scan_grid_ldL=0.1_ldSV=0.1_MS=200.dat", dtype=float, unpack=True, skip_header=True, comments='#') 

################################################################
## Planck limits for Relic Density vs Mh1 for no-degenerate case
################################################################
fig1, ax1 = plt.subplots()

ax1.fill_between(Mv, omega, 1000 ,facecolor='red', alpha=0.25,  interpolate=True)
ax1.text(0.7, 0.72, 'overabundance \n non physical', verticalalignment='top', horizontalalignment='center', transform=ax1.transAxes, color='red', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density ($\\Omega h^2_{v1}$ + $\\Omega h^2_{S}$)",fontsize=15)
plt.title('M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV \n M$_S = 100$ GeV, $\\lambda_{HS} = 0.1$, $\\lambda_{VS}$ = 0.1',fontsize=15)
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')
plt.xlim(10,1010)
plt.ylim(1E-5,1E3)

N = 991

MV1 = [Mv1a[i] for i in range (0,N)]
OME_ldL_1 = [Ome1a[i]+Ome2a[i] for i in range (0,N)]
NDEG1, = plt.plot(MV1, OME_ldL_1, label='$\lambda_L=1$',color='k',linestyle='-')

MV2 = [Mv1a[i] for i in range (N,2*N)]
OME_ldL_01 = [Ome1a[i]+Ome2a[i] for i in range (N,2*N)]
NDEG2, = plt.plot(MV2, OME_ldL_01, label='$\lambda_L=0.1$',color='r',linestyle='-')

MV3 = [Mv1a[i] for i in range (2*N,3*N)]
OME_ldL_001 = [Ome1a[i]+Ome2a[i] for i in range (2*N,3*N)]
NDEG3, = plt.plot(MV3, OME_ldL_001, label='$\lambda_L=0.01$',color='m',linestyle='-')

MV4 = [Mv1a[i] for i in range (3*N,4*N)]
OME_ldL_n1 = [Ome1a[i]+Ome2a[i] for i in range (3*N,4*N)]
NDEG4, = plt.plot(MV4, OME_ldL_n1, label='$\lambda_L=-1$',color='k',linestyle='--')

MV5 = [Mv1a[i] for i in range (4*N,5*N)]
OME_ldL_n01 = [Ome1a[i]+Ome2a[i] for i in range (4*N,5*N)]
NDEG5, = plt.plot(MV5, OME_ldL_n01, label='$\lambda_L=-0.1$',color='r',linestyle='--')

MV6 = [Mv1a[i] for i in range (5*N,6*N)]
OME_ldL_n001 = [Ome1a[i]+Ome2a[i] for i in range (5*N,6*N)]
NDEG6, = plt.plot(MV6, OME_ldL_n001, label='$\lambda_L=-0.01$',color='m',linestyle='--')

PLANCK, = plt.plot(Mv, omega, linestyle='-.', color='red', linewidth=2, label=' $\\Omega h^2$ PLANCK measurement')

#Creamos la primera leyenda
legend1 = plt.legend(handles=[NDEG1,NDEG2,NDEG3,NDEG4,NDEG5,NDEG6], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) 

#Agregamos la primera leyenda
plt.gca().add_artist(legend1)

#Agregamos segunda leyenda
plt.legend(handles=[PLANCK], loc="lower left", ncol=1, handlelength=3, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1)

#plt.legend(loc="upper right", borderaxespad=0.1)
plt.savefig('Omega_Mv1_nodeg_ldHS=0.1_MS=100.pdf')

################################################################
## Planck limits for Relic Density vs Mh1 for no-degenerate case
################################################################
fig2, ax2 = plt.subplots()

ax2.fill_between(Mv, omega, 1000 ,facecolor='red', alpha=0.25,  interpolate=True)
ax2.text(0.7, 0.72, 'overabundance \n non physical', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='red', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density ($\\Omega h^2_{v1}$ + $\\Omega h^2_{S}$)",fontsize=15)
plt.title('M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV \n M$_S = 300$ GeV, $\\lambda_{HS} = 0.1$, $\\lambda_{VS}$ = 0.1',fontsize=15)
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')
plt.xlim(10,1010)
plt.ylim(1E-5,1E3)

MV1 = [Mv1b[i] for i in range (0,N)]
OME_ldL_1 = [Ome1b[i]+Ome2b[i] for i in range (0,N)]
NDEG1b, = plt.plot(MV1, OME_ldL_1, label='$\lambda_L=1$',color='k',linestyle='-')

MV2 = [Mv1b[i] for i in range (N,2*N)]
OME_ldL_01 = [Ome1b[i]+Ome2b[i] for i in range (N,2*N)]
NDEG2b, = plt.plot(MV2, OME_ldL_01, label='$\lambda_L=0.1$',color='r',linestyle='-')

MV3 = [Mv1b[i] for i in range (2*N,3*N)]
OME_ldL_001 = [Ome1b[i]+Ome2b[i] for i in range (2*N,3*N)]
NDEG3b, = plt.plot(MV3, OME_ldL_001, label='$\lambda_L=0.01$',color='m',linestyle='-')

MV4 = [Mv1b[i] for i in range (3*N,4*N)]
OME_ldL_n1 = [Ome1b[i]+Ome2b[i] for i in range (3*N,4*N)]
NDEG4b, = plt.plot(MV4, OME_ldL_n1, label='$\lambda_L=-1$',color='k',linestyle='--')

MV5 = [Mv1b[i] for i in range (4*N,5*N)]
OME_ldL_n01 = [Ome1b[i]+Ome2b[i] for i in range (4*N,5*N)]
NDEG5b, = plt.plot(MV5, OME_ldL_n01, label='$\lambda_L=-0.1$',color='r',linestyle='--')

MV6 = [Mv1b[i] for i in range (5*N,6*N)]
OME_ldL_n001 = [Ome1b[i]+Ome2b[i] for i in range (5*N,6*N)]
NDEG6b, = plt.plot(MV6, OME_ldL_n001, label='$\lambda_L=-0.01$',color='m',linestyle='--')

PLANCK, = plt.plot(Mv, omega, linestyle='-.', color='red', linewidth=2, label=' $\\Omega h^2$ PLANCK measurement')

#Creamos la primera leyenda
legend2 = plt.legend(handles=[NDEG1b,NDEG2b,NDEG3b,NDEG4b,NDEG5b,NDEG6b], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) 

#Agregamos la primera leyenda
plt.gca().add_artist(legend2)

#Agregamos segunda leyenda
plt.legend(handles=[PLANCK], loc="lower left", ncol=1, handlelength=3, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1)

#plt.legend(loc="upper right", borderaxespad=0.1)
plt.savefig('Omega_Mv1_nodeg_ldHS=0.1_MS=300.pdf')

################################################################
## Planck limits for Relic Density vs Mh1 for no-degenerate case
################################################################
fig3, ax3 = plt.subplots()

ax3.fill_between(Mv, omega, 1000 ,facecolor='red', alpha=0.25,  interpolate=True)
ax3.text(0.7, 0.72, 'overabundance \n non physical', verticalalignment='top', horizontalalignment='center', transform=ax3.transAxes, color='red', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density ($\\Omega h^2_{v1}$ + $\\Omega h^2_{S}$)",fontsize=15)
plt.title('M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV \n M$_S = 500$ GeV, $\\lambda_{HS} = 0.1$, $\\lambda_{VS}$ = 0.1',fontsize=15)
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')
plt.xlim(10,1010)
plt.ylim(1E-5,1E3)

MV1 = [Mv1c[i] for i in range (0,N)]
OME_ldL_1 = [Ome1c[i]+Ome2c[i] for i in range (0,N)]
NDEG1c, = plt.plot(MV1, OME_ldL_1, label='$\lambda_L=1$',color='k',linestyle='-')

MV2 = [Mv1c[i] for i in range (N,2*N)]
OME_ldL_01 = [Ome1c[i]+Ome2c[i] for i in range (N,2*N)]
NDEG2c, = plt.plot(MV2, OME_ldL_01, label='$\lambda_L=0.1$',color='r',linestyle='-')

MV3 = [Mv1c[i] for i in range (2*N,3*N)]
OME_ldL_001 = [Ome1c[i]+Ome2c[i] for i in range (2*N,3*N)]
NDEG3c, = plt.plot(MV3, OME_ldL_001, label='$\lambda_L=0.01$',color='m',linestyle='-')

MV4 = [Mv1c[i] for i in range (3*N,4*N)]
OME_ldL_n1 = [Ome1c[i]+Ome2c[i] for i in range (3*N,4*N)]
NDEG4c, = plt.plot(MV4, OME_ldL_n1, label='$\lambda_L=-1$',color='k',linestyle='--')

MV5 = [Mv1c[i] for i in range (4*N,5*N)]
OME_ldL_n01 = [Ome1c[i]+Ome2c[i] for i in range (4*N,5*N)]
NDEG5c, = plt.plot(MV5, OME_ldL_n01, label='$\lambda_L=-0.1$',color='r',linestyle='--')

MV6 = [Mv1c[i] for i in range (5*N,6*N)]
OME_ldL_n001 = [Ome1c[i]+Ome2c[i] for i in range (5*N,6*N)]
NDEG6c, = plt.plot(MV6, OME_ldL_n001, label='$\lambda_L=-0.01$',color='m',linestyle='--')

PLANCK, = plt.plot(Mv, omega, linestyle='-.', color='red', linewidth=2, label=' $\\Omega h^2$ PLANCK measurement')

#Creamos la primera leyenda
legend3 = plt.legend(handles=[NDEG1c,NDEG2c,NDEG3c,NDEG4c,NDEG5c,NDEG6c], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) 

#Agregamos la primera leyenda
plt.gca().add_artist(legend3)

#Agregamos segunda leyenda
plt.legend(handles=[PLANCK], loc="lower left", ncol=1, handlelength=3, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1)

#plt.legend(loc="upper right", borderaxespad=0.1)
plt.savefig('Omega_Mv1_nodeg_ldHS=0.1_MS=500.pdf')

################################################################
## Planck limits for Relic Density vs Mh1 for no-degenerate case
################################################################
fig3, ax3 = plt.subplots()

ax3.fill_between(Mv, omega, 1000 ,facecolor='red', alpha=0.25,  interpolate=True)
ax3.text(0.7, 0.72, 'overabundance \n non physical', verticalalignment='top', horizontalalignment='center', transform=ax3.transAxes, color='red', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density ($\\Omega h^2_{v1}$ + $\\Omega h^2_{S}$)",fontsize=15)
plt.title('M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV \n M$_S = 500$ GeV, $\\lambda_{HS} = 0.1$, $\\lambda_{VS}$ = 0.1',fontsize=15)
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')
plt.xlim(10,1010)
plt.ylim(1E-5,1E3)

MV1 = [Mv1d[i] for i in range (0,N)]
OME_ldL_1 = [Ome1d[i]+Ome2d[i] for i in range (0,N)]
NDEG1d, = plt.plot(MV1, OME_ldL_1, label='$\lambda_L=1$',color='k',linestyle='-')

MV2 = [Mv1d[i] for i in range (N,2*N)]
OME_ldL_01 = [Ome1d[i]+Ome2d[i] for i in range (N,2*N)]
NDEG2d, = plt.plot(MV2, OME_ldL_01, label='$\lambda_L=0.1$',color='r',linestyle='-')

MV3 = [Mv1d[i] for i in range (2*N,3*N)]
OME_ldL_001 = [Ome1d[i]+Ome2d[i] for i in range (2*N,3*N)]
NDEG3d, = plt.plot(MV3, OME_ldL_001, label='$\lambda_L=0.01$',color='m',linestyle='-')

MV4 = [Mv1d[i] for i in range (3*N,4*N)]
OME_ldL_n1 = [Ome1d[i]+Ome2d[i] for i in range (3*N,4*N)]
NDEG4d, = plt.plot(MV4, OME_ldL_n1, label='$\lambda_L=-1$',color='k',linestyle='--')

MV5 = [Mv1d[i] for i in range (4*N,5*N)]
OME_ldL_n01 = [Ome1d[i]+Ome2d[i] for i in range (4*N,5*N)]
NDEG5d, = plt.plot(MV5, OME_ldL_n01, label='$\lambda_L=-0.1$',color='r',linestyle='--')

MV6 = [Mv1d[i] for i in range (5*N,6*N)]
OME_ldL_n001 = [Ome1d[i]+Ome2d[i] for i in range (5*N,6*N)]
NDEG6d, = plt.plot(MV6, OME_ldL_n001, label='$\lambda_L=-0.01$',color='m',linestyle='--')

PLANCK, = plt.plot(Mv, omega, linestyle='-.', color='red', linewidth=2, label=' $\\Omega h^2$ PLANCK measurement')

#Creamos la primera leyenda
legend4 = plt.legend(handles=[NDEG1d,NDEG2d,NDEG3d,NDEG4d,NDEG5d,NDEG6d], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) 

#Agregamos la primera leyenda
plt.gca().add_artist(legend4)

#Agregamos segunda leyenda
plt.legend(handles=[PLANCK], loc="lower left", ncol=1, handlelength=3, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1)

#plt.legend(loc="upper right", borderaxespad=0.1)
plt.savefig('Omega_Mv1_nodeg_ldHS=0.1_MS=800.pdf')

################################################################
## Planck limits for Relic Density vs Mh1 for no-degenerate case
################################################################
fig4, ax4 = plt.subplots()

ax4.fill_between(Mv, omega, 1000 ,facecolor='red', alpha=0.25,  interpolate=True)
ax4.text(0.7, 0.72, 'overabundance \n non physical', verticalalignment='top', horizontalalignment='center', transform=ax4.transAxes, color='red', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density ($\\Omega h^2_{v1}$ + $\\Omega h^2_{S}$)",fontsize=15)
plt.title('M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV \n M$_S = 500$ GeV, $\\lambda_L = 0.1$, $\\lambda_{VS}$ = 0.1',fontsize=15)
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')
plt.xlim(10,1010)
plt.ylim(1E-5,1E3)

N = 991

MV1 = [Mv1e[i] for i in range (0,N)]
OME_ldHS_1 = [Ome1e[i]+Ome2e[i] for i in range (0,N)]
NDEG1e, = plt.plot(MV1, OME_ldHS_1, label='$\lambda_{HS}=1$',color='k',linestyle='-')

MV2 = [Mv1e[i] for i in range (N,2*N)]
OME_ldHS_01 = [Ome1e[i]+Ome2e[i] for i in range (N,2*N)]
NDEG2e, = plt.plot(MV2, OME_ldHS_01, label='$\lambda_{HS}=0.1$',color='r',linestyle='-')

MV3 = [Mv1e[i] for i in range (2*N,3*N)]
OME_ldHS_001 = [Ome1e[i]+Ome2e[i] for i in range (2*N,3*N)]
NDEG3e, = plt.plot(MV3, OME_ldHS_001, label='$\lambda_{HS}=0.01$',color='m',linestyle='-')

MV4 = [Mv1e[i] for i in range (3*N,4*N)]
OME_ldHS_0001 = [Ome1e[i]+Ome2e[i] for i in range (3*N,4*N)]
NDEG4e, = plt.plot(MV4, OME_ldHS_0001, label='$\lambda_{HS}=0.001$',color='g',linestyle='-')

PLANCK, = plt.plot(Mv, omega, linestyle='-.', color='red', linewidth=2, label=' $\\Omega h^2$ PLANCK measurement')

#Creamos la primera leyenda
legend4 = plt.legend(handles=[NDEG1e,NDEG2e,NDEG3e,NDEG4e], loc="upper left", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) 

#Agregamos la primera leyenda
plt.gca().add_artist(legend4)

#Agregamos segunda leyenda
plt.legend(handles=[PLANCK], loc="lower right", ncol=1, handlelength=3, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1)

#plt.legend(loc="upper right", borderaxespad=0.1)
plt.savefig('Omega_Mv1_nodeg_ldL=0.1_MS=500.pdf')

################################################################
## Planck limits for Relic Density vs Mh1 for no-degenerate case
################################################################
fig5, ax5 = plt.subplots()

ax5.fill_between(Mv, omega, 1000 ,facecolor='red', alpha=0.25,  interpolate=True)
ax5.text(0.7, 0.72, 'overabundance \n non physical', verticalalignment='top', horizontalalignment='center', transform=ax5.transAxes, color='red', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Relic Density ($\\Omega h^2_{v1}$ + $\\Omega h^2_{S}$)",fontsize=15)
plt.title('M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV \n M$_S = 200$ GeV, $\\lambda_L = 0.1$, $\\lambda_{VS}$ = 0.1',fontsize=15)
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')
plt.xlim(10,1010)
plt.ylim(1E-5,1E3)

N = 991

MV1 = [Mv1f[i] for i in range (0,N)]
OME_ldHS_1 = [Ome1f[i]+Ome2f[i] for i in range (0,N)]
NDEG1f, = plt.plot(MV1, OME_ldHS_1, label='$\lambda_{HS}=1$',color='k',linestyle='-')

MV2 = [Mv1f[i] for i in range (N,2*N)]
OME_ldHS_01 = [Ome1f[i]+Ome2f[i] for i in range (N,2*N)]
NDEG2f, = plt.plot(MV2, OME_ldHS_01, label='$\lambda_{HS}=0.1$',color='r',linestyle='-')

MV3 = [Mv1f[i] for i in range (2*N,3*N)]
OME_ldHS_001 = [Ome1f[i]+Ome2f[i] for i in range (2*N,3*N)]
NDEG3f, = plt.plot(MV3, OME_ldHS_001, label='$\lambda_{HS}=0.01$',color='m',linestyle='-')

MV4 = [Mv1f[i] for i in range (3*N,4*N)]
OME_ldHS_0001 = [Ome1f[i]+Ome2f[i] for i in range (3*N,4*N)]
NDEG4f, = plt.plot(MV4, OME_ldHS_0001, label='$\lambda_{HS}=0.001$',color='g',linestyle='-')

PLANCK, = plt.plot(Mv, omega, linestyle='-.', color='red', linewidth=2, label=' $\\Omega h^2$ PLANCK measurement')

#Creamos la primera leyenda
legend5 = plt.legend(handles=[NDEG1f,NDEG2f,NDEG3f,NDEG4f], loc="upper left", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) 

#Agregamos la primera leyenda
plt.gca().add_artist(legend5)

#Agregamos segunda leyenda
plt.legend(handles=[PLANCK], loc="lower right", ncol=1, handlelength=3, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1)

#plt.legend(loc="upper right", borderaxespad=0.1)
plt.savefig('Omega_Mv1_nodeg_ldL=0.1_MS=200.pdf')

plt.clf()
