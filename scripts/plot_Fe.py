import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np
import math

def plot_data(ax, filename, slope, color, label, fmt, norm):
    filename = 'kiss_tables/' + filename
    T, y, err_y_lo, err_y_up = np.loadtxt(filename, skiprows=7, usecols=(0,1,2,3), unpack=True)
    y *= norm
    err_y_lo *= norm
    err_y_up *= norm
    y_err = [np.power(T, slope) * err_y_lo, np.power(T, slope) * err_y_up]
    y_plot = np.power(T, slope) * y
    x_plot = T
    ax.errorbar(x_plot, y_plot, yerr=y_err,
                fmt=fmt, markersize=7, elinewidth=2, markeredgecolor=color, capsize=4, capthick=2,
                color=color, label=label, zorder=1)

def set_axes(ax):
    ax.set_xscale('log')
    ax.set_xlim([2e1,3e3])
    ax.set_xlabel('R [GV]')
    #ax.set_yscale('log')
    ax.set_ylim([50.,125.])
    ax.set_ylabel('R$^{2.7}$ Intensity')

def plot_FeO():
    fig = plt.figure(figsize=(8.5, 8.))
    ax = fig.add_subplot(111)
    set_axes(ax)

    plot_data(ax, 'AMS-02_O_rigidity.txt', 2.7, 'tab:red', 'O', 'o', 1)
    plot_data(ax, 'AMS-02_Fe_rigidity.txt', 2.7, 'tab:blue', 'Fe [x6]', 'o', 6.)

    ax.legend(fontsize=26)
    plt.savefig('Fe_O_AMS02.pdf')

if __name__== "__main__":
    plot_FeO()
