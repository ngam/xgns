""" gfdl path """


def gfdl_path(cons):
    """ read path at gfdl """

    apath, cpath = [], []
    for path in [apath, cpath]:
        for exp in cons["aexps"]:
            for key, vals in cons["rads"][0].items():
                for val in vals:
                    path.append(
                        cons["apath1"] +
                        exp +
                        cons["apath2"] +
                        key +
                        val +
                        "*.nc"
                    )

    return apath, cpath
