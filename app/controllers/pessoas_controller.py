from app import app
from ..database import pessoas_repository
from flask import request

Pessoa = pessoas_repository.PessoasRepository()

def criar():
    data = {}
    data['nome'] = request.form['nome']
    data['cpf'] = request.form['cpf']
    data['telefone'] = request.form['telefone']
    data['re_gado'] = request.form['re_gado']
    data['email'] = request.form['email']
    pessoa = Pessoa.create(data)
    return {
        "data": pessoa,
    }

def ver_todas():
    pessoas = Pessoa.get_all()
    return {
        "data": pessoas,
    }