from flask import Blueprint

from services.Services import PostService
from utils.utils import templated, login_required


mod = Blueprint('Post', __name__)


@mod.route('/posts')
@templated('Post/posts.html')
@login_required
def posts_path():
    posts = PostService().getAll()
    return dict(posts=posts)