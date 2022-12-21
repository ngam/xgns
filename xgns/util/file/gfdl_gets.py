""" dmget files at gfdl """

import subprocess


def gfdl_dmget(paths):
    """ dmget files at gfdl """
    for path in paths:
        subprocess.run(["dmget", path], check=True)
