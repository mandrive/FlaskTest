from flask import Blueprint, render_template
from services.Services import PostService

mod = Blueprint('Post', __name__)


@mod.route('/posts')
def posts_path():
    posts = PostService().getAll()
    return render_template('Post/posts.html', posts=posts)