""" xarray dataset to zarr file """


def zr_save(_ds, _file):
    """ save a dataset as a zarr file """

    _ds.to_zarr(_file, compute=True, mode="w")
