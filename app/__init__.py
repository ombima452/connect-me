

from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
<<<<<<< HEAD
from flask_uploads import UploadSet,configure_uploads,IMAGES
=======
>>>>>>> Dev

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstrap = Bootstrap()
<<<<<<< HEAD
photos = UploadSet('photos',IMAGES)
=======
>>>>>>> Dev

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from  .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

<<<<<<< HEAD


      # configure UploadSet
    configure_uploads(app,photos)


=======
>>>>>>> Dev
    return app

