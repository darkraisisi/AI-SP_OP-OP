import psycopg2
import csv

connection = psycopg2.connect(user="postgres",
                              password="root",
                              host="localhost",
                              port="5432",
                              database="OpisOp")
cursor = connection.cursor()

<<<<<<< HEAD
# cursor.execute(
#             """COPY products (id,category,subcategory,subsubcategory,gender,name)
#                 FROM \'C:\\Users\\david\\Documents\\School\\HBO\\Blok C\\Structured Programming\\AI-SP_OP-OP\\products.csv\' 
#                 WITH DELIMITER ',' CSV HEADER
# """
# )

with open('products.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cursor.execute(
            """
            INSERT INTO brand(name)
            SELECT %s WHERE NOT EXISTS (
                SELECT 1 FROM brand WHERE name=%s
            );""",(row[6],row[6]))
            
        cursor.execute("SELECT id FROM brand WHERE name = %s ",(row[6], ))
        brand_id = cursor.fetchone()
        
        cursor.execute(
            """ 
            INSERT INTO products (id,name,gender,category,subcategory,subsubcategory,brand_id) 
            VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (id) DO NOTHING
            """,
            (row[0],row[1],row[2],row[3],row[4],row[5],brand_id[0]))
=======
cursor.execute(
            """INSERT INTO products VALUES (id,category,subcategory,subsubcategory,gender,name)
                FROM \' C:\\Users\\frisf\Documents\GitHub\AI-SP_OP-OP\Formatieve Opdracht 2\products.csv \' 
                WITH DELIMITER ',' CSV HEADER
"""
)
>>>>>>> c7c39c2d46b66c1d5a7fa61ebc0c517db0c9315e

connection.commit()
cursor.close()
connection.close()
print("Data imported.")
