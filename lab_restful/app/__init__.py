from flask import Flask
from . import router

import app.config
import app.utils
import app.models
import app.api

__name__ = 'lab_restful'
__version__ = 0.1

app = Flask(__name__)

router.register_api(app)

