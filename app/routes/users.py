from app import app
from flask import request
from ..controllers import user_controller

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method == 'GET':
        return user_controller.get_user()
    elif request.method == "POST":
        return user_controller.post_user()
    else:
        return {
            "message": "Esse método de request não é suportado por essa rota!"
        }, 400