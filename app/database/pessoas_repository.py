from app import db, sql
from ..database import crud

class PessoasRepository(crud.Crud):
    table = 'pessoas'
    filables = [
        'nome',
        'cpf',
        'telefone',
        're_gado',
        'email',
    ]
    visible = [
        'nome',
        'cpf',
        'telefone',
        're_gado',
        'email',
        'id',
    ]
