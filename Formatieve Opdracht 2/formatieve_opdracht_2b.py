from pymongo import MongoClient
import psycopg2

dbstring = 'mongodb+srv://{0}:{1}@{2}/test?retryWrites=true&w=majority'
client = MongoClient()
database = client.huwebshop

products = database.products.find()

connection = psycopg2.connect(user="postgres",
                              password="root",
                              host="localhost",
                              port="5432",
                              database="OpisOp")
cursor = connection.cursor()

def transferAllProducts():
    for product in products:
        sql = f"INSERT INTO products (name,price) VALUES (%s,%s); "
        cursor.execute(sql,(product['name'],product['price']['discount']))
        connection.commit()    

transferAllProducts()

connection.close()