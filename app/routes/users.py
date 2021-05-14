from app import app
from flask import request
from ..controllers import user_controller

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET': return user_controller.get_user()
    elif request.method == "POST": return user_controller.post_user()

@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def users_id(id):
    if request.method == 'PUT': return user_controller.update_user(id)
    if request.method == 'GET': return user_controller.read(id)
    if request.method == 'DELETE': return user_controller.delete(id)