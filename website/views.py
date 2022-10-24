from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.models import BlogPost
from website.__init_ import db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def signals():
    if request.method == 'POST':
        post_content = request.form.get('content')
        new_post = BlogPost(content=post_content)
        db.session.add(new_post)
        db.create_all()
        db.session.commit()
        return redirect('/')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('home.html', all_post=all_posts, user=current_user)


@views.route('/home')
def home():
    return render_template('home.html', user=current_user)


@views.route('/banner')
def banner():
    return render_template('banner.html')


@views.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('views.signals'))


@views.route('/signals/delete/<int:id>')
def delete_signal(id):
    post = SignalPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('views.signals'))

