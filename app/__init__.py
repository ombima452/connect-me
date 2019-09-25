from flask_sqlalchemy import flask_sqlalchemy



db = SQLAlchemy()


def create_(config_name):
    app = Flask(__name__)
    
    
    
    #initializing flask extensions
    db.init_app(app)