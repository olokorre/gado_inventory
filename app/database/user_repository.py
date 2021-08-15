from app import db, sql
from ..database import crud

class UserRepository(crud.Crud):
    table = 'users'
    filables = [
        'name',
        'passwd',
        'email',
        'token',
    ]
    visible = [
        'name',
        'email',
        'id',
    ]

    def get_token(self, id):
        sql.execute('select token from %s where id = %s' %(self.table, id))
        return sql.fetchone()[0]
    
    def get_by_email(self, email):
        sql.execute('select * from %s where email = "%s"' %(self.table, email))
        return sql.fetchone()
    
    def refresh_token(self, id, new_token):
        sql.execute('update %s set token = "%s" where id = %s' %(self.table, new_token, id))
        db.commit()
        sql.execute('select * from %s where id = %s' %(self.table, id))
        return sql.fetchone()

    def auth(self, token):
        sql.execute('select * from %s where token = "%s"' %(self.table, token))
        return sql.fetchone()