# -*- coding: utf-8 -*-


def r(d, pred):
    if type(d) not in (dict, list):
        return d

    elif type(d) == list:
        return [v for v in (r(v, pred) for v in d) if pred(v)]

    elif type(d) == dict:
        return {k: v for k, v in ((k, r(v, pred)) for k, v in d.items()) if pred(v)}


def clean_empty(d):
    return r(d, lambda x: x not in ([], {}, ()))
