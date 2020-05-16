# Excludes anomalous Relic Density points  
cut0=(omega1>0)&(omega2>0)

########################
#Teoretical constraints#
########################

#--------Definition of parameters
pi=np.pi
EE=0.31343     
MZ=91.188
MW=80.385      
CW=MW/MZ 
SW=(1-CW**2)**0.5 
vv=2*MW/EE*SW
MH=125
alp=EE**2/(4*pi)
g=EE/SW

#-------Definition of lambda couplings as function of independet parameters
l2 = lamL + (2./vv**2)*(Mv1**2 - Mvp**2)
l3 = (1./vv**2)*(2*Mvp**2 - Mv1**2 - Mv2**2)
l4 = (1./vv**2)*(Mv2**2 - Mv1**2) 
MV2 = Mv1**2 + vv**2*lamL/2
lamR = l2 + l3 - l4

#########################
#Theoretical constraints#
#########################

#-------Perturbativity-------------
cut_pert=(abs(l2)<4*pi)&(abs(l3)<4*pi)&(abs(l4)<4*pi)&(lamL<4*pi)&(lamS<4*pi)&(lamSV<4*pi)&(lamHS<4*pi)
cut1 = cut_pert

##############################
#Experimantal LHC constraints#
##############################

#----- LEP limits
MZ=91.188 #(Z-boson mass)
MW=80.385 #(W-boson mass)

cut_LEPW = (Mv1+Mvp > MW)&(Mv2+Mvp > MW)
cut_LEPZ = (Mv1+Mv2 > MZ)&(2*Mvp > MZ)

cut_LEPa=(Mv1>100)|(Mv2>200)|(Mv2-Mv1<8)|(Mv2+Mv1>198-8)
cut_LEPb=(Mvp>93)

cut2 = cut_LEPW&cut_LEPZ&cut_LEPa&cut_LEPb 

## ----- Invisible Higgs decay limits (h->inv)

cut_invH = (Brv1 + Brv2 + Brs < 0.24)
cut3 = cut_invH

# ------ Diphoton limits (h->AA)

SMBrHAA=2.28E-03  # SM Branching of Higgs decay into diphoton
RAA=BrHAA/SMBrHAA  # Diphoton parameter
#cut_RAA = (RAA<1.16+0.40)&(RAA>1.16-0.36) 
#cut4 = cut_RAA 

cut_RAA = (RAA<0.99+0.14)&(RAA>0.99-0.14)
cut4 = cut_RAA

######################################
#Experimantal Dark Matter constraints#
######################################

#------- Relic Density limits (PLANCK experiment)
omega = omega1 + omega2
cut5=(omega<0.1196)
cut10=cut1&(omega>0.1172)

# Direct Detection limits
#R_ome = omega/0.112  #Re-scale of Omega
#Psi_hat = R_ome*prot

#cut6=(Psi_hat<LUX) # (LUX experiment)
#cut7=(Psi_hat<XENON) #(XENON experiment)

#-------Unitarity----------------





