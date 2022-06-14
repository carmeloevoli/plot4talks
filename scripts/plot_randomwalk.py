import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np
import math
    
def compute_gaussian(ax, dt, color, label):
    z = np.linspace(-10., 10, 2000)
    f = 1. / np.power(4. * np.pi * dt, 0.5) * np.exp(-(z * z) / 4. / dt)
    ax.plot(z, f, color=color, zorder=1, label=label, lw=4)

def plot_gaussian():
    fig = plt.figure(figsize=(11.5, 8.5))
    ax = fig.add_subplot(111)

    ax.set_ylim([0.,0.7])
    ax.set_ylabel('propagator')
    ax.set_xlabel(r'distance')
    ax.set_xlim([-10.,10.])

    #compute_gaussian(ax, 0.1, 'tab:blue', 'Dt = 0.1')
    compute_gaussian(ax, 0.2, 'tab:orange', 't = 0.2')
    compute_gaussian(ax, 0.5, 'tab:green', 't = 0.5')
    compute_gaussian(ax, 1., 'tab:red', 't = 1')
    compute_gaussian(ax, 2., 'tab:purple', 't = 2')
    compute_gaussian(ax, 5., 'tab:olive', 't = 5')
    compute_gaussian(ax, 10., 'tab:cyan', 't = 10')

    ax.plot([0,0],[0.,3.],':',color='tab:gray', linewidth=2)
    ax.legend(loc='best')
    plt.savefig('gaussian_1D.pdf')

# Fixing random state for reproducibility
np.random.seed(19680801)

def random_walk(num_steps, max_step=0.05):
    pos = 0.
    walk = []
    for i in range(num_steps):
        walk.append(pos)
        r = np.random.uniform(-max_step, max_step)
        if r > 0:
            pos += 1.
        else:
            pos -= 1.
    #steps = np.array([0.1, 0.1]) # np.random.uniform(-max_step, max_step, size=(num_steps, 2))
    #walk = start_pos + np.cumsum(steps, axis=0)
    return np.array(walk)

def plot_rw():
    fig = plt.figure(figsize=(16.5, 8.5))
    ax = fig.add_subplot(111)

    ax.set_ylim([-30.,30.])
    ax.set_ylabel(r'd')
    ax.set_xlabel(r't')
    ax.set_xlim([0.,100.])

    num_steps = 100
    walks = [random_walk(num_steps, 1.) for index in range(40)]

    t = np.arange(0, num_steps)
    for walk in walks:
        ax.plot(t, walk)

    plt.savefig('rw_2D.pdf')

if __name__== "__main__":
    #plot_gaussian()
    plot_rw()
