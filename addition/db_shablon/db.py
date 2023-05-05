import psycopg2


class DB:

    con = psycopg2.connect(
        dbname = "online_shop",
        user = "postgres",
        password = "2",
        host = "localhost",
        port = "5432"
    )

    cur = con.cursor()


    def select(self , **where):

        fields = ','.join(self.fields)
        table_name = self.__class__.__name__
        query = f"""select {fields} from {table_name }"""

        f = f' where {list(where.keys())[0]} = %s'
        query += f
        param = tuple(where.values())
        print(query)
        self.cur.execute(query , param)
        result = self.cur.fetchall()
        return result

    def insert_into(self , **params):
        pass

class Users(DB):
    def __init__(self, *fields):
        self.fields = fields

class Students(DB):
    def __init__(self, *fields):
        self.fields = fields

user1 = Users("id" ,"phone").select(id  = 5)
# user1 = Users().insert_into(id = 6 , name = "javogir")
print(user1)





# query = """select * from users where id = %s"""



