from app import app
from flask import request

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