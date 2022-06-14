import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np
import math

def lambda_A(A):
    mbarn = 1e-27 # cm2
    proton_mass = 1.6726219e-24 # g
    sigma = 45. * mbarn * np.power(A, 0.7) # cm2
    mass = 1.4 * proton_mass # g
    return mass / sigma
    
def P_BC():
    mbarn = 1e-27 # cm2
    proton_mass = 1.6726219e-24 # g
    A = 12.0 # 0
    sigma = 45. * mbarn * np.power(A, 0.7) # cm2
    sigma_B = 15. + 25. + 25. # B10 + B11 + C11
    sigma_B *= mbarn
    return (sigma_B / sigma)
    
def find_nearest(array, value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return idx-1
    else:
        return idx
    
def plot_ratio(ax, color, lambda_s, lambda_p, P):
    X = np.linspace(0, 20, 2000)
    r = P * lambda_s / (lambda_s - lambda_p) * (np.exp(-X / lambda_s + X / lambda_p) - 1.0)
    ax.plot(X, r, color=color, zorder=1, lw=5)

def compute_grammage(r, lambda_s, lambda_p, P):
    X = 1e-1
    r_found = 0.0
    while (r_found < r):
        r_found = P * lambda_s / (lambda_s - lambda_p) * (np.exp(-X / lambda_s + X / lambda_p) - 1.0)
        X *= 1.004
    return X

def plot_data_ratio(ax, T_plot, filename, color, label):
    filename = 'kiss_tables/' + filename
    T, y, err_y_lo, err_y_up = np.loadtxt(filename, skiprows=8, usecols=(0,1,2,3), unpack=True)

    assert(T_plot > T[0] and T_plot < T[-1])

    i = find_nearest(T, T_plot)
    yerr = np.sqrt(err_y_lo[i] * err_y_up[i])
    y = y[i]
    
    X = compute_grammage(y, lambda_A(10.), lambda_A(12.), P_BC())
    ax.errorbar(X, y, yerr=yerr, fmt='o', markersize=8, elinewidth=2, capsize=4, capthick=2,
                markeredgecolor=color, color=color, zorder=3)
    
    ax.text(X,y + 0.025,label,color=color,fontsize=20,horizontalalignment='center', verticalalignment='baseline')

def plot_grammage():
    fig = plt.figure(figsize=(11.5, 8.5))
    ax = fig.add_subplot(111)

    ax.set_ylabel(r'secondary / primary')
    ax.set_ylim([0,0.7])
    ax.set_xlabel(r'grammage [g/cm$^2$]')
    ax.set_xlim([0,20])
    
    plot_ratio(ax, 'tab:orange', lambda_A(10.), lambda_A(12.), P_BC())

    ax.plot([0,100],[0.3,0.3],'--',color='tab:blue', linewidth=5)
    ax.text(14.5, 0.26, 'B/C at 10 GV', color='tab:blue', fontsize=22)

#    plot_data_ratio(ax, 10.0, 'AMS-02_B_C_rigidity.txt', 'tab:blue', '10 GV')
#    plot_data_ratio(ax, 30.0, 'AMS-02_B_C_rigidity.txt', 'tab:blue', '30 GV')
#    plot_data_ratio(ax, 100.0, 'AMS-02_B_C_rigidity.txt', 'tab:blue', '100 GV')
#    plot_data_ratio(ax, 1000.0, 'AMS-02_B_C_rigidity.txt', 'tab:blue', '1 TV')
      
    ax.text(1., 0.60, r'$\lambda_B = 10.4$ g/cm$^2$', fontsize=24)
    ax.text(1., 0.55, r'$\lambda_C = 9.1$ g/cm$^2$', fontsize=24)
    ax.text(1., 0.50, r'$P_{C \rightarrow B} = 0.25$', fontsize=24)

#    color = 'tab:blue'
#    ax.errorbar(-1,-1,-1, label='AMS-02', fmt='o', markersize=8, elinewidth=2, capsize=4, capthick=2,
#                markeredgecolor=color, color=color, zorder=3)
#    ax.legend(loc='lower right')
    plt.savefig('grammage_simple.pdf')

def plot_diffusion():
    fig = plt.figure(figsize=(11.5, 8.5))
    ax = fig.add_subplot(111)

    ax.set_ylabel(r'intensity')
    ax.set_ylim([1e-2,2])
    ax.set_yscale('log')
    ax.set_xlabel(r'energy')
    ax.set_xlim([1,1e3])
    ax.set_xscale('log')

    T = np.logspace(0, 3, 100)

    ax.plot([10.,10.], [np.power(10. / T[0], -0.2), np.power(10. / T[0], -0.66)], color='tab:orange', linestyle=':', lw=2)
    ax.text(10., .80, 'slow escape', color='tab:orange', fontsize=18, ha='center', va='center')

    ax.plot([500.,500.], [np.power(500. / T[0], -0.2), np.power(500. / T[0], -0.66)], color='tab:orange', linestyle=':', lw=2)
    ax.text(500., .35, 'fast escape', color='tab:orange', fontsize=18, ha='center', va='center')

    ax.plot(T, np.power(T / T[0], -0.2), color='tab:red', label='injection')
    ax.plot(T, np.power(T / T[0], -0.66), color='tab:blue', label='measured')

    ax.text(70, 0.25, r'$E^{-\gamma}$', color='tab:red', fontsize=33)
    ax.text(70, 0.02, r'$E^{-\gamma-\delta}$', color='tab:blue', fontsize=33)
    
    ax.legend()
    plt.savefig('diffusion_simple.pdf')

def plot_losses():
    fig = plt.figure(figsize=(11.5, 8.5))
    ax = fig.add_subplot(111)

    ax.set_ylabel(r'intensity')
    ax.set_ylim([1e-2,2])
    ax.set_yscale('log')
    ax.set_xlabel(r'energy')
    ax.set_xlim([1e1,1e4])
    ax.set_xscale('log')

    T = np.logspace(1, 4, 100)

    #ax.plot([10.,10.], [np.power(10. / T[0], -0.2), np.power(10. / T[0], -0.66)], color='tab:orange', linestyle=':', lw=2)
    #ax.text(10., .80, 'slow escape', color='tab:orange', fontsize=18, ha='center', va='center')

    #ax.plot([500.,500.], [np.power(500. / T[0], -0.2), np.power(500. / T[0], -0.66)], color='tab:orange', linestyle=':', lw=2)
    #ax.text(500., .35, 'fast escape', color='tab:orange', fontsize=18, ha='center', va='center')

    x = T / 10.
    ax.plot(T, np.power(x, -0.2), color='tab:red', label='injection')
    ax.plot(T, np.power(x, -0.66) * np.power(1. + np.power(T / 1e3, 15.), -0.35 / 15.), color='tab:blue', label='measured')

    ax.text(70, 0.85, r'$E^{-\gamma}$', color='tab:red', fontsize=33)
    ax.text(70, 0.30, r'$E^{-\gamma-\delta}$', color='tab:blue', fontsize=33)
    ax.text(2.0e3, 3e-2, r'$E^{-\gamma-\frac{1+\delta}{2}}$', color='tab:blue', fontsize=33)

    ax.legend()
    plt.savefig('losses_simple.pdf')
    
if __name__== "__main__":
    print (f'{lambda_A(10.):5.1f} {lambda_A(12.):5.1f} {P_BC():5.2f}')
    #plot_grammage()
    #plot_diffusion()
    plot_losses()
