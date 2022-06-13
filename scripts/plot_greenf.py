import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np
import math
    
H = 4.
z = np.linspace(-10., 10, 2000)

def compute_free(l2, z_s):
    f = 1. / np.power(np.pi * l2, 1.5) * np.exp(-np.power(z - z_s, 2.) / l2)
    return f

def compute_halo(l2, z_s, n_max):
    f = 0
    for n in range(-n_max, n_max + 1):
        print (n)
        z_prime = 2. * H * n + np.power(-1., n) * z_s
        f += np.power(-1., n) * compute_free(l2, z_prime)
    return f
    
def plot_images():
    fig = plt.figure(figsize=(11.5, 8.5))
    ax = fig.add_subplot(111)
    
    ax.set_yscale('log')
    ax.set_ylim([1e-20,0.004])
    ax.set_ylabel('propagator')
    ax.set_xlabel(r'z')
    ax.set_xlim([-10.,10.])

    G = compute_free(36., 0.)
    ax.plot(z, G, color='red', zorder=1, label='free', linestyle=':')

    G = compute_halo(36., 0., 1)
    ax.plot(z, G, color='orange', zorder=1, label='n = 1')

#    print(G)
#    G = compute_halo(16., 0., 2)
#    ax.plot(z, G, color='green', zorder=1, label='n = 2')

    G = compute_halo(36., 0., 10)
    ax.plot(z, G, color='blue', zorder=1, label='n = 3', linestyle=':')

    print(G)
    #compute_halo(ax, 16., 0., 3, 'tab:blue', 'n = 3')
    #compute_gaussian(ax, 0.1, 'tab:blue', 'Dt = 0.1')
    #compute_gaussian(ax, 0.2, 'tab:orange', 't = 0.2')
    #compute_gaussian(ax, 0.5, 'tab:green', 't = 0.5')
    #compute_gaussian(ax, 2., 'tab:purple', 't = 2')
    #compute_gaussian(ax, 5., 'tab:olive', 't = 5')
    #compute_gaussian(ax, 10., 'tab:cyan', 't = 10')

    #ax.plot([0,0],[0.,3.],':',color='tab:gray', linewidth=2)
    ax.legend(loc='best')
    plt.savefig('halo_images.pdf')

def compute_sum(n_max, H, R_d):
    f = 0.
    for n in range(-n_max, n_max + 1):
        print (n)
        x = 2. * n * H / R_d
        f += np.power(-1., n) * (np.sqrt(1. + x * x) - np.sqrt(x * x))
    return f

def plot_sum():
    fig = plt.figure(figsize=(11.5, 8.5))
    ax = fig.add_subplot(111)

    H = 1.
    R_d = 100.
    
    for i in range(100):
        f = compute_sum(i, H, R_d)
        ax.plot(i, np.abs(f), 'o', color='tab:blue')

    plt.savefig('halo_sum.pdf')

if __name__== "__main__":
    plot_sum()
