import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np

def set_axes(ax):
    ax.set_yscale('log')
    ax.set_ylabel('Relative Abundances (C = 1)')
    ax.set_ylim([1e-8,1e4])
    ax.set_xlabel('Z')
    ax.set_xlim([0,30])
    
def plot_composition():
    fig = plt.figure(figsize=(10.5, 8))
    ax = fig.add_subplot(111)
    set_axes(ax)
    
    x, solar_y = np.loadtxt('data/composition_solar_system.txt',skiprows=2,usecols=(1, 2),unpack=True)

    size = len(x)
    x = np.arange(size)
    
    ax.bar(x, solar_y / solar_y[5], align='edge', width=1.01, linewidth=0, color='tab:blue', alpha=0.7, edgecolor='none', label='Solar System')

    x, y = np.loadtxt('data/composition_CRIS.txt',skiprows=0, usecols=(0,1),unpack=True)

    print (x)

    ax.plot(x - 0.5, y / y[5], 'r', marker='o', markersize='12', markeredgewidth=0.0, label='CRIS')

    ax.legend(loc='upper right')

    Z = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn']
    x_text = 0.5
    for i in Z:
        ax.text(x_text, 1.26e4, i, fontsize=13, horizontalalignment='center', verticalalignment='baseline')
        x_text += 1
        
    plt.savefig('composition.pdf')

if __name__== "__main__":
    plot_composition()
