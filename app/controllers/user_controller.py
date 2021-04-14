from app import app
from flask import request

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
    try:
        name = request.form['name']
        nick = request.form['nick']
        passwd = request.form['passwd']
        return {
            "message": "Seu usuário foi criado!",
            "user_info": {
                "name": name,
                "nick": nick,
                "passwd": passwd
            }
        }, 200
    except:
        return {
            "message": "Os parámetros 'name', 'nick' e 'passwd' são obrigatórios!"
        }, 400