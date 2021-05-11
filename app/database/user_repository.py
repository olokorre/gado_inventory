from app import db, sql
from ..database import crud

class UserRepository(crud.Crud):
    table = 'user'
    filables = [
        'name',
        'passwd',
        'email',
    ]