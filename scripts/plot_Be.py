import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np

def gaussian(x, area, x_0, sigma_x):
    pi = 3.14
    return area / sigma_x / np.sqrt(2. * pi) * np.exp(-0.5*((x-x_0)/sigma_x)**2.)

def set_axes(ax):
    ax.text(8.85, 2.1, 'Be9', color='steelblue', fontsize=30)
    ax.text(9.8, 2.1, 'Be10', color='darkorange', fontsize=30)
    ax.set_xlabel('mass [amu]', fontsize=26)
    ax.set_xlim([8, 12])
    ax.set_ylim([0, 2.5])
    ax.set_ylabel('number of events [a.u.]', fontsize=26)

def plot_Be():
    fig = plt.figure(figsize=(10.5, 8))
    ax = fig.add_subplot(111)
    set_axes(ax)

    mass = np.linspace(8, 11, 200)

    be9 = gaussian(mass, 1, 9, 0.2)
    be10 = gaussian(mass, 1, 10, 0.2)

    ax.plot(mass, be10, lw = 4, color='darkorange', label='production')
    ax.fill_between(mass, be10, 0, color='darkorange', alpha=0.2)

    be10 = gaussian(mass, 0.5, 10, 0.2)
    ax.plot(mass, be10, lw = 4, linestyle='--', color='darkorange', label=r't $\sim$ 40 Myr')

    be10 = gaussian(mass, 0.1, 10, 0.2)
    ax.plot(mass, be10, lw = 4, linestyle=':', color='darkorange', label=r't $\sim$ 80 Myr')

    ax.plot(mass, be9, lw = 4, color='steelblue')
    ax.fill_between(mass, be9, 0, color='steelblue', alpha=0.2)

    ax.legend(fontsize=23)

    ax.plot([0, 20], [2, 2], ':', lw=2)
    ax.text(10.5, 1.85, r'$\sigma$(C $\rightarrow$ $^{10}$Be) $\sim$ $\sigma$(C $\rightarrow$ $^{9}$Be)', fontsize=18, color='tab:blue')
    plt.savefig('Be_ratio.pdf')

if __name__== "__main__":
    plot_Be()

