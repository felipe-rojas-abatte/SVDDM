#size of the dots in scatter plot
dots=6
#Create the features of the colorbar
bounds=np.linspace(-7,5,13,endpoint=True)
lim_inf = np.log10(0.0000001)
lim_sup = np.log10(100)

Mvchar = np.linspace(10, 2000, 1000) 
mu_sup = np.linspace(1.16+0.40, 1.16+0.40, 1000)
mu_inf = np.linspace(1.16-0.36, 1.16-0.36, 1000)

mu_sup_new = np.linspace(0.99+0.14,0.99+0.14,1000) 
mu_inf_new = np.linspace(0.99-0.14,0.99-0.14,1000)

bounds_l2=np.linspace(-10,10,21,endpoint=True)
lim_inf_l2 = -10
lim_sup_l2 = 10

bounds_lamL=np.linspace(-12,12,21,endpoint=True)
lim_inf_lamL = -12
lim_sup_lamL = 12

lambdaL = np.linspace(-12, 12, 1000) 
mu_sup = np.linspace(1.16+0.40, 1.16+0.40, 1000)
mu_inf = np.linspace(1.16-0.36, 1.16-0.36, 1000)

#Define the quantity of colors in colorbar
cmap = plt.get_cmap('jet') 

Mv = np.linspace(10, 2000, 1000)
y = Mv

current_dir = os.getcwd()
new_folder = current_dir+'/Systematic_cuts/'+cuts

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

#----------- Plot 1 Mv1-ld345-Omega-------------------------
fig, ax = plt.subplots(figsize=(6,4))
cax = ax.scatter(Mv1[cut], lamL[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax=lim_sup, s=dots, edgecolor='', rasterized=True)
cbar = fig.colorbar(cax,ticks=bounds, format="$10^{%.d}$")
cbar.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("Mv$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_L$", fontsize=20)
plt.xlim(min(Mv1),max(Mv1))
plt.xscale('log')
#plt.xlim(min(Mh1),200)
plt.ylim(min(lamL),max(lamL))
fig.tight_layout()
plt.savefig(new_folder+'/Mv1_lamL_Omega_'+cuts+'.pdf')

#----------- Plot 1 Ms-ldhs-Omega-------------------------
fig, ax = plt.subplots(figsize=(6,4))
cax = ax.scatter(MS[cut], lamHS[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax=lim_sup, s=dots, edgecolor='', rasterized=True)
cbar = fig.colorbar(cax,ticks=bounds, format="$10^{%.d}$")
cbar.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("M$_s$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_{HS}$", fontsize=20)
plt.xlim(min(MS),max(MS))
plt.xscale('log')
#plt.xlim(min(Mh1),200)
plt.ylim(min(lamHS),max(lamHS))
fig.tight_layout()
plt.savefig(new_folder+'/MS_lamHS_Omega_'+cuts+'.pdf')


# ---------- Plot 2 Mv1-Mv2-Omega --------------------------
fig2, ax2 = plt.subplots(figsize=(6,4))
cax2 = ax2.scatter(Mv1[cut], Mv2[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax =lim_sup, s=dots, edgecolor='', rasterized=True)
cbar2 = fig2.colorbar(cax2,ticks=bounds, format="$10^{%.d}$")
cbar2.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

if excluded_region==1:
	ax2.fill_between(Mv, y, 10 ,facecolor='gray', alpha = 0.45, interpolate=True)
	ax2.text(0.75, 0.35, 'Excluded region  \n Mv$_{1} > $Mv$_{2}$', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='black', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Mv$_2$ (GeV)",fontsize=15)
plt.xlim(min(Mv1),max(Mv1))
plt.ylim(min(Mv2),max(Mv2))
#plt.xlim(10,2000)
#plt.ylim(10,2000)
plt.xscale('log')
plt.yscale('log')
fig2.tight_layout()
plt.savefig(new_folder+'/Mv1_Mv2_Omega_'+cuts+'.pdf')

# ---------- Plot 3 Mv1-Mvp-Omega --------------------------
fig3, ax3 = plt.subplots(figsize=(6,4))
cax3 = ax3.scatter(Mv1[cut], Mvp[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax =lim_sup, s=dots, edgecolor='', rasterized=True)
cbar3 = fig3.colorbar(cax3,ticks=bounds, format="$10^{%.d}$")
cbar3.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

if excluded_region==1:
	ax3.fill_between(Mv, y, 10 ,facecolor='gray', alpha = 0.45, interpolate=True)
	ax3.text(0.75, 0.35, 'Excluded region  \n Mv$_{1} > $M$_{v^{\\pm}}$', verticalalignment='top', horizontalalignment='center', transform=ax3.transAxes, color='black', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("M$_{v^{\\pm}}$ (GeV)",fontsize=15)
plt.xlim(min(Mv1),max(Mv1))
plt.ylim(min(Mvp),max(Mvp))
#plt.xlim(10,2000)
#plt.ylim(10,2000)
plt.xscale('log')
plt.yscale('log')
fig3.tight_layout()
plt.savefig(new_folder+'/Mv1_Mvp_Omega_'+cuts+'.pdf')

# ---------- Plot 4 Mv2-Mvp-Omega --------------------------
fig4, ax4 = plt.subplots(figsize=(6,4))
cax4 = ax4.scatter(Mv2[cut], Mvp[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax =lim_sup, s=dots, edgecolor='', rasterized=True)
cbar4 = fig4.colorbar(cax4,ticks=bounds, format="$10^{%.d}$")
cbar4.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes
plt.xlabel("Mv$_2$ (GeV)",fontsize=15)
plt.ylabel("M$_{v^{\\pm}}$ (GeV)",fontsize=15)
plt.xlim(min(Mv2),max(Mv2))
plt.ylim(min(Mvp),max(Mvp))
plt.xscale('log')
plt.yscale('log')
fig4.tight_layout()
plt.savefig(new_folder+'/Mv2_Mvp_Omega_'+cuts+'.pdf')


# ---------- Plot 5 Mv1-Ms1-Omega --------------------------
fig5, ax5 = plt.subplots(figsize=(6,4))
cax5 = ax5.scatter(Mv1[cut], MS[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax =lim_sup, s=dots, edgecolor='', rasterized=True)
cbar5 = fig5.colorbar(cax5,ticks=bounds, format="$10^{%.d}$")
cbar5.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("M$_s$ (GeV)",fontsize=15)
plt.xlim(min(Mv1),max(Mv1))
plt.ylim(min(MS),max(MS))
#plt.xlim(10,2000)
#plt.ylim(10,2000)
plt.xscale('log')
plt.yscale('log')
fig5.tight_layout()
plt.savefig(new_folder+'/Mv1_Ms_Omega_'+cuts+'.pdf')

#----------- Plot 6 Ms1-lamHS-Omega-------------------------
fig6, ax6 = plt.subplots(figsize=(6,4))
cax6 = ax6.scatter(MS[cut], lamHS[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax=lim_sup, s=dots, edgecolor='', rasterized=True)
cbar6 = fig6.colorbar(cax6,ticks=bounds, format="$10^{%.d}$")
cbar6.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("M$_s$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_{\\phi S}$", fontsize=20)
plt.xlim(min(MS),max(MS))
plt.ylim(min(lamHS),max(lamHS))
plt.xscale('log')
fig6.tight_layout()
plt.savefig(new_folder+'/MS_lamHS_Omega_'+cuts+'.pdf')

#----------- Plot 6 Ms1-lamHS-Omega-------------------------
fig6, ax6 = plt.subplots(figsize=(6,4))
cax6 = ax6.scatter(lamL[cut], lamHS[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax=lim_sup, s=dots, edgecolor='', rasterized=True)
cbar6 = fig6.colorbar(cax6,ticks=bounds, format="$10^{%.d}$")
cbar6.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("$\\lambda_{L}$", fontsize=15)
plt.ylabel("$\\lambda_{\\phi S}$", fontsize=20)
plt.xlim(min(lamL),max(lamL))
plt.ylim(min(lamHS),max(lamHS))
#plt.xscale('log')
fig6.tight_layout()
plt.savefig(new_folder+'/lamL_lamHS_Omega_'+cuts+'.pdf')

#----------- Plot 6 Ms1-lamHS-Omega-------------------------
fig6, ax6 = plt.subplots(figsize=(6,4))
cax6 = ax6.scatter(lamSV[cut], lamHS[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax=lim_sup, s=dots, edgecolor='', rasterized=True)
cbar6 = fig6.colorbar(cax6,ticks=bounds, format="$10^{%.d}$")
cbar6.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes 
plt.xlabel("$\\lambda_{SV}$", fontsize=15)
plt.ylabel("$\\lambda_{\\phi S}$", fontsize=20)
plt.xlim(min(lamSV),max(lamSV))
plt.ylim(min(lamHS),max(lamHS))
#plt.xscale('log')
fig6.tight_layout()
plt.savefig(new_folder+'/lamSV_lamHS_Omega_'+cuts+'.pdf')

# ---------- Plot 2 MS-Mv2-Omega --------------------------
fig2, ax2 = plt.subplots(figsize=(6,4))
cax2 = ax2.scatter(MS[cut], Mv2[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax =lim_sup, s=dots, edgecolor='', rasterized=True)
cbar2 = fig2.colorbar(cax2,ticks=bounds, format="$10^{%.d}$")
cbar2.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes
plt.xlabel("M$_S$ (GeV)",fontsize=15)
plt.ylabel("Mv$_2$ (GeV)",fontsize=15)
#plt.xlim(10,2000)
#plt.ylim(10,2000)
plt.xlim(min(MS),max(MS))
plt.ylim(min(Mv2),max(Mv2))
plt.xscale('log')
plt.yscale('log')
fig2.tight_layout()
plt.savefig(new_folder+'/MS_Mv2_Omega_'+cuts+'.pdf')

# ---------- Plot 3 MS-Mvp-Omega --------------------------
fig3, ax3 = plt.subplots(figsize=(6,4))
cax3 = ax3.scatter(MS[cut], Mvp[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax =lim_sup, s=dots, edgecolor='', rasterized=True)
cbar3 = fig3.colorbar(cax3,ticks=bounds, format="$10^{%.d}$")
cbar3.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes
plt.xlabel("M$_S$ (GeV)",fontsize=15)
plt.ylabel("M$_{v^{\\pm}}$ (GeV)",fontsize=15)
#plt.xlim(10,2000)
#plt.ylim(10,2000)
plt.xlim(min(MS),max(MS))
plt.ylim(min(Mvp),max(Mvp))
plt.xscale('log')
plt.yscale('log')
fig3.tight_layout()
plt.savefig(new_folder+'/MS_Mvp_Omega_'+cuts+'.pdf')


# ---------- Plot 7 RAA-Mv1-Omega --------------------------
fig7, ax7 = plt.subplots(figsize=(6,4))
cax7 = ax7.scatter(Mv1[cut],RAA[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax =lim_sup, s=dots, edgecolor='', rasterized=True)
cbar7 = fig7.colorbar(cax7,ticks=bounds, format="$10^{%.d}$")
cbar7.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("$\\mu_{\\gamma \\gamma}$ ",fontsize=15)
plt.xlim(min(Mv1),max(Mv1))
plt.ylim(0,2)
plt.xscale('log')
#MUAA1, = plt.plot(Mv, mu_sup, color='r',linewidth=2, label='$ \\mu_{\\gamma \\gamma}$ by ATLAS at $\\sqrt{s} = 7$ and $8$ TeV')
#MUAA2, = plt.plot(Mv, mu_inf, color='r',linewidth=2)
MUAA3, = plt.plot(Mv, mu_sup_new, color='r',linewidth=2, linestyle='--', label='$ \\mu_{\\gamma \\gamma}$ by ATLAS at $\\sqrt{s} = 13$ TeV')
MUAA4, = plt.plot(Mv, mu_inf_new, color='r',linewidth=2, linestyle='--')

legend1b = plt.legend(handles=[MUAA3], loc="upper left", ncol=1, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.gca().add_artist(legend1b)
fig7.tight_layout()
plt.savefig(new_folder+'/RAA_Mv1_Omega_'+cuts+'.pdf')


# ---------- Plot 8 RAA-Mvp-Omega --------------------------
fig8, ax8 = plt.subplots(figsize=(6,4))
cax8 = ax8.scatter(Mvp[cut],RAA[cut], c=np.log10(omega[cut]), cmap=cmap, vmin=lim_inf, vmax =lim_sup, s=dots, edgecolor='', rasterized=True)
cbar8 = fig8.colorbar(cax8,ticks=bounds, format="$10^{%.d}$")
cbar8.set_label('Relic Density $\\Omega h^2$', rotation=90, fontsize=15)

#Name of axes
plt.xlabel("M$_{V^{\\pm}}$ (GeV)",fontsize=15)
plt.ylabel("$\\mu_{\\gamma \\gamma}$ ",fontsize=15)
plt.xlim(min(Mvp),max(Mvp))
plt.ylim(0,2)
plt.xscale('log')
#MUAA1, = plt.plot(Mvchar, mu_sup, color='r',linewidth=2, label='$ \\mu_{\\gamma \\gamma}$ by ATLAS at $\\sqrt{s} = 7$ and $8$ TeV')
#MUAA2, = plt.plot(Mvchar, mu_inf, color='r',linewidth=2)
MUAA3, = plt.plot(Mvchar, mu_sup_new, color='r',linewidth=2, linestyle='--', label='$ \\mu_{\\gamma \\gamma}$ by ATLAS at $\\sqrt{s} = 13$ TeV')
MUAA4, = plt.plot(Mvchar, mu_inf_new, color='r',linewidth=2, linestyle='--')

legend2b = plt.legend(handles=[MUAA3], loc="upper left", ncol=1, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.gca().add_artist(legend2b)
fig8.tight_layout()
plt.savefig(new_folder+'/RAA_Mvp_Omega_'+cuts+'.pdf')

# ---------- Plot 9 RAA-Mvp-l2 --------------------------
fig9, ax9 = plt.subplots(figsize=(6,4))
cax9 = ax9.scatter(Mvp[cut],RAA[cut], c=l2[cut], cmap=cmap, vmin=lim_inf_l2, vmax=lim_sup_l2, s=dots, edgecolor='', rasterized=True)
cbar9 = fig9.colorbar(cax9,ticks=bounds_l2, format="$%.d$")
cbar9.set_label('$\\lambda_2$', rotation=90, fontsize=15)

#Name of axes
plt.xlabel("M$_{V^{\\pm}}$ (GeV)",fontsize=15)
plt.ylabel("$\\mu_{\\gamma \\gamma}$ ",fontsize=15)
plt.xlim(min(Mvp),max(Mvp))
plt.ylim(0,2)
plt.xscale('log')
#MUAA1, = plt.plot(Mvchar, mu_sup, color='r',linewidth=2, label='$\\mu_{\\gamma \\gamma}$ by ATLAS at $\\sqrt{s} = 7$ and $8$ TeV')
#MUAA2, = plt.plot(Mvchar, mu_inf, color='r',linewidth=2)
MUAA3, = plt.plot(Mvchar, mu_sup_new, color='r',linewidth=2, linestyle='--', label='$\\mu_{\\gamma \\gamma}$ by ATLAS at $\\sqrt{s} = 13$ TeV')
MUAA4, = plt.plot(Mvchar, mu_inf_new, color='r',linewidth=2, linestyle='--')

legend3b = plt.legend(handles=[MUAA3], loc="upper left", ncol=1, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.gca().add_artist(legend3b)
fig9.tight_layout()
plt.savefig(new_folder+'/RAA_Mvp_l2_'+cuts+'.pdf')


