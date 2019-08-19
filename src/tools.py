# -*- coding: utf-8 -*-


def r(d, f):
    if type(d) not in (dict, list):
        return d

    elif type(d) == list:
        return [v for v in (r(v, f) for v in d) if not f(v)]

    elif type(d) == dict:
        return {k: v for k, v in ((k, r(v, f)) for k, v in d.items()) if not f(v)}


def clean_empty(d):
    return r(d, lambda x: x in ([], {}, ()))
