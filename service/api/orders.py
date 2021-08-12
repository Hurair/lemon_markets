from datetime import datetime
from flask import abort


def post(**kwargs):
    """
    POST method to place order
    :param kwargs
    :return: request_body
    """
    request_body = kwargs['body']

    validate_time(request_body['valid_until'])

    result = {
        "isin": request_body['isin'],
        "limit_price": request_body['limit_price'],
        "quantity": request_body['quantity'],
        "side":  request_body['side'],
        "valid_until": request_body['valid_until']
    }
    return result, 201


def validate_time(utc_time: int) -> bool:
    """
    Validates the UNIX UTC Timestamp, abort in case of failure.
    :param utc_time
    """
    date_time = datetime.fromtimestamp(utc_time)
    if date_time > date_time.now():
        return True
    else:
        abort(400, f"{utc_time} is not a valid time or not in future.")
