from flask import Flask
from . import api


__name__ = 'lab_restful'
__version__ = 0.1

app = Flask(__name__)

api.register_api(app)

