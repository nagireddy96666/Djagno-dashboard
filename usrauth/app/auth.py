from functools import wraps
from flask import request, Response



def basic_auth(username, password):
    return username == 'admin' and password == 'admin'


def authenticate():
    return Response ('You have to login with proper credentials', 401,
                     {'message': 'user is not authenticated, login is required'})


def requires_auth(f):
    # import pdb; pdb.set_trace()
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not basic_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated