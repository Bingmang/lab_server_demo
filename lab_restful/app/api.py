from flask_restful import Api
from . import models


def register_api(app):
    api = Api(app)
    api.add_resource(models.Hello, '/api/hello')

