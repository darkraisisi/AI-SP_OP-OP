import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="root",
                              host="localhost",
                              port="5432",
                              database="OpisOp")
cursor = connection.cursor()

cursor.execute(
            """INSERT INTO products VALUES (id,category,subcategory,subsubcategory,gender,name)
                FROM 'C:\\Users\\frisf\Documents\GitHub\AI-SP_OP-OP\Formatieve Opdracht 2\products.csv'
                WITH DELIMITER ',' CSV HEADER
"""
)

connection.commit()
cursor.close()
connection.close()
print("Data imported.")
