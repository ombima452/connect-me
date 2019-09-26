from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True,unique = True)
    pass_secure = db.Column(db.String(255))
    comment = db.relationship('Comments',backref='user',lazy='dynamic')
    post = db.relationship('Post',backref='user',lazy='dynamic')
    email=db.Column(db.String(255),unique = True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

    def __repr__(self):
        return f'User{self.username}'

class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    description = db.Column(db.String(255))
    comment = db.relationship('Comments',backref='post',lazy='dynamic')
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(id):
        posts = Post.query.order_by(post_id = id).desc().all()
        return posts
    
    def __repr__(self):
        return f'Post {self.category}'

class Comments(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String(255))
    name=db.Column(db.String(255))
    # number=db.Column(db.Integer(255))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id=db.Column(db.Integer,db.ForeignKey('posts.id'))
    def save(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'Comments {self.comment}'
