from app import app
from flask import request
from ..controllers import pessoas_controller

@app.route('/pessoas', methods = ['POST', 'GET'])
def criar_pessoa():
    if request.method == 'POST': return pessoas_controller.criar()
    if request.method == 'GET': return pessoas_controller.ver_todas()