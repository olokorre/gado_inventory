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
        print(insert)
        sql.execute(insert)
        db.commit()