import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np

def my_savefig(fig, pltname, pngsave=False):
    if pngsave:
        filename = pltname + '.png'
    else:
        filename = pltname + '.pdf'
    print ("Saving plot as " + filename)
    fig.savefig(filename, bbox_inches='tight', dpi=300)

def set_axes(ax):
    #Set x-axis
    ax.minorticks_off()
    ax.set_xscale('log')
    ax.set_xlim([1e2, 1e7])
    ax.set_xlabel('Rigidity [GV]')
    #Set y-axis
    ax.set_yscale('log')
    ax.set_ylim([5e3, 2e5])
    ax.set_ylabel(r'R$^2$ I [GV m$^{-2}$ s$^{-1}$ sr$^{-1}$]')

def plot_data(ax, filename, color, fmt, zorder, label, norm=1.0):
    slope = 2.8
    
    E, dJdE, stat_low, stat_high, sys_low, sys_high = np.loadtxt("kiss_tables/" + filename,skiprows=7,usecols=(0,1,2,3,4,5),unpack=True)
    y = norm * np.power(E, slope) * dJdE
    
    dJdE_err = .5 * norm * (stat_low + stat_high)
    y_err = np.power(E, slope) * dJdE_err
    ax.errorbar(E, y, yerr=y_err, fmt=fmt, label=label, markeredgecolor=color, color=color,
                elinewidth=1.5, capthick=1.5, markersize=5.5, capsize=3.5, zorder=zorder)

    dJdE_err = .5 * norm * (sys_low + sys_high)
    y_err = np.power(E, slope) * dJdE_err
    ax.errorbar(E, y, yerr=y_err, fmt=fmt, markeredgecolor=color, color=color,
                elinewidth=1.5, capthick=2.5, markersize=5.5, capsize=4.5, zorder=zorder)
                
#def plot_data_from_Etot(ax, filename, color, norm, label, Z):
#    E, dJdE, err_low, err_high = np.loadtxt("kiss_tables/" + filename,skiprows=7,usecols=(0,1,2,3),unpack=True)
#    R = E / float(Z)
#    y = norm / float(Z) * np.power(E, 2.0) * dJdE
#    dJdE_err = .5 * norm * (err_low + err_high) / float(Z)
#    y_err = np.power(E, 2.0) * dJdE_err
#    ax.errorbar(R, y, yerr=y_err, fmt='o', label=label, markeredgecolor=color, color=color, elinewidth=1, capthick=1, zorder=Z, markersize=5)
#
#def yCR(i):
#    return 2e3 * np.power(0.45, i)
#
#def get_color(Z):
#    if Z == 'H':
#        return 'tab:blue'
#    elif Z == 'He':
#        return 'tab:orange'
#    elif Z == 'Li':
#        return 'tab:green'
#    elif Z == 'Be':
#        return 'tab:red'
#    elif Z == 'B':
#        return 'tab:purple'
#    elif Z == 'C':
#        return 'tab:brown'
#    elif Z == 'N':
#        return 'tab:pink'
#    elif Z == 'O':
#        return 'tomato'
#    elif Z == 'F':
#        return 'tab:olive'
#    elif Z == 'Ne':
#        return 'tab:cyan'
#    elif Z == 'Na':
#        return 'navy'
#    elif Z == 'Mg':
#        return 'darkorange'
#    elif Z == 'Al' :
#        return 'seagreen'
#    elif Z == 'Si':
#        return 'salmon'
#    elif Z == 'Fe':
#        return 'tab:gray'
#    elif Z == 'Ni':
#        return 'indigo'
#    else:
#        return 'Something is wrong'
#
#def plot_allgalactic():
#    fig = plt.figure(figsize=(12.5, 9.5))
#    ax = fig.add_subplot(111)
#    set_axes(ax)
#
#    ### AMS-02 ###
#    plot_data(ax, 'AMS-02_H_rigidity.txt', get_color('H'), 1., 'H', 1)
#    plot_data(ax, 'AMS-02_He_rigidity.txt', get_color('He'), 1., 'He', 2)
#    plot_data(ax, 'AMS-02_Li_rigidity.txt', get_color('Li'), 1., 'Li', 3)
#    plot_data(ax, 'AMS-02_Be_rigidity.txt', get_color('Be'), 1., 'Be', 4)
#    plot_data(ax, 'AMS-02_B_rigidity.txt', get_color('B'), 1., 'B', 5)
#    plot_data(ax, 'AMS-02_C_rigidity.txt', get_color('C'), 1., 'C', 6)
#    plot_data(ax, 'AMS-02_N_rigidity.txt', get_color('N'), 1., 'N', 7)
#    plot_data(ax, 'AMS-02_O_rigidity.txt', get_color('O'), 1., 'O', 8)
#    plot_data(ax, 'AMS-02_F_rigidity.txt', get_color('F'), 1., 'F', 9)
#    plot_data(ax, 'AMS-02_Ne_rigidity.txt', get_color('Ne'), 1., 'Ne', 10)
#    plot_data(ax, 'AMS-02_Na_rigidity.txt', get_color('Na'), 1., 'Na', 11)
#    plot_data(ax, 'AMS-02_Mg_rigidity.txt', get_color('Mg'), 1., 'Mg', 12)
#    plot_data(ax, 'AMS-02_Al_rigidity.txt', get_color('Al'), 1., 'Al', 13)
#    plot_data(ax, 'AMS-02_Si_rigidity.txt', get_color('Si'), 1., 'Si', 14)
#    plot_data(ax, 'AMS-02_Fe_rigidity.txt', get_color('Fe'), 1., 'Fe', 26)
#
#    ### CREAM ###
#    plot_data_from_Etot(ax, 'CREAM_III_H_totalEnergy.txt', get_color('H'), 1., 'H', 1)
#    plot_data_from_Etot(ax, 'CREAM_III_He_totalEnergy.txt', get_color('He'), 1., 'He', 2)
##    # Li
##    # Be
##    # B
#    plot_data_from_Etot(ax, 'CREAM_II_C_totalEnergy.txt', get_color('C'), 1., 'C', 6)
##    # N
#    plot_data_from_Etot(ax, 'CREAM_II_O_totalEnergy.txt', get_color('O'), 1., 'O', 8)
##    # F
#    plot_data_from_Etot(ax, 'CREAM_II_Ne_totalEnergy.txt', get_color('Ne'), 1., 'Ne', 10)
#    plot_data_from_Etot(ax, 'CREAM_II_Mg_totalEnergy.txt', get_color('Mg'), 1., 'Mg', 12)
#    plot_data_from_Etot(ax, 'CREAM_II_Si_totalEnergy.txt', get_color('Si'), 1., 'Si', 14)
#    plot_data_from_Etot(ax, 'CREAM_II_Fe_totalEnergy.txt', get_color('Fe'), 1., 'Fe', 26)
#
#    ### CALET ###
#    plot_data_from_Etot(ax, 'CALET_H_kineticEnergy.txt', get_color('H'), 1., 'H', 1)
##    plot_data_from_Etot(ax, 'C_CALET_Etot.txt', 'tab:brown', 1., 'C', 6)
##    plot_data_from_Etot(ax, 'O_CALET_Etot.txt', 'tab:olive', 1., 'O', 8)
#    plot_data_from_Etot(ax, 'CALET_Ni_kineticEnergy.txt', get_color('Ni'), 1., 'Ni', 1)
#
#    ### NUCLEON ###
#    plot_data_from_Etot(ax, 'NUCLEON_H_totalEnergy.txt', get_color('H'), 1., 'H', 1)
#    plot_data_from_Etot(ax, 'NUCLEON_He_totalEnergy.txt', get_color('He'), 1., 'He', 2)
#
#    ### DAMPE ###
#    plot_data(ax, 'DAMPE_H_kineticEnergy.txt', get_color('H'), 1., get_color('H'), 1)
#
#    fontsize=20
#    ax.text(7e5, yCR(0.),  'H',  color=get_color('H'),  fontsize=fontsize)
#    ax.text(7e5, yCR(1.),  'He', color=get_color('He'), fontsize=fontsize)
#    ax.text(7e5, yCR(2.),  'Li', color=get_color('Li'), fontsize=fontsize)
#    ax.text(7e5, yCR(3.),  'Be', color=get_color('Be'), fontsize=fontsize)
#    ax.text(7e5, yCR(4.),  'B',  color=get_color('B'),  fontsize=fontsize)
#    ax.text(7e5, yCR(5.),  'C',  color=get_color('C'),  fontsize=fontsize)
#    ax.text(7e5, yCR(6.),  'N',  color=get_color('N'),  fontsize=fontsize)
#    ax.text(7e5, yCR(7.),  'O',  color=get_color('O'),  fontsize=fontsize)
#    ax.text(7e5, yCR(8.),  'F',  color=get_color('F'),  fontsize=fontsize)
#    ax.text(7e5, yCR(9.),  'Ne', color=get_color('Ne'), fontsize=fontsize)
#    ax.text(7e5, yCR(10.), 'Na', color=get_color('Na'), fontsize=fontsize)
#    ax.text(7e5, yCR(11.), 'Mg', color=get_color('Mg'), fontsize=fontsize)
#    ax.text(7e5, yCR(12.), 'Al', color=get_color('Al'), fontsize=fontsize)
#    ax.text(7e5, yCR(13.), 'Si', color=get_color('Si'), fontsize=fontsize)
#    ax.text(7e5, yCR(14.), 'Fe', color=get_color('Fe'), fontsize=fontsize)
#    ax.text(7e5, yCR(15.), 'Ni', color=get_color('Ni'), fontsize=fontsize)
#
#    ax.text(2, 1.3e4, 'Credits: AMS-02, CALET, CREAM, DAMPE, NUCLEON', fontsize=15)
###    plot_data_from_Etot(ax, 'C_PAMELA_Etot.txt', 'tab:blue', 1e-5, 'CALET', 6.0)
###    plot_data(ax, 'H_NUCLEON_Etot.txt', 'tab:red', 1., 'CREAM')
###    plot_data(ax, 'H_ICECUBE-ICETOP_Etot.txt', 'tab:red', 1., 'CREAM')
###    plot_data(ax, 'H_KASCADEGrande_SIBYLL-2.3_Etot.txt', 'y', 1., 'KG')
#
#    plt.savefig('allgalactic.pdf')


def plot_unpublished_argo(ax):
    filename = '../data/unpublished_ARGO_light.txt'
    lgEmin, lgEmax, flux, stat, syst = np.loadtxt(filename, usecols=(0,1,2,3,4), skiprows=1, unpack=True)
    x = np.sqrt(np.power(10., lgEmin) * np.power(10., lgEmax)) * 1e3
    ax.plot(x, np.power(x, 2.8) * flux, '*', color='tab:red', label='ARGO-YBJ (preliminary)')

def plot_unpublished_grapes_H(ax):
    filename = '../data/unpublished_GRAPES3_H.txt'
    x, y = np.loadtxt(filename, usecols=(0,1), unpack=True, skiprows=2)
    ax.plot(x, y * np.power(x, 2.8 - 2.7), '*', color='tab:red', label='GRAPES-3 (QGSJET-II-04)')

def plot_unpublished_grapes_He(ax):
    filename = '../data/unpublished_GRAPES3_He.txt'
    x, y = np.loadtxt(filename, usecols=(0,1), unpack=True, skiprows=2)
    ax.plot(x, y * np.power(x, 2.8 - 2.7), '*', color='tab:red', label='GRAPES-3 (QGSJET-II-04)')

def plot_H():
    fig = plt.figure(figsize=(12.5,9.5))
    ax = fig.add_subplot(111)
    set_axes(ax)
    ax.set_ylim([5e3, 1e5])
    ax.set_xlim([2e2, 2e7])

    fmt = 'o'
    plot_data(ax, 'NUCLEON_H_totalEnergy.txt', 'tab:olive', fmt, 1, 'NUCLEON')
    plot_data(ax, 'AMS-02_H_rigidity.txt', 'tab:gray', fmt, 2, 'AMS-02')
    plot_data(ax, 'CREAM_III_H_totalEnergy.txt', 'tab:green', fmt, 3, 'CREAM')
    plot_data(ax, 'CALET_H_kineticEnergy.txt', 'tab:blue', fmt, 4, 'CALET')
    plot_data(ax, 'DAMPE_H_kineticEnergy.txt', 'tab:red', fmt, 5, 'DAMPE')

    fmt = 's'
    #plot_data(ax, 'TUNKA-133_H_totalEnergy.txt', 'tab:gray', 1., 'TUNKA-133 (QGSJET-01)', fmt)
    plot_data(ax, 'ICECUBE-ICETOP_SIBYLL-2.1_H_totalEnergy.txt', 'tab:olive', fmt, 1, 'ICETOP (SIBYLL-2.1)')
    plot_data(ax, 'KASCADE_2011_QGSJET-II-02_H_totalEnergy.txt', 'tab:brown', fmt, 1, 'KASCADE (QGSJET-II-02)')
    plot_data(ax, 'KASCADE_2011_SIBYLL-2.1_H_totalEnergy.txt', 'tab:cyan', fmt, 1, 'KASCADE (SIBYLL-2.1)')

    plot_unpublished_grapes_H(ax)

    ax.legend(fontsize=14)
    my_savefig(fig, 'knee_H_data')

def plot_He():
    fig = plt.figure(figsize=(12.5,9.5))
    ax = fig.add_subplot(111)
    set_axes(ax)
    ax.set_ylim([5e3, 1e5])
    ax.set_xlim([2e2, 2e7])
    
    fmt = 'o'
    plot_data(ax, 'NUCLEON_He_totalEnergy.txt', 'tab:olive', fmt, 1, 'NUCLEON')
    plot_data(ax, 'AMS-02_He_rigidity.txt', 'tab:gray', fmt, 2, 'AMS-02')
    plot_data(ax, 'CREAM_III_He_totalEnergy.txt', 'tab:green', fmt, 3, 'CREAM')
    #plot_data(ax, 'CALET_He_kineticEnergy.txt', 'tab:green', 1., 'CALET')
    plot_data(ax, 'DAMPE_He_kineticEnergy.txt', 'tab:red', fmt, 5, 'DAMPE')

    #plot_data(ax, 'ICECUBE-ICETOP_SIBYLL-2.1_He_totalEnergy.txt', 'tab:olive', 1., 'ICETOP')
    #plot_data(ax, 'KASCADE_2011_QGSJET-II-02_He_totalEnergy.txt', 'tab:olive', 1., 'ICETOP')
    #plot_data(ax, 'KASCADE_2011_SIBYLL-2.1_He_totalEnergy.txt', 'tab:olive', 1., 'ICETOP')

    plot_unpublished_grapes_He(ax)

    ax.legend(fontsize=14)
    my_savefig(fig, 'knee_He_data')

def plot_light():
    fig = plt.figure(figsize=(12.5,9.5))
    ax = fig.add_subplot(111)
    set_axes(ax)
    ax.set_ylim([5e3, 1e6])
    ax.set_xlim([2e2, 2e7])

    fmt = 's'
    plot_data(ax, 'ARGO-YBJ_light_totalEnergy.txt', 'tab:green', fmt, 1, 'ARGO-YBJ')
    plot_data(ax, 'HAWC_light_totalEnergy.txt', 'tab:red', fmt, 2, 'HAWC')

    plot_unpublished_argo(ax)

    ax.legend(fontsize=14)
    my_savefig(fig, 'knee_light_data')

if __name__== "__main__":
    plot_H()
    plot_He()
    plot_light()
