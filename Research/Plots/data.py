#Data micrOMEGAs information
current_dir = os.getcwd()
this_file = current_dir+'/data/'

t1 = np.genfromtxt(this_file+'scan_rand.dat', dtype=float,unpack=True,skip_header=True)
#t2 = np.genfromtxt(this_file+'scan_rand2.dat', dtype=float,unpack=True,skip_header=True)
#t3 = np.genfromtxt(this_file+'scan_rand_sat.dat',dtype=float,unpack=True,skip_header=True)
#t10 = np.genfromtxt(this_file+'scan_ran_puntos.dat', dtype=float,unpack=True,skip_header=True)

#Put all the data together in one file
#tc = np.hstack((t1,t2,t3))
#tc = np.hstack((t1,t2))

(Mv1, Mv2, Mvp, MS, lamL, lamS, lamSV, lamHS, omega1, omega2, prot1, prot2, photf, Brv1, Brv2 , Brs, BrHAA, WH) = t1

#Data with Direct Detection limits (LUX experiment)
#(MDM_L,SIG_L)=np.genfromtxt(this_file+'LUX.dat',dtype=float,unpack=True,skip_header=False) 
#LUX_SIG=interp1d(MDM_L, SIG_L, kind='linear')
#LUX=LUX_SIG(Mv1)

#Data with Direct Detection limits (XENON1T experiment)
#(MDM_X,SIG_X)=np.genfromtxt(this_file+'XENON1T.dat',dtype=float,unpack=True,skip_header=False) 
#XENON_SIG=interp1d(MDM_X, SIG_X, kind='linear')
#XENON=XENON_SIG(Mv1)

