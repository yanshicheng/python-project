from rest_framework.response import Response
from collections import OrderedDict


def json_api_response(code=0, data='successful', message='successful', **kwargs):
    result = OrderedDict([
        ('code', code),
        ('message', message),
        ('data', data),
    ])
    result.update(**kwargs)
    return Response(result)
