""" calculate temporal mean weighted by days in each month

    adapted from:
    https://ncar.github.io/esds/posts/2021/yearly-averages-xarray/
"""

import numpy as np
import xarray as xr


def weighted_temporal_mean(_ds, var=None):
    """ weight by days in each month """

    # Determine the month length
    month_length = _ds.time.dt.days_in_month

    # Calculate the weights
    wgts = (
        month_length.groupby("time.year") /
        month_length.groupby("time.year").sum()
    )

    # Make sure the weights in each year add up to 1
    np.testing.assert_allclose(wgts.groupby("time.year").sum(xr.ALL_DIMS), 1.0)

    # Subset our dataset for our variable
    obs = _ds if var is None else _ds[var]

    # Setup our masking for nan values
    cond = obs.isnull()
    ones = xr.where(cond, 0.0, 1.0)

    # Calculate the numerator
    obs_sum = (obs * wgts).resample(time="AS").sum(dim="time")

    # Calculate the denominator
    ones_out = (ones * wgts).resample(time="AS").sum(dim="time")

    # Return the weighted average
    return obs_sum / ones_out
