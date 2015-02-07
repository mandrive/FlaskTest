from flask import jsonify
from flask_restful import Resource
from services.Services import PostService


class PostsList(Resource):
    def get(self):
        all_posts = PostService().getAll()
        dictionaries_list = []
        for post in all_posts:
            dictionaries_list.append(post.as_dict())
        return jsonify(results=dictionaries_list)


class Posts(Resource):
    def get(self, post_id):
        return jsonify(PostService().getById(post_id).as_dict())