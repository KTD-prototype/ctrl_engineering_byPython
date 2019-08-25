import control
from control.matlab import *
import sympy as sp
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


# generator to set style of line to plot a graph
def linestyle_generator():
    linestyle = ['-', '--', '-.', ':']
    lineID = 0
    while True:
        yield linestyle[lineID]
        lineID = (lineID + 1) % len(linestyle)

# function to fix style of graph


def plot_set(fig_ax, *args):
    fig_ax.set_xlabel(args[0])  # set label for x axis from 1st argument
    fig_ax.set_ylabel(args[1])  # set label for y axis from 2nd argument
    fig_ax.grid(ls=':')
    if len(args) == 3:
        fig_ax.legend(loc=args[2])  # set location of legend by 3rd argument
    # plt.show()


# function to fix bode diagram
def bodeplot_set(fig_ax, *args):
    # grid and y axis settings for gain diagram
    fig_ax[0].grid(which="both", ls=':')
    fig_ax[0].set_ylabel('Gain [dB]')  # show "gain [dB]" at drawed diagram

    # grid, x axis and y axis settings for phase diagrams
    fig_ax[1].grid(which="both", ls=':')
    fig_ax[1].set_xlabel('$\omega$ [rad/s]')
    fig_ax[1].set_ylabel('Phase [deg]')  # show "phase[deg]" at drawed diagram

    # show legend
    if len(args) > 0:
        # if argments are equal or more then 1, write in gain diagrams
        fig_ax[1].legend(loc=args[0])
    if len(args) > 1:
        # if eq or more than 2, also write in phase diagram, too
        fig_ax[0].legend(loc=args[1])
