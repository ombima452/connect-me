from flask_login import login_required,current_user
from . import main
from app.models import Post,Comments
from . forms import PostForm,CommentForm
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from .forms import ReviewForm,UpdateProfile
from .. import db,photos


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    all_posts = Post.query.all()

    return render_template('index.html',all_posts = all_posts)

@main.route('/posts/new',methods=['GET','POST'])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        user_id = current_user._get_current_object().id
        post = Post(name = post_form.name.data,age = post_form.age.data,gender = post_form.gender.data,description = post_form.description.data,user_id=user_id)
        post.save()
        return redirect(url_for('main.index'))
    return render_template('post.html',post_form=post_form)

@main.route('/comment/<int:post_id>',methods=['GET','POST'])
@login_required
def comment(post_id):
    comment_form = CommentForm()
    comments = Comments.query.filter_by(post_id=post_id).all()
    if comment_form.validate_on_submit():
        post_id = post_id
        user_id = current_user._get_current_object().id
        comment = Comments(name = comment_form.name.data,number = comment_form.number.data,comment = comment_form.comment.data,user_id = user_id, post_id = post_id) 
        comment.save()
        return redirect(url_for('main.index'))
    return render_template('comment.html',comment_form=comment_form,comments = comments)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html",user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('main.profile',uname=uname))
    return render_template('index.html')

