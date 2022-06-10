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

#def plot_data(ax, filename, slope, color, label, fmt, norm, zorder):
#    filename = 'kiss_tables/' + filename
#    T, y, err_y_lo, err_y_up = np.loadtxt(filename, skiprows=7, usecols=(0,1,2,3), unpack=True)
#    y_err = [np.power(T, slope) * norm * err_y_lo, np.power(T, slope) * norm * err_y_up]
#    y_plot = np.power(T, slope) * norm * y
#    x_plot = T
#
#    counter = 0
#    sum = 0.
#    for x,y in zip(x_plot, y_plot):
#        if (50. < x < 100.):
#            sum += y
#            counter += 1
#    norm = sum / counter
#    print (norm)
#    ax.errorbar(x_plot, y_plot / norm, yerr=y_err, fmt=fmt, markersize=8, elinewidth=2, markeredgecolor=color, capsize=4, capthick=2, color=color, label=label, zorder=zorder)
#
#def spallation(A): # gr cm^-2
#    m_p = 1.6726219e-24
#    sigma = 40. * 1e-27 * A**0.7
#    return m_p / sigma
#
#def grammage(Chi_0, R):
#    s = 0.02
#    delta = 0.7
#    delta_delta = delta - 1./3.
#    return Chi_0 * (R / 10.)**(-delta) * (1. + (R / 260.)**(delta_delta / s))**s
#
#def compute_model(CO_fraction, Chi_0):
#    R = np.logspace(1, 4, 100)
#    return R, CO_fraction * (1. + grammage(Chi_0, R) / spallation(16.)) / (1. + grammage(Chi_0, R) / spallation(12.))

def set_axes(ax):
    ax.set_xscale('log')
    ax.set_xlim([2e1,1e3])
    ax.set_xlabel('R [GV]')
    #ax.set_yscale('log')
    ax.set_ylim([0.06,0.3])
    ax.set_ylabel('secondary/primary')

def plot_BC():
    fig = plt.figure(figsize=(11.5, 8))
    ax = fig.add_subplot(111)
    set_axes(ax)
    ax.set_ylim([0.05,0.3])
    ax.set_xlim([1e1, 1e3])
    plot_data(ax, 'AMS-02_Be_C_rigidity.txt', 0., 'tab:orange', 'Be/C (x 2.7)', 'o', 2.7)
    plot_data(ax, 'AMS-02_Li_C_rigidity.txt', 0., 'tab:green', 'Li/C (x 1.4)', 'o', 1.4)
    plot_data(ax, 'AMS-02_B_C_rigidity.txt', 0., 'tab:red', 'B/C', 'o', 1)

    ax.text(14., 0.07, 'data from AMS-02', fontsize=20)

    ax.legend(fontsize=22)
    plt.savefig('LiBeB_C_AMS02.pdf')

def plot_BC_scaled():
    fig = plt.figure(figsize=(11.5, 8))
    ax = fig.add_subplot(111)

    plot_data(ax, 'AMS-02_Li_C_rigidity.txt', 0.41, 'tab:blue', 'Li/C', 'o', 1.65)
    plot_data(ax, 'AMS-02_Li_O_rigidity.txt', 0.41, 'tab:green', 'Li/O', 'o', 1.73)
    plot_data(ax, 'AMS-02_B_C_rigidity.txt', 0.41, 'tab:red', 'B/C', 'o', 1.17)
    plot_data(ax, 'AMS-02_B_O_rigidity.txt', 0.41, 'tab:orange', 'B/O', 'o', 1.24)

    ax.set_xscale('log')
    #ax.set_yscale('log')
    ax.set_xlim([3e1,2e3])
    ax.set_ylim([0.80,1.80])

    R = np.logspace(0, 4, 100)
    ax.plot(R, R / R, '--', color='k', lw=2)

    #BC_0 = 10. * (70. * 1e-27) / (1.4 * 1.67262158e-24)
    #ax.text(15, 0.07, 'AMS-02', fontsize=30, color='k')

    ax.legend(fontsize=22)

    ax.set_xlabel('R [GV]', fontsize=26, labelpad=10)
    ax.set_ylabel(r'$R^{0.4}$ (secondary / primary)', fontsize=26, labelpad=10)

    plt.savefig('LiBeB_C_scaled.pdf',format='pdf',dpi=300)

def plot_FeO():
    fig = plt.figure(figsize=(10.5, 8))
    ax = fig.add_subplot(111)
    set_axes(ax)
    ax.set_ylim([0.1,0.2])

    plot_data(ax, 'AMS-02_Fe_O_rigidity.txt', 0., 'tab:red', 'Fe/O', 'o', 1)

    ax.legend(fontsize=26)
    plt.savefig('Fe_O_AMS02.pdf')

if __name__== "__main__":
    plot_BC()
    plot_BC_scaled()
#    plot_FeO()
