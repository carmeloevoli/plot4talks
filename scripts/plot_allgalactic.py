import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np

def set_axes(ax):
    #Set x-axis
    ax.minorticks_off()
    ax.set_xscale('log')
    ax.set_xlim([1e0, 2e6])
    ax.set_xlabel('Rigidity [GV]')
    #Set y-axis
    ax.set_yscale('log')
    ax.set_ylim([1e-3, 1e4])
    ax.set_ylabel(r'R$^2$ I [GV m$^{-2}$ s$^{-1}$ sr$^{-1}$]')

def plot_data(ax, filename, color, norm, label, Z):
    E, dJdE, err_low, err_high = np.loadtxt("kiss_tables/" + filename,skiprows=7,usecols=(0,1,2,3),unpack=True)
    y = norm * np.power(E, 2.0) * dJdE
    dJdE_err = .5 * norm * (err_low + err_high)
    y_err = np.power(E, 2.0) * dJdE_err
    ax.errorbar(E, y, yerr=y_err, fmt='o', label=label, markeredgecolor=color, color=color, elinewidth=1, capthick=1, zorder=Z, markersize=5)
#    yspline = interpolate.splrep(np.log10(E), np.log10(y), s=0)
#    ynew = interpolate.splev(np.log10(10.), yspline, der=0)
#    print (filename, np.power(10., ynew))

def plot_data_from_Etot(ax, filename, color, norm, label, Z):
    E, dJdE, err_low, err_high = np.loadtxt("kiss_tables/" + filename,skiprows=7,usecols=(0,1,2,3),unpack=True)
    R = E / float(Z)
    y = norm / float(Z) * np.power(E, 2.0) * dJdE
    dJdE_err = .5 * norm * (err_low + err_high) / float(Z)
    y_err = np.power(E, 2.0) * dJdE_err
    ax.errorbar(R, y, yerr=y_err, fmt='o', label=label, markeredgecolor=color, color=color, elinewidth=1, capthick=1, zorder=Z, markersize=5)

def yCR(i):
    return 2e3 * np.power(0.45, i)

def get_color(Z):
    if Z == 'H':
        return 'tab:blue'
    elif Z == 'He':
        return 'tab:orange'
    elif Z == 'Li':
        return 'tab:green'
    elif Z == 'Be':
        return 'tab:red'
    elif Z == 'B':
        return 'tab:purple'
    elif Z == 'C':
        return 'tab:brown'
    elif Z == 'N':
        return 'tab:pink'
    elif Z == 'O':
        return 'tomato'
    elif Z == 'F':
        return 'tab:olive'
    elif Z == 'Ne':
        return 'tab:cyan'
    elif Z == 'Na':
        return 'navy'
    elif Z == 'Mg':
        return 'darkorange'
    elif Z == 'Al' :
        return 'seagreen'
    elif Z == 'Si':
        return 'salmon'
    elif Z == 'Fe':
        return 'tab:gray'
    elif Z == 'Ni':
        return 'indigo'
    else:
        return 'Something is wrong'

def plot_allgalactic():
    fig = plt.figure(figsize=(12.5, 9.5))
    ax = fig.add_subplot(111)
    set_axes(ax)

    ### AMS-02 ###
    plot_data(ax, 'AMS-02_H_rigidity.txt', get_color('H'), 1., 'H', 1)
    plot_data(ax, 'AMS-02_He_rigidity.txt', get_color('He'), 1., 'He', 2)
    plot_data(ax, 'AMS-02_Li_rigidity.txt', get_color('Li'), 1., 'Li', 3)
    plot_data(ax, 'AMS-02_Be_rigidity.txt', get_color('Be'), 1., 'Be', 4)
    plot_data(ax, 'AMS-02_B_rigidity.txt', get_color('B'), 1., 'B', 5)
    plot_data(ax, 'AMS-02_C_rigidity.txt', get_color('C'), 1., 'C', 6)
    plot_data(ax, 'AMS-02_N_rigidity.txt', get_color('N'), 1., 'N', 7)
    plot_data(ax, 'AMS-02_O_rigidity.txt', get_color('O'), 1., 'O', 8)
    plot_data(ax, 'AMS-02_F_rigidity.txt', get_color('F'), 1., 'F', 9)
    plot_data(ax, 'AMS-02_Ne_rigidity.txt', get_color('Ne'), 1., 'Ne', 10)
    plot_data(ax, 'AMS-02_Na_rigidity.txt', get_color('Na'), 1., 'Na', 11)
    plot_data(ax, 'AMS-02_Mg_rigidity.txt', get_color('Mg'), 1., 'Mg', 12)
    plot_data(ax, 'AMS-02_Al_rigidity.txt', get_color('Al'), 1., 'Al', 13)
    plot_data(ax, 'AMS-02_Si_rigidity.txt', get_color('Si'), 1., 'Si', 14)
    plot_data(ax, 'AMS-02_Fe_rigidity.txt', get_color('Fe'), 1., 'Fe', 26)

    ### CREAM ###
    plot_data_from_Etot(ax, 'CREAM_III_H_totalEnergy.txt', get_color('H'), 1., 'H', 1)
    plot_data_from_Etot(ax, 'CREAM_III_He_totalEnergy.txt', get_color('He'), 1., 'He', 2)
#    # Li
#    # Be
#    # B
    plot_data_from_Etot(ax, 'CREAM_II_C_totalEnergy.txt', get_color('C'), 1., 'C', 6)
#    # N
    plot_data_from_Etot(ax, 'CREAM_II_O_totalEnergy.txt', get_color('O'), 1., 'O', 8)
#    # F
    plot_data_from_Etot(ax, 'CREAM_II_Ne_totalEnergy.txt', get_color('Ne'), 1., 'Ne', 10)
    plot_data_from_Etot(ax, 'CREAM_II_Mg_totalEnergy.txt', get_color('Mg'), 1., 'Mg', 12)
    plot_data_from_Etot(ax, 'CREAM_II_Si_totalEnergy.txt', get_color('Si'), 1., 'Si', 14)
    plot_data_from_Etot(ax, 'CREAM_II_Fe_totalEnergy.txt', get_color('Fe'), 1., 'Fe', 26)

    ### CALET ###
    plot_data_from_Etot(ax, 'CALET_H_kineticEnergy.txt', get_color('H'), 1., 'H', 1)
#    plot_data_from_Etot(ax, 'C_CALET_Etot.txt', 'tab:brown', 1., 'C', 6)
#    plot_data_from_Etot(ax, 'O_CALET_Etot.txt', 'tab:olive', 1., 'O', 8)
    plot_data_from_Etot(ax, 'CALET_Ni_kineticEnergy.txt', get_color('Ni'), 1., 'Ni', 1)

    ### NUCLEON ###
    plot_data_from_Etot(ax, 'NUCLEON_H_totalEnergy.txt', get_color('H'), 1., 'H', 1)
    plot_data_from_Etot(ax, 'NUCLEON_He_totalEnergy.txt', get_color('He'), 1., 'He', 2)

    ### DAMPE ###
    plot_data(ax, 'DAMPE_H_kineticEnergy.txt', get_color('H'), 1., get_color('H'), 1)

    fontsize=20
    ax.text(7e5, yCR(0.),  'H',  color=get_color('H'),  fontsize=fontsize)
    ax.text(7e5, yCR(1.),  'He', color=get_color('He'), fontsize=fontsize)
    ax.text(7e5, yCR(2.),  'Li', color=get_color('Li'), fontsize=fontsize)
    ax.text(7e5, yCR(3.),  'Be', color=get_color('Be'), fontsize=fontsize)
    ax.text(7e5, yCR(4.),  'B',  color=get_color('B'),  fontsize=fontsize)
    ax.text(7e5, yCR(5.),  'C',  color=get_color('C'),  fontsize=fontsize)
    ax.text(7e5, yCR(6.),  'N',  color=get_color('N'),  fontsize=fontsize)
    ax.text(7e5, yCR(7.),  'O',  color=get_color('O'),  fontsize=fontsize)
    ax.text(7e5, yCR(8.),  'F',  color=get_color('F'),  fontsize=fontsize)
    ax.text(7e5, yCR(9.),  'Ne', color=get_color('Ne'), fontsize=fontsize)
    ax.text(7e5, yCR(10.), 'Na', color=get_color('Na'), fontsize=fontsize)
    ax.text(7e5, yCR(11.), 'Mg', color=get_color('Mg'), fontsize=fontsize)
    ax.text(7e5, yCR(12.), 'Al', color=get_color('Al'), fontsize=fontsize)
    ax.text(7e5, yCR(13.), 'Si', color=get_color('Si'), fontsize=fontsize)
    ax.text(7e5, yCR(14.), 'Fe', color=get_color('Fe'), fontsize=fontsize)
    ax.text(7e5, yCR(15.), 'Ni', color=get_color('Ni'), fontsize=fontsize)

    ax.text(2, 1.3e4, 'Credits: AMS-02, CALET, CREAM, DAMPE, NUCLEON', fontsize=15)
##    plot_data_from_Etot(ax, 'C_PAMELA_Etot.txt', 'tab:blue', 1e-5, 'CALET', 6.0)
##    plot_data(ax, 'H_NUCLEON_Etot.txt', 'tab:red', 1., 'CREAM')
##    plot_data(ax, 'H_ICECUBE-ICETOP_Etot.txt', 'tab:red', 1., 'CREAM')
##    plot_data(ax, 'H_KASCADEGrande_SIBYLL-2.3_Etot.txt', 'y', 1., 'KG')
    
    plt.savefig('allgalactic.pdf')

if __name__== "__main__":
    plot_allgalactic()
