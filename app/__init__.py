from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap
from flask_login import LoginManager
<<<<<<< HEAD
from flask_mail import Mail
=======
<<<<<<< HEAD
from flask_uploads import UploadSet,configure_uploads,IMAGES
=======
>>>>>>> Dev
>>>>>>> b7cf39af251eb5530313b3a00fd81b0d5ee0d12b

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy()
<<<<<<< HEAD

=======
bootstrap = Bootstrap()
<<<<<<< HEAD
photos = UploadSet('photos',IMAGES)
=======
>>>>>>> Dev
>>>>>>> b7cf39af251eb5530313b3a00fd81b0d5ee0d12b

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from  .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

<<<<<<< HEAD


      # configure UploadSet
    configure_uploads(app,photos)


=======
>>>>>>> Dev
    return app

