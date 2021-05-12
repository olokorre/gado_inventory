from app import app
from ..database import user_repository
from flask import request

User = user_repository.UserRepository()

def get_user():
    try:
        nick = request.form['nick']
        passwd = request.form['passwd']
        # Validação do usuário
        return {
            "message": "você foi autenticado!",
            "user_info": {
                "name": "--nome--",
                "nick": nick,
                "passwd": passwd
            }
        }
    except:
        return {
            "message": "Os campos 'nick' e 'passwd' são obrigatórios!"
        }, 400

def post_user():
    # try:
    data = []
    data.append(request.form['name'])
    data.append(request.form['passwd'])
    data.append(request.form['email'])
    user = User.create(data)
    return {
        "message": "Seu usuário foi criado!",
        "data": {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        }
    }, 201
    # except:
    #     return {
    #         "message": "Os parámetros 'name', 'nick' e 'passwd' são obrigatórios!"
    #     }, 400

def read(id):
    user = User.read(id)
    return {
        "message": "Aqui esta os dados do usuário:",
        "data": {
            "name": user[1],
            "email": user[2],
        }
    }, 200

def update_user(id):
    # try:
    data = []
    data.append(request.form['name'])
    data.append(request.form['passwd'])
    data.append(request.form['email'])
    user = User.update(id, data)
    return {
        "message": "Seu usuário foi atualizado!",
        "data": {
            "name": user[1],
            "email": user[2],
        }
    }, 200
    # except:
    #     return {
    #         "message": "Os parámetros 'name', 'nick' e 'passwd' são obrigatórios!"
    #     }, 400