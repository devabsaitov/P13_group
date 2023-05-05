import psycopg2

con = psycopg2.connect(
    host = 'localhost',
    dbname="p13_db",
    user="postgres",
    password=1
)

cur = con.cursor()
query = """insert into product(title , price) values ('Nimadir' , '50000')"""

cur.execute(query)
con.commit()
con.close()


