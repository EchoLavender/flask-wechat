# set python env utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
#from flask.ext.cors import CORS
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app    



