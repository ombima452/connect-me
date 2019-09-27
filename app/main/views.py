from flask_login import login_required,current_user
from flask import redirect,render_template,url_for
from . import main
from .. import db
from app.models import Post,Comments
from . forms import PostForm,CommentForm

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
