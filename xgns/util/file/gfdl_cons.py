""" read cons at gfdl """

import yaml


def gfdl_cons(cons_file=None):
    """ read cons at gfdl """

    if cons_file is None:
        defs_file = "xgns/util/file/cons.yaml"
        with open(defs_file, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    else:
        with open(cons_file, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
