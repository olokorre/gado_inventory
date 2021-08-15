from app import app
from flask import request
from ..controllers import user_controller
from ..database import user_repository

User = user_repository.UserRepository()

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    try:
        if request.method == 'POST': return user_controller.post_user()
        else:
            user = User.auth(request.headers['User-key'])
            if user and request.method == 'GET': return user_controller.read(user[0])
            elif user and request.method == 'DELETE': return user_controller.delete(user[0])
            elif user and request.method == 'PUT': return user_controller.update_user(user[0])
    except:
        return {
            "message": "Não autenticado"
        }, 401 

@app.route('/login', methods=['POST'])
def auth_user():
    return user_controller.login()