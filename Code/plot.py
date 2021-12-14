import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os

DEFAULT_VALUE = 4

def cart2pol(x, y):
    r = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return (r, phi)

def pol2cart(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return (x, y)

'''
  Plot an 2D ndarray
'''
def plot(points, centered=2, color=colors.CSS4_COLORS['dodgerblue'], markersize=3, system='cart', saveTo=''):
    x_axis = points[:, 0]
    y_axis = points[:, 1]
    xmin = np.min(x_axis)
    xmax = np.max(x_axis)
    ymin = np.min(y_axis)
    ymax = np.max(y_axis)
    xabsmax = np.max(np.abs(x_axis))
    yabsmax = np.max(np.abs(y_axis))
    if (xmin == -np.inf):
        xmin = -DEFAULT_VALUE
    if (ymin == -np.inf):
        ymin = -DEFAULT_VALUE
    if (xmax == np.inf):
        xmax = DEFAULT_VALUE
    if (ymax == np.inf):
        ymax = DEFAULT_VALUE
    if (xabsmax == np.inf):
        xabsmax = DEFAULT_VALUE
    if (yabsmax == np.inf):
        yabsmax = DEFAULT_VALUE

    ax = plt.subplot(polar=(system == 'pol'))
    #ax.spines['left'].set_position('center')
    ax.plot(x_axis, y_axis, color=color, linestyle='', marker='.', markersize=markersize)
    
    #plt.axis('equal')
    #plt.gca().set_aspect('equal', adjustable='box')
    #ax.set_xlim([xmin-0.05, xmax+0.05])
    #ax.set_ylim([ymin-0.05, ymax+0.05])
    if (centered == 1):
        ax.set_xlim([-xabsmax, xabsmax])
        ax.set_ylim([ymin, ymax])
    elif (centered == -1):
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([-yabsmax, yabsmax])
    elif (centered == 0):
        ax.set_xlim([-xabsmax, xabsmax])
        ax.set_ylim([-yabsmax, yabsmax])
    else:
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
    
    if (saveTo != ''):
        print('SAVING ENABLED')
        _, ext = os.path.splitext(saveTo)
        ext = ext.replace('.', '')
        plt.savefig(saveTo, format=ext, dpi=1200)
    else:
        print('SAVING DISABLED')
    plt.show()


def plot1(x, f_x):
    plt.plot(x, f_x, 'r')
    plt.show()

def plot2(x, f_x, U, f_x_inv):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x, f_x, 'r')
    ax2.plot(U, f_x_inv, 'b')
    plt.show()

# len(X) % columns == 0
def plotM(X, F, titles=[], columns=2, colors = ['tab:green', 'tab:red', 'tab:blue', 'tab:orange', 'tab:cyan']):
    if (len(X) != len(F)):
        print("ERROR")
        return
    cid = 0 
    rows = int(len(X)/columns)
    fig, axs = plt.subplots(rows, columns, num='Distribution functions and their inverses')
    for a in range(0, rows):
        for b in range(0, columns):
            idx = a * columns + b
            if (len(titles) != 0):
                axs[a, b].set_title(titles[idx])
            axs[a, b].plot(X[idx], F[idx], colors[cid])
        cid = (cid + 1) % len(colors)
    
    plt.tight_layout()