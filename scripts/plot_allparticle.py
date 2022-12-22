import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('./review.mplstyle')
import numpy as np
import math

def MySaveFig(fig, pltname):
    filename = pltname + '.pdf'
    print ("Saving plot as " + filename)
    fig.savefig(filename)
    
def SetAxes(ax):
    #Set x-axis
    ax.minorticks_off()
    ax.set_xscale('log')
    ax.set_xlim([1e4, 1e12])
    ax.set_xlabel('Energy [GeV]')
    #Set y-axis
    ax.set_yscale('log')
    ax.set_ylim([1e5, 1e7])
    ax.set_ylabel(r'E$^3$ Flux [GeV$^2$/m$^2$ s sr]')

def plot_data(ax, filename, fmt, color, label):
    filename = 'kiss_tables/' + filename
    E, dJdE, err_stat_lo, err_stat_up, err_sys_lo, err_sys_up = np.loadtxt(filename,skiprows=7,usecols=(0,1,2,3,4,5),unpack=True)
    y = np.power(E, 3.0) * dJdE
    dJdE_err = .5 * (err_stat_lo + err_stat_up)
    y_err = np.power(E, 3.0) * dJdE_err
    ax.errorbar(E, y, yerr=y_err, fmt=fmt, markeredgecolor=color, color=color, elinewidth=2, capthick=2, label=label, zorder=3)
    dJdE_err = .5 * (err_sys_lo + err_sys_up)
    y_err = np.power(E, 3.0) * dJdE_err
    ax.errorbar(E, y, yerr=y_err, fmt=fmt, markeredgecolor=color, color=color, elinewidth=2, capthick=2, zorder=3)
    
def plot_data_shifted(ax, filename, fmt, color, label, shift):
    E, dJdE, err_low, err_high = np.loadtxt(filename,skiprows=7,usecols=(0,1,2,3),unpack=True)
    E *= shift
    y = np.power(E, 3.0) * dJdE
    dJdE_err = .5 * (err_low + err_high)
    y_err = np.power(E, 3.0) * dJdE_err
    ax.errorbar(E, y, yerr=y_err, fmt=fmt, markeredgecolor=color, color=color, elinewidth=2, capthick=2, label=label, zorder=3)

def plot_data_back(ax, filename):
    E, dJdE, err_low, err_high = np.loadtxt(filename,skiprows=7,usecols=(0,1,2,3),unpack=True)
    y = np.power(E, 3.0) * dJdE
    dJdE_err = .5 * (err_low + err_high)
    y_err = np.power(E, 3.0) * dJdE_err
    ax.errorbar(E, y, yerr=y_err, fmt='o', markeredgecolor='silver', color='silver', elinewidth=2, capthick=2, zorder=1)

def plot_alldata_back(ax):
    plot_data_back(ax, 'kiss_tables/allparticle_AUGER_Etot.txt')
    plot_data_back(ax, 'kiss_tables/allparticle_TA_Etot.txt')
    plot_data_back(ax, 'kiss_tables/allparticle_TIBET_QGSJET+PD_Etot.txt')
    plot_data_back(ax, 'kiss_tables/allparticle_NUCLEON_Etot.txt')
    plot_data_back(ax, 'kiss_tables/allparticle_HAWC_Etot.txt')
    plot_data_back(ax, 'kiss_tables/allparticle_TUNKA-133_Etot.txt')
    plot_data_back(ax, 'kiss_tables/allparticle_KASCADE_QGSjet-II-02_Etot.txt')
    plot_data_back(ax, 'kiss_tables/allparticle_KASCADEGrande_QGSJET-II-04_Etot.txt')
    plot_data_back(ax, 'kiss_tables/allparticle_ICECUBE-ICETOP_SIBYLL-2.1_Etot.txt')
    plot_data_back(ax, 'kiss_tables/allparticle_TALE_Etot.txt')
        
### PLOT ROUTINES ###
def plot_allparticle():
    fig = plt.figure(figsize=(13.5,8.5))
    ax = fig.add_subplot(111)
    SetAxes(ax)
    ax.set_ylim([1e5, 1e7])

    #plot_data(ax, 'Auger2021_allParticle_totalEnergy.txt', 'o', 'tab:blue', 'Auger 2021')
    plot_data(ax, 'Auger2019_allParticle_totalEnergy.txt', 'o', 'tab:red', 'Auger 2019')
    plot_data(ax, 'TA_allParticle_totalEnergy.txt', 'o', 'tab:blue', 'Telescope Array')

#    plot_data(ax, 'kiss_tables/allparticle_TIBET_QGSJET+HD_Etot.txt', '^', 'darkorange', 'TIBET - QGSJET+HD')
#    plot_data(ax, 'kiss_tables/allparticle_TIBET_QGSJET+PD_Etot.txt', 'o', 'tab:orange', 'TIBET - QGSJET+PD')
    plot_data(ax, 'Tibet_SIBYLL+HD_allparticle_totalEnergy.txt', '*', 'darkorange', 'TIBET - SIBYLL+HD')

    plot_data(ax, 'TUNKA-133_allParticle_totalEnergy.txt', 'o', 'tab:cyan', 'TUNKA-133')

    plot_data(ax, 'KASCADE_2011_QGSJET-II-02_allParticle_totalEnergy.txt', '^', 'tab:olive', 'KASCADE - QGSJET-II-02')
    plot_data(ax, 'KASCADE_2011_SIBYLL-2.1_allParticle_totalEnergy.txt', '*', 'm', 'KASCADE - SIBYLL-2.1')
#    #plot_data_back(ax, 'output/allparticle_KASCADE_EPOS-199_Etot.txt', 'o', 'm', 'KASCADE - EPOS-199')
#
#    plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_SIBYLL-2.3_Etot.txt', '^', 'm', 'KASCADE-Grande - SIBYLL 2.3')
#    #plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_SIBYLL-2.1_Etot.txt', '^', 'm', 'KASCADE-Grande - SIBYLL 2.1')
#    #plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_QGSJET-II-02_Etot.txt', '^', 'm', 'KASCADE-Grande - QGSJET II-02')
#    #plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_QGSJET-II-04_Etot.txt', '^', 'tab:pink', 'KASCADE-Grande - QGSJET II-04')
#    #plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_EPOS-LHC_Etot.txt', '^', 'm', 'KASCADE-Grande - EPOS-LHC')

    plot_data(ax, 'IceCube_SIBYLL-2.1_allParticle_totalEnergy.txt', '^', 'tab:green', 'IceCube-IceTop - Sibyll-2.1')
    plot_data(ax, 'TALE_allParticle_totalEnergy.txt', '^', 'tab:brown', 'TALE')

    plot_data(ax, 'NUCLEON_allParticle_totalEnergy.txt', 'o', 'tab:gray', 'NUCLEON')
    plot_data(ax, 'HAWC_allParticle_totalEnergy.txt', 'o', 'tab:purple', 'HAWC')

    plt.annotate('4 PeV', xy=(4e6, 2.5e6), xytext=(4e6, 1.25e6), fontsize=18, ha='center', va='bottom',
                arrowprops=dict(facecolor='black', shrink=0.2),
                )
    plt.annotate('26 x 4 PeV', xy=(26. * 4e6, 2.5e6), xytext=(26. * 4e6, 1.25e6), fontsize=18, ha='center', va='bottom',
                arrowprops=dict(facecolor='black', shrink=0.2),
                )
    plt.annotate('5 EeV', xy=(5e9, 1.2e6), xytext=(5e9, 0.6e6), fontsize=18, ha='center', va='bottom',
                arrowprops=dict(facecolor='black', shrink=0.2),
                )
    
    ax.legend(fontsize=12)
    MySaveFig(fig, 'allparticle_UHECR')

def plot_UHECR_AUGER_centric():
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    SetAxes(ax)

    ax.set_xticks([1e4,1e5,1e6,1e7,1e8,1e9,1e10,1e11,1e12])

    ax.set_ylim([3e5, 6e6])
    
    plot_data(ax, 'kiss_tables/allparticle_AUGER_Etot.txt', 'o', 'tab:blue', 'AUGER')
    plot_data_shifted(ax, 'kiss_tables/allparticle_TA_Etot.txt', 'o', 'tab:red', 'TA -6\%', 0.94)

    #plot_data(ax, 'kiss_tables/allparticle_TIBET_QGSJET+HD_Etot.txt', '^', 'darkorange', 'TIBET - QGSJET+HD')
    plot_data_shifted(ax, 'kiss_tables/allparticle_TIBET_QGSJET+PD_Etot.txt', 'o', 'tab:orange', 'TIBET - QGSJET+PD', 0.96)
    #plot_data(ax, 'kiss_tables/allparticle_TIBET_SIBYLL+HD_Etot.txt', '*', 'darkorange', 'TIBET - SIBYLL+HD')

    plot_data_shifted(ax, 'kiss_tables/allparticle_TUNKA-133_Etot.txt', 'o', 'tab:cyan', 'TUNKA -6\%', 0.94)

    plot_data_shifted(ax, 'kiss_tables/allparticle_TALE_Etot.txt', '^', 'tab:brown', 'TALE -3\%', 0.97)
    plot_data_shifted(ax, 'kiss_tables/allparticle_ICECUBE-ICETOP_SIBYLL-2.1_Etot.txt', '^', 'tab:green', 'ICECUBE-ICETOP -8\%', 0.92)

    plot_data_shifted(ax, 'kiss_tables/allparticle_NUCLEON_Etot.txt', 'o', 'tab:gray', 'NUCLEON -10\%', 0.85,)
    plot_data_shifted(ax, 'kiss_tables/allparticle_HAWC_Etot.txt', 'o', 'tab:purple', 'HAWC -10\%', 0.85,)

    E = np.logspace(4,12,100)
    ax.plot(E, 5.0e5 * np.power(E / 1e4, 3. - 2.7), ':', label=r'$E^{-2.7}$')
    ax.plot(E, 3.0e6 * np.power(E / 1e6, 3. - 3.), ':', label=r'$E^{-3.0}$')
    ax.plot(E, 3.8e6 * np.power(E / 1e8, 3. - 3.3), ':', label=r'$E^{-3.3}$')

#    ax.plot([5e6,5e6],[1e0,1e10], '--')
#    ax.plot([26.*5e6,26.*5e6],[1e0,1e10], '--')

    ax.legend(fontsize=16)
    MySaveFig(fig, 'allparticle_UHECR_AUGER')

def plot_KASCADE():
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    SetAxes(ax)
    
    ax.set_xlim([1e6, 1e10])
    ax.set_ylim([1e6, 1e7])

    #plot_alldata_back(ax)

    plot_data(ax, 'kiss_tables/allparticle_KASCADE_QGSjet-II-02_Etot.txt', '^', 'tab:orange', 'KASCADE - QGSJET-II-02')
    plot_data(ax, 'kiss_tables/allparticle_KASCADE_SIBYLL-2.1_Etot.txt', '*', 'tab:olive', 'KASCADE - SIBYLL-2.1')
    plot_data(ax, 'kiss_tables/allparticle_KASCADE_EPOS-199_Etot.txt', 'o', 'tab:blue', 'KASCADE - EPOS-199')

    #plot_data(ax, 'output/allparticle_KASCADEGrande_SIBYLL-21_Etot.txt', '^', 'm', 'KASCADE-Grande - SIBYLL 2.1')
    #plot_data(ax, 'output/allparticle_KASCADEGrande_QGSJET-II-02_Etot.txt', '^', 'm', 'KASCADE-Grande - QGSJET II-02')
    plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_QGSJET-II-04_Etot.txt', '^', 'tab:red', 'KASCADE-Grande - QGSJET II-04')
    plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_SIBYLL-2.3_Etot.txt', '*', 'tab:green', 'KASCADE-Grande - SIBYLL 2.3')
    plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_EPOS-LHC_Etot.txt', 'o', 'tab:purple', 'KASCADE-Grande - EPOS-LHC')

    ax.legend(fontsize=16)
    MySaveFig(fig, 'allparticle_KASCADE')

def plot_TIBET():
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    SetAxes(ax)

    ax.set_xlim([1e5, 1e9])
    ax.set_ylim([1e6, 1e7])

    #plot_alldata_back(ax)

    plot_data_shifted(ax, 'kiss_tables/allparticle_TIBET_QGSJET+HD_Etot.txt', '^', 'tab:orange', 'QGSJET+HD -3\%', 0.975)
    plot_data_shifted(ax, 'kiss_tables/allparticle_TIBET_QGSJET+PD_Etot.txt', 'o', 'tab:green', 'QGSJET+PD +4\%', 1.04)
    plot_data(ax, 'kiss_tables/allparticle_TIBET_SIBYLL+HD_Etot.txt', '*', 'tab:red', 'TIBET - SIBYLL+HD')

    ax.legend(fontsize=16)
    MySaveFig(fig, 'allparticle_TIBET')
   
def plot_protons():
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    SetAxes(ax)

    ax.set_ylim([0.3e4, 0.6e7])

    plot_data(ax, 'kiss_tables/H_DAMPE_Ek.txt', 'o', 'tab:orange', 'DAMPE') # Penso sia Etot!
    plot_data(ax, 'kiss_tables/H_CREAM-III_Ek.txt', '^', 'tab:green', 'CREAM')
    plot_data(ax, 'kiss_tables/H_ICECUBE-ICETOP_Etot.txt', '^', 'tab:red', 'ICECUBE-ICETOP')
    plot_data(ax, 'kiss_tables/H_NUCLEON_Etot.txt', '^', 'tab:brown', 'NUCLEON')
    
    plot_data(ax, 'kiss_tables/H_KASCADE_2005_QGSJET-01_Etot.txt', '*', 'tab:purple', 'KASCADE+05 QGSJet-01')
    plot_data(ax, 'kiss_tables/H_KASCADE_2005_SIBYLL-2.1_Etot.txt', '*', 'tab:pink', 'KASCADE+05 SIBYL-2.1')
    plot_data(ax, 'kiss_tables/H_KASCADE_2011_QGSJET-II-02_Etot.txt', '*', 'tab:olive', 'KASCADE+11 QGSJet-II-02')
    plot_data(ax, 'kiss_tables/H_KASCADE_2011_SIBYLL-2.1_Etot.txt', '*', 'tab:gray', 'KASCADE+11 SIBYLL-2.1')

    plot_data(ax, 'kiss_tables/H_KASCADEGrande_SIBYLL-2.3_Etot.txt', '*', 'tab:cyan', 'KASCADE-Grande SIBYLL-2.3')

    E, dJdE, err_low, err_high = np.loadtxt('AUGER_composition/H_AUGER_QGSJET-II-04_Etot.txt',
                                            skiprows=3,usecols=(0,1,2,3),unpack=True)
    y = np.power(E, 3.0) * dJdE
    dJdE_err = .5 * (err_low + err_high)
    y_err = np.power(E, 3.0) * dJdE_err
    color = 'b'
    label = 'AUGER QGSJET-II-04'
    ax.errorbar(E, y, yerr=y_err, fmt='o', markeredgecolor=color, color=color, elinewidth=2, capthick=2, label=label, zorder=3)

    E, dJdE, err_low, err_high = np.loadtxt('AUGER_composition/H_AUGER_SIBYLL-2.3_Etot.txt',
                                            skiprows=3,usecols=(0,1,2,3),unpack=True)
    y = np.power(E, 3.0) * dJdE
    dJdE_err = .5 * (err_low + err_high)
    y_err = np.power(E, 3.0) * dJdE_err
    color = 'm'
    label = 'AUGER SIBYLL-2.3'
    ax.errorbar(E, y, yerr=y_err, fmt='o', markeredgecolor=color, color=color, elinewidth=2, capthick=2, label=label, zorder=3)

#    ax.set_xlim([1e5, 1e9])
#    ax.set_ylim([1e6, 1e7])

    plot_alldata_back(ax)

    ax.legend(fontsize=12)
    MySaveFig(fig, 'protons_allexperiments')
   
def plot_light_ICECUBE(ax, fmt, color):
    E, dJdE_He, err_low, err_high = np.loadtxt('kiss_tables/He_ICECUBE-ICETOP_Etot.txt',skiprows=7,usecols=(0,1,2,3),unpack=True)
    E, dJdE_H, err_low, err_high = np.loadtxt('kiss_tables/H_ICECUBE-ICETOP_Etot.txt',skiprows=7,usecols=(0,1,2,3),unpack=True)
    y = np.power(E, 3.0) * (dJdE_H + dJdE_He)
    dJdE_err = .5 * (err_low + err_high)
    y_err = np.power(E, 3.0) * dJdE_err
    ax.errorbar(E, y, yerr=y_err, fmt=fmt, markeredgecolor=color, color=color, elinewidth=2, capthick=2, label='IC', zorder=3)


def plot_light():
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    SetAxes(ax)

    ax.set_ylim([0.3e5, 0.6e7])

    plot_data(ax, 'kiss_tables/light_ARGO_Etot.txt', 'o', 'tab:orange', 'ARGO')
#    plot_data(ax, 'kiss_tables/H_CREAM-III_Ek.txt', '^', 'tab:green', 'CREAM')
#    plot_data(ax, 'kiss_tables/H_ICECUBE-ICETOP_Etot.txt', '^', 'tab:red', 'ICECUBE-ICETOP')
#    plot_data(ax, 'kiss_tables/H_NUCLEON_Etot.txt', '^', 'tab:brown', 'NUCLEON')
#
    plot_data(ax, 'kiss_tables/light_KASCADEGrande_EPOS-LHC_Etot.txt', '*', 'tab:cyan', '')
    plot_data(ax, 'kiss_tables/light_KASCADEGrande_QGSJET-II-04_Etot.txt', '*', 'tab:cyan', '')
    plot_data(ax, 'kiss_tables/light_KASCADEGrande_SIBYLL-2.1_Etot.txt', '*', 'tab:cyan', '')

    plot_light_ICECUBE(ax, '^', 'tab:red')

#    plot_data(ax, 'kiss_tables/H_KASCADE_2011_SIBYLL-2.1_Etot.txt', '*', 'tab:cyan', '')
#    plot_data(ax, 'kiss_tables/H_KASCADEGrande_SIBYLL-2.3_Etot.txt', '*', 'tab:pink', '')

#    ax.set_xlim([1e5, 1e9])
#    ax.set_ylim([1e6, 1e7])

    plot_alldata_back(ax)

    ax.legend(fontsize=14)
    MySaveFig(fig, 'light_allexperiments')

def plot_UHECR_pc():
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    SetAxes(ax)
    ax.set_ylabel(r'E$^{2.7}$ Flux [GeV$^{1.7}$/m$^2$ s sr]')

    ax.set_ylim([1e3, 1e5])
    ax.set_xlim([1e4, 1e10])
#    plot_data(ax, 'kiss_tables/allparticle_AUGER_Etot.txt', 'o', 'tab:blue', 'AUGER')
#    plot_data(ax, 'kiss_tables/allparticle_TA_Etot.txt', 'o', 'tab:red', 'Telescope Array')
#
#    #plot_data(ax, 'kiss_tables/allparticle_TIBET_QGSJET+HD_Etot.txt', '^', 'darkorange', 'TIBET - QGSJET+HD')
#    #plot_data(ax, 'kiss_tables/allparticle_TIBET_QGSJET+PD_Etot.txt', 'o', 'tab:orange', 'TIBET - QGSJET+PD')
#    plot_data(ax, 'kiss_tables/allparticle_TIBET_SIBYLL+HD_Etot.txt', '*', 'darkorange', 'TIBET - SIBYLL+HD')
#
    plot_data(ax, 'kiss_tables/TUNKA-133_allParticle_totalEnergy.txt', 'o', 'tab:cyan', 'TUNKA-133')
##    plot_data(ax, 'kiss_tables/allparticle_TUNKA-Rex_Etot.txt', 'o', 'darkcyan', 'TUNKARex') # troppi pochi punti!
#
#    #plot_data(ax, 'kiss_tables/allparticle_KASCADE_QGSjet-II-02_Etot.txt', '^', 'tab:olive', 'KASCADE - QGSJET-II-02')
    plot_data(ax, 'kiss_tables/KASCADE_2011_SIBYLL-2.1_allParticle_totalEnergy.txt', '*', 'm', 'KASCADE - SIBYLL-2.1')
#    #plot_data_back(ax, 'output/allparticle_KASCADE_EPOS-199_Etot.txt', 'o', 'm', 'KASCADE - EPOS-199')
#
    plot_data(ax, 'kiss_tables/KASCADE-Grande_SIBYLL-2.3_allParticle_totalEnergy.txt', '^', 'm', 'KASCADE-Grande - SIBYLL 2.3')
#    #plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_SIBYLL-2.1_Etot.txt', '^', 'm', 'KASCADE-Grande - SIBYLL 2.1')
#    #plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_QGSJET-II-02_Etot.txt', '^', 'm', 'KASCADE-Grande - QGSJET II-02')
#    #plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_QGSJET-II-04_Etot.txt', '^', 'tab:pink', 'KASCADE-Grande - QGSJET II-04')
#    #plot_data(ax, 'kiss_tables/allparticle_KASCADEGrande_EPOS-LHC_Etot.txt', '^', 'm', 'KASCADE-Grande - EPOS-LHC')
#
#    #plot_data(ax, 'kiss_tables/allparticle_RUNJOB_Etot.txt', '^', 'y', 'RUNJOB') # outliers
#
    plot_data(ax, 'kiss_tables/ICECUBE-ICETOP_SIBYLL-2.1_allParticle_totalEnergy.txt', '^', 'tab:green', 'ICECUBE-ICETOP - Sibyll-2.1')
    plot_data(ax, 'kiss_tables/TALE_allParticle_totalEnergy.txt', '^', 'tab:brown', 'TALE')

    plot_data(ax, 'kiss_tables/NUCLEON_allParticle_totalEnergy.txt', 'o', 'tab:gray', 'NUCLEON')
#    plot_data(ax, 'kiss_tables/allparticle_HAWC_Etot.txt', 'o', 'tab:purple', 'HAWC')

#    plt.annotate('4 PeV', xy=(4e6, 2.5e6), xytext=(4e6, 1.25e6), fontsize=18, ha='center', va='bottom',
#                arrowprops=dict(facecolor='black', shrink=0.2),
#                )
#    plt.annotate('26 x 4 PeV', xy=(26. * 4e6, 2.5e6), xytext=(26. * 4e6, 1.25e6), fontsize=18, ha='center', va='bottom',
#                arrowprops=dict(facecolor='black', shrink=0.2),
#                )
#    plt.annotate('5 EeV', xy=(5e9, 1.2e6), xytext=(5e9, 0.6e6), fontsize=18, ha='center', va='bottom',
#                arrowprops=dict(facecolor='black', shrink=0.2),
#                )
    
    ax.legend(fontsize=12)
    MySaveFig(fig, 'allparticle_UHECR_pierre')

### MAiN ###
if __name__== "__main__":
    plot_allparticle()
    #plot_UHECR_AUGER_centric()
    #plot_KASCADE()
    #plot_TIBET()
    #plot_protons()
    #plot_light()
