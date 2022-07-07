import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np

def plot_data(ax, filename, slope, color, label, norm):
    T, y, err_y_lo, err_y_up = np.loadtxt(filename, skiprows=8, usecols=(0,1,2,3), unpack=True)
    y_err = [norm * np.power(T, slope) * err_y_lo, norm * np.power(T, slope) * err_y_up]
    y_plot = np.power(T, slope) * norm * y
    x_plot = T
    ax.errorbar(x_plot, y_plot, yerr=y_err, fmt='o', markersize=7, elinewidth=2, capsize=4, capthick=2, zorder=1,
                markeredgecolor=color, color=color, label=label)

def set_axes(ax):
    ax.set_xscale('log')
    #ax.set_yscale('log')
    ax.set_xlim([10, 2e3])
    ax.set_xlabel('E [GeV]')
    ax.set_ylim([40., 250.])
    ax.set_ylabel(r'E$^{3}$ I  [GeV$^2$ m$^{-2}$ s$^{-1}$ sr$^{-1}$]')

def plot_fluxes():
    fig = plt.figure(figsize=(8.8, 7.2))
    ax = fig.add_subplot(111)
    set_axes(ax)

    plot_data(ax, 'kiss_tables/AMS-02_e+_kineticEnergy.txt', 3.0, 'tab:green', r'positrons (x10)', 10.)
    plot_data(ax, 'kiss_tables/AMS-02_e-_kineticEnergy.txt', 3.0, 'tab:red', r'electrons', 1.)
    
    ax.legend(loc='best', fontsize=22)
    plt.savefig('AMS-02_leptons.pdf')

def plot_total():
    fig = plt.figure(figsize=(8.8, 7.2))
    ax = fig.add_subplot(111)
    set_axes(ax)
    ax.set_ylim([7., 300.])
    ax.set_xlim([1e1, 1e4])
    ax.set_yscale('log')

    plot_data(ax, 'kiss_tables/VERITAS_e+e-_totalEnergy.txt', 3.0, 'tab:orange', r'VERITAS', 1.)
    plot_data(ax, 'kiss_tables/HESS_e+e-_totalEnergy.txt', 3.0, 'tab:brown', r'HESS', 1.)
    plot_data(ax, 'kiss_tables/AMS-02_e+e-_kineticEnergy.txt', 3.0, 'tab:green', r'AMS-02', 1.)
    plot_data(ax, 'kiss_tables/CALET_e+e-_kineticEnergy.txt', 3.0, 'tab:red', r'CALET', 1.)
    plot_data(ax, 'kiss_tables/DAMPE_e+e-_kineticEnergy.txt', 3.0, 'tab:blue', r'DAMPE', 1.)

    ax.fill_between([1e1,1e3], [300,300], 7, color='gray', alpha=0.2)

    ax.text(1.6e3, 200., r'e$^+$+e$^-$')

    ax.legend(loc='best', fontsize=22)
    plt.savefig('all_leptons.pdf')

if __name__== "__main__":
    plot_fluxes()
    plot_total()
