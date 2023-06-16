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
    ax.plot(T, np.power(T / T[0], -0.66), color='tab:blue', label='after propagation')

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
    ax.plot(T, np.power(x, -0.66) * np.power(1. + np.power(T / 1e3, 15.), -0.35 / 15.), color='tab:blue', label='after propagation')

    ax.text(70, 0.85, r'$E^{-\gamma}$', color='tab:red', fontsize=33)
    ax.text(70, 0.30, r'$E^{-\gamma-\delta}$', color='tab:blue', fontsize=33)
    ax.text(2.0e3, 3e-2, r'$E^{-\gamma-\frac{1+\delta}{2}}$', color='tab:blue', fontsize=33)

    ax.legend()
    plt.savefig('losses_simple.pdf')
    
def D_R(R, D_0, delta, Delta_delta, s, R_b):
    beta = 1.
    return D_0 * beta * np.power(R, delta) / np.power(1. + np.power(R / R_b, Delta_delta / s), s)

def plot_critical_grammage():
    fig = plt.figure(figsize=(11.5, 8.5))
    ax = fig.add_subplot(111)

    R = np.logspace(1, 3, 100)

    year = 3.14e7
    Myr = 1e6 * year
    kpc = 3.1e21
    km_s = 1e5
    s = 0.1
    Delta_delta = 0.2

    u = 5.0 * km_s
    v = 3e10 # cm/s
    delta = 0.54
    D_0 = 2.2 * 1e28 # cm^2/s
    H = 5. * kpc
    R_b = 312.
    mu = 2.3e-3 # gr/cm^2

    f_He = 0.1
    Sigma_He = np.power(4., 2./3.)

    m = 1.67e-24 * (1. + Sigma_He * f_He) / (1. + f_He) # gr
    sigma_Fe = 45. * np.power(56., 0.7) * 1e-27 # check
    sigma_O = 45. * np.power(16., 0.7) * 1e-27 # check
    sigma_C = 45. * np.power(12., 0.7) * 1e-27 # check

    print (40. / (45. * np.power(11., 0.7)))

    #D = D_0 * np.power(R, delta) / np.power(1. + np.power(R / R_b, Delta_delta / s), s)
    X = mu * (v / 2. / u) * (1. - np.exp(-u * H / D_R(R, D_0, delta, Delta_delta, s, R_b)))
    ax.plot(R, X, lw=5, color='tab:blue', label='this work')

    ax.plot(R, (m / sigma_O) * R / R, linestyle='--', color='tab:orange')
    ax.plot(R, (m / sigma_C) * R / R, linestyle='--', color='tab:green')
    ax.plot(R, (m / sigma_Fe) * R / R, linestyle='--', color='tab:red')

    #ax.fill_between([1e1,1e4],[0.7,0.7],0.,facecolor='tab:olive',alpha=0.5)

    ax.text(400, 8.05, 'C$^{12}_{6}$', fontsize=19, color='tab:green')
    ax.text(400, 5.15, 'O$^{16}_{8}$', fontsize=19, color='tab:orange')
    ax.text(400, 2.75, 'Fe$^{56}_{26}$', fontsize=19, color='tab:red')
    ax.text(300, 0.84, 'Galactic', fontsize=22, color='tab:blue') # , rotation=-30)
    #ax.text(15, 0.75, 'Sources', fontsize=20, color='tab:olive', rotation=0)

    #ax.legend(fontsize=14)

    ax.set_xscale('log')
    ax.set_xlim([1e1, 1e3])
    ax.set_yscale('log')
    ax.set_ylim([0.5, 10])
    ax.set_xlabel('R [GV]')
    ax.set_ylabel('X [gr/cm$^2$]')

    plt.savefig('grammage_critical.pdf')

    
if __name__== "__main__":
    print (f'{lambda_A(10.):5.1f} {lambda_A(12.):5.1f} {P_BC():5.2f}')
    plot_grammage()
    plot_critical_grammage()
    plot_diffusion()
    #plot_losses()
