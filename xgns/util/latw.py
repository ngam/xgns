""" get the latitude weights for a given xarray dataset """

import numpy as np


def get_wts(xda):
    """ get the lat weights """

    return np.cos(np.deg2rad(xda.lat))
