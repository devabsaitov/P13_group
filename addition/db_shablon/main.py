import psycopg2


class AbstractClass:
    con = psycopg2.connect(
        dbname = 'online_shop',
        user = 'postgres',
        password = 2,
        host = 'localhost',
        port = 5432
    )

    cur = con.cursor()

    def select(self ,  **params):

        fields = ','.join(self.fields) if self.fields else '*'
        table_name = self.__class__.__name__
        query = f"""select {fields} from {table_name}"""
        if params:
            str_ = ''
            for i in params.items():
                str_ += f"{i[0]}=%s"
            query += f" where {str_};"
        self.cur.execute(query, tuple(params.values()))
        return self.cur

    def insert_into(self , **params):
        fields = ','.join(params.keys())
        params = ','.join(list(params.values()))
        table_name = self.__class__.__name__

        query = f"""insert into {table_name}({fields}) values ({params})"""
        self.cur.execute(query)
        self.con.commit()


class Users(AbstractClass):
    def __init__(self , *args):
        self.fields = args


class Students(AbstractClass):
    def __init__(self, *args):
        self.fields = args


obj = Users().insert_into(id = '5' , name = "'Furqat'" , phone = '+998993456787' , gender = "'E'")
print(obj)



# params = {"id" : 3 , "name" : "St
# print(str_)
