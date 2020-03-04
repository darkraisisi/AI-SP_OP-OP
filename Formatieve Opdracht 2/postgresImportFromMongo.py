import psycopg2
import random, os, json, urllib.parse, requests


connection = psycopg2.connect(user="postgres",
                              password="root",
                              host="localhost",
                              port="5432",
                              database="OpisOp")
cursor = connection.cursor()
sql = """INSERT INTO products (name)
VALUES ('zeep');
    """
cursor.execute(sql)
connection.commit()

cursor.close()
connection.close()
print("PostgreSQL connection is closed")