""" 
Various plotting tools for oceanographic data analysis

- This is largely oriented towards observational datasets but will one day hopefully have  model output orientied tools as well


TOC:
1. CTD profiles -- oldy but a goody 
2. Time series - single series
3. time series - 2d contourd plot 
4.
5.
6.




"""

# load modules
import matplotlib.pyplot as plt
import gsw
import cmocean
import colorcet as cc
import xarray as xr 
import pandas as pd
import gsw
import numpy.ma as ma 



## A dictionary of basin plotting parameers
# plot parameters
plotParams = dict(
    bathyBottom=3000,
    bathyColor='k',
    bathyMaskColor='grey',
    mooringLineColor='k',
    mooringLineStye='--',
    mooringGridxlabelDist='[km]',
    mooringGridylabelDepth='[m]'
)


def ctdProfile(z, data, ax=None, pressure=True):
    """

    """

    return profileAx


def hovmoller():
    """
    


    """

def timeSeries():
    """
    



    """

def twoDfieldPlot():
    """
    


    """


