import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('./review.mplstyle')
import numpy as np

from scipy.interpolate import CubicSpline

def MySaveFig(fig, pltname):
    filename = pltname + '.pdf'
    print ("Saving plot as " + filename)
    fig.savefig(filename)
    
def SetAxes(ax):
    #Set x-axis
    ax.minorticks_off()
    ax.set_xscale('log')
    ax.set_xlim([1e1, 1e5])
    ax.set_xlabel('Energy [GeV]')
    #Set y-axis
    ax.set_yscale('log')
    #ax.set_ylim([1e5, 1e7])
    ax.set_ylabel(r'E$^{2.7}$ Flux [GeV$^{1.7}$/m$^2$ s sr]')
  
def plot_data_shifted(ax, filename, fmt, color, label, Z, A):
    R, dJdR, dJdR_errLo, dJdR_errUp = np.loadtxt(filename,skiprows=7,usecols=(0,1,2,3),unpack=True)
    P = R * Z
    M = A * 0.938
    E = np.sqrt(M * M + P * P)
    Z2 = Z * Z
    dRdE = E / Z2 / R
    dJdE = dJdR * dRdE
    dJdE_errLo = dJdR_errLo * dRdE
    dJdE_errUp = dJdR_errUp * dRdE
    y = np.power(E, 2.7) * dJdE
    y_err = np.power(E, 2.7) * [dJdE_errLo, dJdE_errUp]
    ax.errorbar(E, y, yerr=y_err, fmt=fmt, markeredgecolor=color, color=color, elinewidth=2, capthick=2, label=label, zorder=3)
    return CubicSpline(np.log10(E), np.log10(y), extrapolate=False)
        
### PLOT ROUTINES ###
def plot_allparticle():
    fig = plt.figure(figsize=(13.5,8.5))
    ax = fig.add_subplot(111)
    SetAxes(ax)

    H = plot_data_shifted(ax, 'kiss_tables/AMS-02_H_rigidity.txt', 'o', 'tab:blue', 'H', 1, 1)
    He = plot_data_shifted(ax, 'kiss_tables/AMS-02_He_rigidity.txt', 'o', 'tab:orange', 'He', 2, 4)
    Li = plot_data_shifted(ax, 'kiss_tables/AMS-02_Li_rigidity.txt', 'o', 'tab:green', 'Li', 3, 6)
    Be = plot_data_shifted(ax, 'kiss_tables/AMS-02_Be_rigidity.txt', 'o', 'tab:red', 'Be', 4, 8)
    B = plot_data_shifted(ax, 'kiss_tables/AMS-02_B_rigidity.txt', 'o', 'tab:purple', 'B', 5, 10)
    C = plot_data_shifted(ax, 'kiss_tables/AMS-02_C_rigidity.txt', 'o', 'tab:brown', 'C', 6, 12)
    N = plot_data_shifted(ax, 'kiss_tables/AMS-02_N_rigidity.txt', 'o', 'tab:pink', 'N', 7, 14)
    O = plot_data_shifted(ax, 'kiss_tables/AMS-02_O_rigidity.txt', 'o', 'tab:gray', 'O', 8, 16)
    F = plot_data_shifted(ax, 'kiss_tables/AMS-02_F_rigidity.txt', 'o', 'tab:olive', 'F', 9, 18)
    Ne = plot_data_shifted(ax, 'kiss_tables/AMS-02_Ne_rigidity.txt', 'o', 'tab:cyan', 'Ne', 10, 20)
    Na = plot_data_shifted(ax, 'kiss_tables/AMS-02_Na_rigidity.txt', '*', 'tab:blue', 'Na', 11, 22)
    Mg = plot_data_shifted(ax, 'kiss_tables/AMS-02_Mg_rigidity.txt', '*', 'tab:orange', 'Mg', 12, 24)
    Al = plot_data_shifted(ax, 'kiss_tables/AMS-02_Al_rigidity.txt', '*', 'tab:green', 'Al', 13, 26)
    Si = plot_data_shifted(ax, 'kiss_tables/AMS-02_Si_rigidity.txt', '*', 'tab:red', 'Si', 14, 28)
    S = plot_data_shifted(ax, 'kiss_tables/AMS-02_S_rigidity.txt', '*', 'tab:purple', 'S', 15, 30)
    Fe = plot_data_shifted(ax, 'kiss_tables/AMS-02_Fe_rigidity.txt', '*', 'tab:cyan', 'Fe', 26, 56)

    species = [H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, S, Fe]
    E = np.logspace(1, 7, 1000)
    flux = []
    for E_i in E:
        value = 0.
        for s in species:
            value_interpolated = np.power(10., s(np.log10(E_i)))
            if value_interpolated > 0.:
                value += value_interpolated
        flux.append(value)
    
    ax.plot(E, flux)
      
    ax.legend(fontsize=12)
    MySaveFig(fig, 'allparticle_ams02')

### MAiN ###
if __name__== "__main__":
    plot_allparticle()
