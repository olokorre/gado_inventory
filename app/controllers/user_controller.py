from app import app
from ..database import user_repository
from flask import request
from binascii import hexlify
from os import urandom

User = user_repository.UserRepository()

def post_user():
    try:
        user = User.create({
            "name": request.json['name'],
            "passwd": request.json['passwd'],
            "email": request.json['email'],
            "token": str(hexlify(urandom(20)).decode())
        })
        return {
            "message": "Seu usuário foi criado",
            "user": user,
            "token": User.get_token(user['id']),
        }, 201
    except:
        return {
            "message": "Seu usuário não foi criado"
        }, 400

def read(id):
    user = User.read(id)
    return {
        "message": "Aqui esta os dados do usuário",
        "user": user,
    }, 200

def update_user(id):
    try:
        user = User.update(id, {
            "name": request.json['name'],
            "passwd": request.json['passwd'],
            "email": request.json['email'],
            "token": User.get_token(id)
        })
        return {
            "message": "Seu usuário foi atualizado",
            "user": user,
        }, 200
    except:
        return {
            "message": "Seu usuário não foi atualizado"
        }, 400

def delete(id):
    try:
        User.delete(id)
        return {
            "message": "ok",
        }, 200
    except:
        return {
            "message": "Usuário não existe"
        }, 404

def login():
    try:
        user = User.get_by_email(request.json['email'])
        if not user: return { "message": "email não cadastrado", "email": request.json['email'] }, 404
        if user[3] != request.json['passwd']: return { "message": "Senha incorreta" }, 401
        user = User.refresh_token(user[0], str(hexlify(urandom(20)).decode()))
        return { "token": user[4] }
    except:
        return {
            "message": "Os parâmetros 'email' e 'passwd' são obrigatórios"
        }, 400