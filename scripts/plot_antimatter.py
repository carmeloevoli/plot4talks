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
    ax.set_xlim([30, 3e3])
    ax.set_xlabel('T [GeV]')
    ax.set_ylim([0., 30.])
    ax.set_ylabel(r'T$^{2.8}$ I')

def plot_antimatter():
    fig = plt.figure(figsize=(10.5, 8))
    ax = fig.add_subplot(111)
    set_axes(ax)

    plot_data(ax, 'kiss_tables/AMS-02_H_rigidity.txt', 2.8, 'tab:red', r'$p$ [$\times 10^{-3}$]', 1e-3)
    #plot_data(ax, 'kiss_tables/AMS-02_He_rigidity.txt', 2.8, 'tab:orange', r'$p$ [$\times 10^{-3}$]', 1e-3)
    plot_data(ax, 'kiss_tables/AMS-02_e+_kineticEnergy.txt', 2.8, 'tab:green', r'$e^+$ [$\times 2.7$]', 2.7)
    plot_data(ax, 'kiss_tables/AMS-02_pbar_rigidity.txt', 2.8, 'tab:blue', r'$\bar p$ [$\times 5.4$]', 5.4)
    
    ax.text(1.2e3, 2, 'AMS-02', fontsize=22)
    
    ax.legend(loc='lower left', fontsize=22)
    plt.savefig('AMS-02_antimatter.pdf')

if __name__== "__main__":
    plot_antimatter()
