from app import db, sql

class Crud(object):
    table = ''
    filables = []
    
    def create(self, data):
        insert = 'insert into ' + self.table + ' ('
        for filable in self.filables:
            insert += filable
            if self.filables[-1] != filable: insert += ','
        insert += ') values ('
        for d in data:
            if type(d) == type(1): insert += d
            else: insert += '"' + d + '"'
            if data[-1] != d: insert += ','
        insert += ')'
        sql.execute(insert)
        db.commit()
        sql.execute('select * from ' + self.table)
        return sql.fetchall()[-1]
    
    def read(self, id):
        read = 'select * from ' + self.table + ' where id = ' + id
        sql.execute(read)
        data = sql.fetchone()
        return data

    def update(self, id, data):
        update = 'update ' + self.table + ' set '
        for i in range(len(self.filables)):
            update += self.filables[i] + ' = "' + data[i] + '"'
            if i != len(self.filables)  - 1: update += ', '
        update += ' where id = ' + id
        sql.execute(update)
        db.commit()
        sql.execute('select * from ' + self.table + ' where id = ' + id)
        return sql.fetchone()