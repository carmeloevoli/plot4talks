import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np
import math
        
def compute_halo(l2, z_s, H, n_max):
    f = 0
    for n in range(-n_max, n_max + 1):
        z_prime = 2. * H * n + np.power(-1., n) * z_s
        f += np.power(-1., n) * np.exp(-(z_prime)**2.0 / l2)
    return f
    
def compute_proton_burst(D, H, time, distance, dohalo = True):
    dtau = D * time
    d2 = distance * distance
    g = 1. / np.power(4. * np.pi * dtau, 1.5) * np.exp(- d2 / 4. / dtau)
    if dohalo:
        g *= compute_halo(4. * D * time, 0., H, 10)
    return g
    
def plot_protons():
    fig = plt.figure(figsize=(17.5, 8.))
    
    kpc = 3.1e21 # cm
    D = 10e28 # cm2/s
    Myr = 3e13 # s
    
    ax1 = fig.add_subplot(121)

    ax1.set_xscale('log')
    ax1.set_xlabel('t [Myr]')
    ax1.set_xlim([0.1, 1e2])
    ax1.set_ylim([0, 1.1])
    ax1.set_ylabel('propagator')
    
    t = np.logspace(-1, 2, 1000)
    y_a = []
    y_b = []
    for t_i in t:
        y_a.append(compute_proton_burst(D, 1. * kpc, t_i * Myr, kpc, True))
        y_b.append(compute_proton_burst(D, 1. * kpc, t_i * Myr, kpc, False))
    ax1.plot(t, y_a / max(y_a), color='tab:red')
    ax1.plot(t, y_b / max(y_b), linestyle = ':', color='tab:blue')

    t_d = kpc * kpc / 4. / D / Myr
    ax1.plot([t_d, t_d], [0, 10], ':', color='tab:orange')
    ax1.text(1.0, 0.9, r'$\frac{d^2}{4 D}$', fontsize=35, color='tab:orange')

    ax2 = fig.add_subplot(122)

    #ax2.set_xscale('log')
    ax2.set_xlabel('distance [kpc]')
    ax2.set_ylim([0, 1.1])
    #ax2.set_ylabel('propagator')
    ax2.set_xlim([0, 10])

    d = np.logspace(-1, 1, 1000)
    y_a = []
    y_b = []
    for d_i in d:
        y_a.append(compute_proton_burst(D, kpc, 10. * Myr, d_i * kpc, True))
        y_b.append(compute_proton_burst(D, kpc, 10. * Myr, d_i * kpc, False))
    ax2.plot(d, y_a / max(y_a), color='tab:red')
    #ax2.plot(d, y_b / max(y_b), linestyle = ':')

    r_d = 2. * np.sqrt(D * 10. * Myr) / kpc
    ax2.plot([r_d, r_d], [0, 10], ':', color='tab:orange')
    ax2.text(3.7, 0.9, r'$\sqrt{4 D \tau}$', fontsize=35, color='tab:orange')

    plt.savefig('green_protons.pdf')

if __name__== "__main__":
    plot_protons()
