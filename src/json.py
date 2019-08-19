# -*- coding: utf-8 -*-

from datetime import (datetime, date, timezone)
from decimal import (Decimal, InvalidOperation)


def parse_date_string(v, f):
    v = datetime.strptime(v, f)
    v = v.replace(tzinfo=timezone.utc)
    return v


def parse_object(v):
    if not isinstance(v, bool) and (isinstance(v, int) or isinstance(v, float)):
        v = Decimal(str(v))
    elif isinstance(v, str):
        try:
            v = Decimal(v)
        except (InvalidOperation, ValueError):
            try:
                v = parse_date_string(v, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                try:
                    v = parse_date_string(v, '%Y-%m-%dT%H:%M:%S.%fZ')
                except ValueError:
                    try:
                        v = parse_date_string(v, '%Y-%m-%dT%H:%M:%SZ')
                    except ValueError:
                        pass
    return v


def json_decoder(obj):
    if type(obj) == list:
        return [json_decoder(v) for v in obj]

    elif type(obj) == dict:
        return {k: v for k, v in obj.items()}
    else:
        return parse_object(obj)


def json_encoder(obj):
    if type(obj) in (date, datetime):
        return obj.isoformat()
    elif type(obj) in (Decimal, int, float):
        return float(obj)
    else:
        return obj
