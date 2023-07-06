import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
plt.style.use('review.mplstyle')
import numpy as np

def set_axes(ax):
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim([1, 1e3])
    ax.set_ylim([0.01, 2])
    ax.set_xlabel('R [GV]', fontsize=28, labelpad=8)
    ax.set_ylabel(r'R$^\gamma$ flux [a.u.]', fontsize=28, labelpad=8)
    ax.legend(loc='lower left', fontsize=18)
    ax.text(10, 1.15, r'$-\gamma$', color='steelblue', fontsize=26)
    ax.text(21, 0.40, r'$-\gamma - \delta$', color='darkorange', fontsize=26)
    ax.text(130, 0.25, r'$-\gamma - \delta + \Delta$', color='darkorange', fontsize=26)
    ax.text(5, 0.1, r'$-\gamma - 2\delta$', color='crimson', fontsize=26)

def origin_break_acceleration():
    fig = plt.figure(figsize=(10.5, 9.0))
    ax = fig.add_subplot(111)

    R = np.logspace(0, 3, 200)

    norm = 1.
    delta = 0.
    ddelta = -0.2
    s = 0.01
    R_b = 100.

    phi = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s

    ax.plot(R, phi, color='steelblue', lw = 4, label='primary injection')
    ax.text(150, 0.8, r'$-\gamma + \Delta$', color='steelblue', fontsize=26)

    delta = 1./3.
    phi_w = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s

    ddelta = 0.
    phi_no = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s

    ax.fill_between(R, phi_w, phi_no, color='darkorange', alpha = 0.2)
    ax.plot(R, phi_w, color='darkorange', lw = 4, label=r'primary after propagation')

    ddelta = -0.2
    delta = 2./3.
    phi_w = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s
  
    ddelta = 0.
    phi_no = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s

    ax.fill_between(R, phi_w, phi_no, color='crimson', alpha = 0.2)
    ax.plot(R, phi_w, color='crimson', lw = 4, label='secondary after propagation')
    ax.text(100, 0.053, r'$-\gamma - 2\delta + \Delta$', color='crimson', fontsize=26)

    ax.set_title('break in the injection')
    set_axes(ax)
    plt.savefig('origin_break_acceleration.pdf')

def origin_break_diffusion():
    fig = plt.figure(figsize=(10.5, 9.0))
    ax = fig.add_subplot(111)

    R = np.logspace(0, 3, 200)
    
    norm = 1.
    delta = 0.
    ddelta = 0.
    s = 0.01
    R_b = 100.

    phi = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s

    ax.plot(R, phi, color='steelblue', lw = 4, label='primary injection')

    ddelta = -0.2
    delta = 1./3.
    phi_w = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s

    ddelta = 0.
    phi_no = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s

    ax.fill_between(R, phi_w, phi_no, color='darkorange', alpha = 0.2)
    ax.plot(R, phi_w, color='darkorange', lw = 4, label=r'primary after propagation')
 
    ddelta = -0.4
    delta = 2./3.
    phi_w = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s

    ddelta = 0.
    phi_no = norm * R**(-delta) * (1. + (R / R_b)**(-ddelta / s))**s

    ax.fill_between(R, phi_w, phi_no, color='crimson', alpha = 0.2)
    ax.plot(R, phi_w, color='crimson', lw = 4, label='secondary after propagation')
    ax.text(100, 0.053, r'$-\gamma - 2\delta + 2\Delta$', color='crimson', fontsize=26)

    ax.set_title('break in the diffusion coefficient')
    set_axes(ax)
    plt.savefig('origin_break_diffusion.pdf')

if __name__== "__main__":
    origin_break_diffusion()
    origin_break_acceleration()
