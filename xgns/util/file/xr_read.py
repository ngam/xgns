""" read .nc files as xr.Dataset """

import xarray as xr


def xr_read(_file):
    """ read in a file with xarray """

    return xr.open_mfdataset(_file, parallel=True, decode_cf=False)
