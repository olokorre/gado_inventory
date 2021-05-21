from app import db, sql

class Crud(object):
    table = ''
    filables = []
    visible = []

    def json_list(self, json, columns):
        print(json)
        response = []
        for i in range(len(columns)): response.append(json[columns[i]])
        return response
    
    def list_json(self, list, columns):
        json = {}
        for i in range(len(columns)): json[columns[i]] = list[i]
        return json

    def make_string(self, columns):
        string = ''
        for i in columns:
            if i != columns[-1]: string += i + ', '
            else: string += i
        return string

    def create(self, data):
        data = self.json_list(data, self.filables)
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
        sql.execute('select %s from %s' %(self.make_string(self.visible), self.table))
        return self.list_json(sql.fetchall()[-1], self.visible)
    
    def read(self, id):
        sql.execute('select %s from %s where id = %s' %(self.make_string(self.visible), self.table, id))
        return self.list_json(sql.fetchone(), self.visible)

    def update(self, id, data):
        update = 'update ' + self.table + ' set '
        for i in range(len(self.filables)):
            update += self.filables[i] + ' = "' + data[i] + '"'
            if i != len(self.filables)  - 1: update += ', '
        update += ' where id = ' + id
        sql.execute(update)
        db.commit()
        sql.execute('select %s from %s where id = %s' %(self.make_string(self.visible), self.table, id))
        return self.list_json(sql.fetchone(), self.visible)
    
    def get_all(self):
        sql.execute('select %s from %s' %(self.make_string(self.visible), self.table))
        response = []
        for i in sql.fetchall(): response.append(self.list_json(i, self.visible))
        return response
    
    def delete(self, id):
        sql.execute('delete from %s where id = %s' %(self.table, id))
        return None