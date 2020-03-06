import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="root",
                              host="localhost",
                              port="5432",
                              database="OpisOp")
cursor = connection.cursor()
cursor.execute(
            """ DROP TABLE IF EXISTS test1 CASCADE;
                DROP TABLE IF EXISTS test2 CASCADE;
            """
)
cursor.execute(
            """CREATE TABLE test1 (
                test01 varchar(255),
                test02 varchar(255),
                test03 varchar(255),
                test04 varchar(255),
                test05 varchar(255)
            );"""
)
cursor.execute(
            """CREATE TABLE test2 (
                test01 varchar(255),
                test02 varchar(255),
                test03 varchar(255),
                test04 varchar(255),
                test05 varchar(255)
            );"""
)

connection.commit()
cursor.close()
connection.close()
print("PostgreSQL datebase is made")