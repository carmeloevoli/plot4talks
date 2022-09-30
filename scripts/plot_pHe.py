import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np
import math

def plot_data(ax, filename, slope, color, label, fmt, norm, zorder=3):
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
                color=color, label=label, zorder=zorder)

def plot_data_from_Etot(ax, filename, Z, slope, color, label, fmt, norm, zorder=3):
    filename = 'kiss_tables/' + filename
    T, y, err_y_lo, err_y_up = np.loadtxt(filename, skiprows=7, usecols=(0,1,2,3), unpack=True)
    T = T / float(Z)
    y = norm * y * float(Z)
    err_y_lo *= norm * float(Z)
    err_y_up *= norm * float(Z)
    y_err = [np.power(T, slope) * err_y_lo, np.power(T, slope) * err_y_up]
    y_plot = np.power(T, slope) * y
    x_plot = T
    ax.errorbar(x_plot, y_plot, yerr=y_err,
                fmt=fmt, markersize=7, elinewidth=2, markeredgecolor=color, capsize=4, capthick=2,
                color=color, label=label, zorder=zorder)

def set_axes(ax):
    ax.set_xscale('log')
    ax.set_xlim([5e1,1e6])
    ax.set_xlabel('R [GV]')
    #ax.set_yscale('log')
    ax.set_ylim([3e3,2.2e4])
    ax.set_ylabel('R$^{2.7}$ I [GV$^{1.7}$ m$^{-2}$ s$^{-1}$ sr$^{-1}$]')

def plot_H():
    fig = plt.figure(figsize=(10., 8.))
    ax = fig.add_subplot(111)
    set_axes(ax)
    
    plot_data(ax, 'NUCLEON_H_totalEnergy.txt', 2.7, 'darkgray', 'NUCLEON', 'o', 1., 1)
    plot_data(ax, 'AMS-02_H_rigidity.txt', 2.7, 'tab:red', 'AMS-02', 'o', 1.)
    plot_data(ax, 'PAMELA_H_rigidity.txt', 2.7, 'tab:purple', 'PAMELA', 'o', 1.)
    plot_data(ax, 'CREAM_III_H_totalEnergy.txt', 2.7, 'tab:orange', 'CREAM-III', 'o', 1.)
    #plot_data(ax, 'BESS-TeV_H_totalEnergy.txt', 2.7, 'tab:olive', 'BESS-TeV', 'o', 1., 1)
    plot_data(ax, 'CALET_H_kineticEnergy.txt', 2.7, 'tab:brown', 'CALET', 'o', 1.)
    plot_data(ax, 'DAMPE_H_kineticEnergy.txt', 2.7, 'tab:blue', 'DAMPE', 'o', 1.)

    ax.text(2e2, 5e3, 'H', fontsize=26)

    ax.legend(fontsize=18)
    plt.savefig('H_highenergy.pdf')

def plot_He():
    fig = plt.figure(figsize=(10., 8.))
    ax = fig.add_subplot(111)
    set_axes(ax)
    ax.set_ylim([1e3,7e3])

    plot_data_from_Etot(ax, 'NUCLEON_He_totalEnergy.txt', 2, 2.7, 'darkgray', 'NUCLEON', 'o', 1., 1)
    plot_data(ax, 'AMS-02_He_rigidity.txt', 2.7, 'tab:red', 'AMS-02', 'o', 1.)
    plot_data(ax, 'PAMELA_He_rigidity.txt', 2.7, 'tab:purple', 'PAMELA', 'o', 1.)
    plot_data_from_Etot(ax, 'CREAM_III_He_totalEnergy.txt', 2, 2.7, 'tab:orange', 'CREAM-III', 'o', 1.)
    #plot_data_from_Etot(ax, 'BESS-TeV_He_totalEnergy.txt', 2, 2.7, 'tab:olive', 'BESS-TeV', 'o', 1., 1)
    #plot_data(ax, 'CALET_He_kineticEnergy.txt', 2.7, 'tab:brown', 'CALET', 'o', 1.)
    plot_data_from_Etot(ax, 'DAMPE_He_totalEnergy.txt', 2, 2.7, 'tab:blue', 'DAMPE', 'o', 1.)

    ax.text(2e2, 1.5e3, 'He', fontsize=26)

    ax.legend(fontsize=18)
    plt.savefig('He_highenergy.pdf')

def plot_p_and_He():
    fig = plt.figure(figsize=(12., 8.))
    ax = fig.add_subplot(111)
    set_axes(ax)
    ax.set_xlim([1e2,1e6])
    ax.set_ylim([8e3,1e6])
    ax.set_ylabel('R$^3$ I [GV$^2$ m$^{-2}$ s$^{-1}$ sr$^{-1}$]')
    ax.set_yscale('log')
    
    plot_data(ax, 'NUCLEON_H_totalEnergy.txt', 3.0, 'darkgray', 'NUCLEON', 'o', 1., 1)
    plot_data(ax, 'AMS-02_H_rigidity.txt', 3.0, 'tab:red', 'AMS-02', 'o', 1.)
    plot_data(ax, 'PAMELA_H_rigidity.txt', 3.0, 'tab:purple', 'PAMELA', 'o', 1.)
    plot_data(ax, 'CREAM_III_H_totalEnergy.txt', 3.0, 'tab:orange', 'CREAM-III', 'o', 1.)
    #plot_data(ax, 'BESS-TeV_H_totalEnergy.txt', 2.7, 'tab:olive', 'BESS-TeV', 'o', 1., 1)
    plot_data(ax, 'CALET_H_kineticEnergy.txt', 3.0, 'tab:brown', 'CALET', 'o', 1.)
    plot_data(ax, 'DAMPE_H_kineticEnergy.txt', 3.0, 'tab:blue', 'DAMPE', 'o', 1.)
    
    ax.legend(fontsize=16)

    plot_data_from_Etot(ax, 'NUCLEON_He_totalEnergy.txt', 2, 3.0, 'darkgray', 'NUCLEON', 'v', 1., 1)
    plot_data(ax, 'AMS-02_He_rigidity.txt', 3.0, 'tab:red', 'AMS-02', 'v', 1.)
    plot_data(ax, 'PAMELA_He_rigidity.txt', 3.0, 'tab:purple', 'PAMELA', 'v', 1.)
    plot_data_from_Etot(ax, 'CREAM_III_He_totalEnergy.txt', 2, 3.0, 'tab:orange', 'CREAM-III', 'v', 1.)
    #plot_data_from_Etot(ax, 'BESS-TeV_He_totalEnergy.txt', 2, 2.7, 'tab:olive', 'BESS-TeV', 'o', 1., 1)
    #plot_data(ax, 'CALET_He_kineticEnergy.txt', 2.7, 'tab:brown', 'CALET', 'o', 1.)
    plot_data_from_Etot(ax, 'DAMPE_He_totalEnergy.txt', 2, 3.0, 'tab:blue', 'DAMPE', 'v', 1.)

    plt.savefig('H_and_He_highenergy.pdf')
    
def plot_pHe_ratio():
    fig = plt.figure(figsize=(10., 8.))
    ax = fig.add_subplot(111)
    set_axes(ax)
    ax.set_ylim([3,5])

    plot_data(ax, 'AMS-02_H_He_rigidity.txt', 0., 'tab:red', 'AMS-02', 'o', 1.)

    ax.legend(fontsize=18)
    plt.savefig('pHe_ratio.pdf')

if __name__== "__main__":
    #plot_pHe_ratio()
    plot_H()
    plot_He()
    plot_p_and_He()
