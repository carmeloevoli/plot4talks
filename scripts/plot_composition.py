import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np

Z = ['H','He','Li','Be','B','C','N','O',
     'F','Ne','Na','Mg','Al','Si','P','S',
     'Cl','Ar','K','Ca','Sc','Ti','V','Cr',
     'Mn','Fe','Co','Ni']

def set_axes(ax):
    ax.set_yscale('log')
    ax.set_ylabel('Relative Abundances (C = 1)')
    ax.set_ylim([1e-8,1e4])
    ax.set_xlabel('Z')
    ax.set_xlim([0.5,28.5])
    
def plot_composition(fCRs, plotname):
    size = len(Z)
    assert(len(fCRs) == size)

    fig = plt.figure(figsize=(12., 8.))
    ax = fig.add_subplot(111)
    set_axes(ax)
    
    x, solar_y = np.loadtxt('data/composition_solar_system.txt',skiprows=2,max_rows=28,usecols=(1,2),unpack=True)
    x = np.arange(size)
    
    my_cmap = plt.get_cmap("viridis")
    rescale = lambda z: (z - np.min(x)) / (np.max(x) - np.min(x))

    ax.bar(x + 0.5, solar_y / solar_y[5], align='edge', width=1.01, linewidth=0, alpha=0.65, edgecolor='none', label='Solar System',
           color = my_cmap(rescale(x)))
    
    color = 'tab:red'
    ax.plot(x + 1.0, fCRs / fCRs[5], color=color, zorder=2)
    ax.plot(x + 1.0, fCRs / fCRs[5], 'o', markersize=12, markeredgecolor=color, color=color, zorder=1, label=r'GCR')

    #x, fCRs = np.loadtxt('data/composition_CRIS.txt',skiprows=0, usecols=(0,1),unpack=True)
    #fCRs /= fCRs[5]

    #color = 'tab:red'
    #ax.plot(x, fCRs / fCRs[5], color=color, zorder=2)
    #ax.plot(x, fCRs / fCRs[5], 'o', markersize=9, markeredgecolor=color, color=color, zorder=3, label=r'CRIS')
    
    #x, fCRs = np.loadtxt('data/composition_HEAO3.txt',skiprows=0, usecols=(0,1),unpack=True)
    #color = 'tab:olive'
    #ax.plot(x, fCRs / fCRs[2], color=color, zorder=2)
    #ax.plot(x, fCRs / fCRs[2], 'o', markersize=9, markeredgecolor=color, color=color, zorder=3, label=r'HEAO-3 at E $> 10$ GeV/n')

    ax.legend(loc='upper right')

    x_text = 1.04
    for i in Z:
        ax.text(x_text, 1.28e4, i, fontsize=14, horizontalalignment='center', verticalalignment='baseline')
        x_text += 1
        
    plt.savefig(plotname)

def plot_composition_ratio(fCRs, plotname):
    size = len(Z)
    assert(len(fCRs) == size)

    fig = plt.figure(figsize=(15., 7.5))
    ax = fig.add_subplot(111)
    ax.set_ylim([-6,2])
    ax.set_xlim([0,29])

    x, solar_y = np.loadtxt('data/composition_solar_system.txt',skiprows=2,max_rows=28,usecols=(1,2),unpack=True)
    solar_y /= solar_y[5]

    x, fCRsCRIS = np.loadtxt('data/composition_CRIS.txt',skiprows=0, usecols=(0,1),unpack=True)
    fCRsCRIS /= fCRsCRIS[5]

    fCRs /= fCRs[5]

    for i in range(size):
        if fCRs[i] == 0.:
            fCRs[i] = fCRsCRIS[i]
    
    x = np.arange(size)
    y = np.log10(solar_y / fCRs)

    mask1 = y < 0.
    mask2 = y >= 0.

    ax.bar(x[mask1] + 1, y[mask1], align='center', color='tab:orange')
    ax.bar(x[mask2] + 1, y[mask2], align='center', color='tab:blue')
#    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xticks(x + 1, labels=Z, minor=False, fontsize=23,
                  horizontalalignment='center', verticalalignment='center')
    ax.tick_params(axis='x', which='minor', length=0)
    ax.tick_params(axis='x', which='major', pad=30)
#    ax.grid(True, axis='y')
    ax.set_ylabel(r'Log (GCR / Solar)')

    ax.plot([0,30], [0,0], '--', color='tab:gray', lw=1)
    plt.savefig(plotname)
    
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
    
def get_flux(Z):
    if Z == 1:
        filename = 'kiss_tables/AMS-02_H_rigidity.txt'
    elif Z == 2:
        filename = 'kiss_tables/AMS-02_He_rigidity.txt'
    elif Z == 3:
        filename = 'kiss_tables/AMS-02_Li_rigidity.txt'
    elif Z == 4:
        filename = 'kiss_tables/AMS-02_Be_rigidity.txt'
    elif Z == 5:
        filename = 'kiss_tables/AMS-02_B_rigidity.txt'
    elif Z == 6:
        filename = 'kiss_tables/AMS-02_C_rigidity.txt'
    elif Z == 7:
        filename = 'kiss_tables/AMS-02_N_rigidity.txt'
    elif Z == 8:
        filename = 'kiss_tables/AMS-02_O_rigidity.txt'
    elif Z == 9:
        filename = 'kiss_tables/AMS-02_F_rigidity.txt'
    elif Z == 10:
        filename = 'kiss_tables/AMS-02_Ne_rigidity.txt'
    elif Z == 11:
        filename = 'kiss_tables/AMS-02_Na_rigidity.txt'
    elif Z == 12:
        filename = 'kiss_tables/AMS-02_Mg_rigidity.txt'
    elif Z == 13:
        filename = 'kiss_tables/AMS-02_Al_rigidity.txt'
    elif Z == 14:
        filename = 'kiss_tables/AMS-02_Si_rigidity.txt'
#    elif Z == 15:
#        filename = 'kiss_tables/AMS-02_P_rigidity.txt'
#    elif Z == 16:
#        filename = 'kiss_tables/AMS-02_S_rigidity.txt'
#    elif Z == 17:
#        filename = 'kiss_tables/AMS-02_Cl_rigidity.txt'
#    elif Z == 18:
#        filename = 'kiss_tables/AMS-02_Ar_rigidity.txt'
#    elif Z == 19:
#        filename = 'kiss_tables/AMS-02_K_rigidity.txt'
#    elif Z == 20:
#        filename = 'kiss_tables/AMS-02_Ca_rigidity.txt'
#    elif Z == 21:
#        filename = 'kiss_tables/AMS-02_Sc_rigidity.txt'
#    elif Z == 22:
#        filename = 'kiss_tables/AMS-02_Ti_rigidity.txt'
#    elif Z == 23:
#        filename = 'kiss_tables/AMS-02_V_rigidity.txt'
#    elif Z == 24:
#        filename = 'kiss_tables/AMS-02_Cr_rigidity.txt'
#    elif Z == 25:
#        filename = 'kiss_tables/AMS-02_Mn_rigidity.txt'
    elif Z == 26:
        filename = 'kiss_tables/AMS-02_Fe_rigidity.txt'
#    elif Z == 27:
#        filename = 'kiss_tables/AMS-02_Co_rigidity.txt'
#    elif Z == 28:
#        filename = 'kiss_tables/AMS-02_Ni_rigidity.txt'
    else:
        return 0., 0.
    
    R, f, fErrLo, fErrUp = np.loadtxt(filename, usecols=(0,1,4,5), unpack=True, skiprows=8)
    i = find_nearest(R, 100.)
    return f[i], 0.5 * (fErrLo[i] + fErrUp[i])

if __name__== "__main__":
#    x, fCRs = np.loadtxt('data/composition_CRIS.txt',skiprows=0, usecols=(0,1),unpack=True)
    x, fCRs = np.loadtxt('data/composition_data_crdb.csv', skiprows=0, usecols=(0, 3), delimiter=',', unpack=True)
    print(x, fCRs)
    plot_composition(fCRs, 'composition_CRIS.pdf')
    plot_composition_ratio(fCRs, 'composition_ratio_CRIS.pdf')

#    fCRs = []
#    for i in range(1,29):
#        #print (i)
#        fCRs.append(get_flux(i)[0])
#        if (fCRs[-1] < 1e-20):
#            print(i, fCRs[-1])
#
#    plot_composition(fCRs, 'composition_AMS_100GeV.pdf')
#    plot_composition_ratio(fCRs, 'composition_ratio_AMS_100GeV.pdf')
