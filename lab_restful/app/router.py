from flask_restful import Api
from . import api


def register_api(app):
    router = Api(app)
    router.add_resource(api.Hello, '/api/hello')
