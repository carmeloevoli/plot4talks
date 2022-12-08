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
    ax.set_xlabel('E [GeV]')
    #Set y-axis
    ax.set_yscale('log')
    ax.set_ylim([5e3, 2e5])
    ax.set_ylabel(r'E$^{2.6}$ I [GeV$^{1.6}$ m$^{-2}$ s$^{-1}$ sr$^{-1}$]')

def plot_data(ax, filename, color, fmt, zorder, label, norm=1.0):
    slope = 2.6
    
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
                
def plot_unpublished_argo(ax):
    slope = 2.6
    filename = '../data/unpublished_ARGO_light.txt'
    lgEmin, lgEmax, flux, stat, syst = np.loadtxt(filename, usecols=(0,1,2,3,4), skiprows=1, unpack=True)
    x = np.sqrt(np.power(10., lgEmin) * np.power(10., lgEmax)) * 1e3
    ax.plot(x, np.power(x, slope) * flux, '*', color='tab:red', label='ARGO-YBJ (preliminary)')

def plot_unpublished_grapes_H(ax):
    filename = '../data/unpublished_GRAPES3_H.txt'
    x, y = np.loadtxt(filename, usecols=(0,1), unpack=True, skiprows=2)
    ax.plot(x, y * np.power(x, 2.8 - 2.7), '*', color='tab:red', label='GRAPES-3 (QGSJET-II-04)')

def plot_unpublished_grapes_He(ax):
    filename = '../data/unpublished_GRAPES3_He.txt'
    x, y = np.loadtxt(filename, usecols=(0,1), unpack=True, skiprows=2)
    ax.plot(x, y * np.power(x, 2.8 - 2.7), '*', color='tab:red', label='GRAPES-3 (QGSJET-II-04)')

def get_KASCADE_2005_QGSJET_light():
    filename = 'kiss_tables/KASCADE_2005_QGSJET-01_H_totalEnergy.txt'
    x_H, y_H, y_H_err = np.loadtxt(filename, usecols=(0,1,4), unpack=True, skiprows=7)
    
    filename = 'kiss_tables/KASCADE_2005_QGSJET-01_He_totalEnergy.txt'
    x_He, y_He, y_He_err = np.loadtxt(filename, usecols=(0,1,4), unpack=True, skiprows=7)

    diff = max(abs(x_H - x_He))
    assert (diff < 1e-20)
    
    return x_H, y_H + y_He, y_H_err + y_He_err

def get_KASCADE_2005_SIBYLL_light():
    filename = 'kiss_tables/KASCADE_2005_SIBYLL-2.1_H_totalEnergy.txt'
    x_H, y_H, y_H_err = np.loadtxt(filename, usecols=(0,1,4), unpack=True, skiprows=7)
    
    filename = 'kiss_tables/KASCADE_2005_SIBYLL-2.1_He_totalEnergy.txt'
    x_He, y_He, y_He_err = np.loadtxt(filename, usecols=(0,1,4), unpack=True, skiprows=7)

    diff = max(abs(x_H - x_He))
    assert (diff < 1e-20)
    
    return x_H, y_H + y_He, y_H_err + y_He_err

def get_ICETOP_light():
    filename = 'kiss_tables/ICECUBE-ICETOP_SIBYLL-2.1_H_totalEnergy.txt'
    x_H, y_H, y_H_err = np.loadtxt(filename, usecols=(0,1,4), unpack=True, skiprows=7)
    
    filename = 'kiss_tables/ICECUBE-ICETOP_SIBYLL-2.1_He_totalEnergy.txt'
    x_He, y_He, y_He_err = np.loadtxt(filename, usecols=(0,1,4), unpack=True, skiprows=7)

    diff = max(abs(x_H - x_He))
    assert (diff < 1e-20)
    
    return x_H, y_H + y_He, y_H_err + y_He_err
    
def plot_combined_light(ax):
    slope = 2.6
    
    x, y, y_err = get_KASCADE_2005_QGSJET_light()
    y = np.power(x, slope) * y
    y_err = np.power(x, slope) * y_err

    color = 'tab:brown'
    ax.errorbar(x, y, yerr=y_err, fmt='o', markeredgecolor=color, color=color,
                elinewidth=1.5, capthick=2.5, markersize=5.5, capsize=4.5, zorder=1, label='KASCADE 2005 (QGSJET-01)')

    x, y, y_err = get_KASCADE_2005_SIBYLL_light()
    y = np.power(x, slope) * y
    y_err = np.power(x, slope) * y_err

    color = 'tab:purple'
    ax.errorbar(x, y, yerr=y_err, fmt='o', markeredgecolor=color, color=color,
                elinewidth=1.5, capthick=2.5, markersize=5.5, capsize=4.5, zorder=1, label='KASCADE 2005 (SIBYLL-2.1)')

    x, y, y_err = get_ICETOP_light()
    y = np.power(x, slope) * y
    y_err = np.power(x, slope) * y_err

    color = 'tab:olive'
    ax.errorbar(x, y, yerr=y_err, fmt='o', markeredgecolor=color, color=color,
                elinewidth=1.5, capthick=2.5, markersize=5.5, capsize=4.5, zorder=1, label='ICETOP (SIBYLL-2.1)')


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
    ax.set_ylim([2e2, 2e4])
    ax.set_xlim([1e3, 1e8])

    fmt = 's'
    plot_data(ax, 'ARGO-YBJ_light_totalEnergy.txt', 'tab:green', fmt, 1, 'ARGO-YBJ')
    plot_data(ax, 'HAWC_light_totalEnergy.txt', 'tab:red', fmt, 2, 'HAWC')

    #plot_unpublished_argo(ax)

    plot_combined_light(ax)

    ax.legend(fontsize=14)
    my_savefig(fig, 'knee_light_data')

if __name__== "__main__":
    #plot_H()
    #plot_He()
    plot_light()
