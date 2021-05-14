from app import app
from ..database import user_repository
from flask import request

User = user_repository.UserRepository()

def get_user():
    users = User.get_all()
    return {
        "message": "você foi autenticado!",
        "users": users,
    }
def post_user():
    # try:
    data = []
    data.append(request.form['name'])
    data.append(request.form['passwd'])
    data.append(request.form['email'])
    user = User.create(data)
    return {
        "message": "Seu usuário foi criado!",
        "user": user,
    }, 201
    # except:
    #     return {
    #         "message": "Os parámetros 'name', 'nick' e 'passwd' são obrigatórios!"
    #     }, 400

def read(id):
    user = User.read(id)
    return {
        "message": "Aqui esta os dados do usuário:",
        "user": user,
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
        "user": user,
    }, 200
    # except:
    #     return {
    #         "message": "Os parámetros 'name', 'nick' e 'passwd' são obrigatórios!"
    #     }, 400

def delete(id):
    User.delete(id)
    return {
        "message": "ok",
    }, 200