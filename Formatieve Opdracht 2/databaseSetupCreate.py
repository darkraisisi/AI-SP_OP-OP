import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="root",
                              host="localhost",
                              port="5432",
                              database="OpisOp")
cursor = connection.cursor()

cursor.execute(
            """DROP TABLE IF EXISTS products ;

                CREATE TABLE products (
                    id INT NOT NULL ,
                    name VARCHAR(45) NULL ,
                    gender VARCHAR(45) NULL ,
                    category VARCHAR(45) NULL ,
                    brand VARCHAR(45) NULL ,
            PRIMARY KEY (id) )"""
)
cursor.execute(
            """DROP TABLE IF EXISTS profiles ;

                CREATE  TABLE IF NOT EXISTS profiles (
                    id INT NOT NULL ,
                    order_amount INT NOT NULL DEFAULT 0 ,
            PRIMARY KEY (id) )
"""
)
cursor.execute(
            """DROP TABLE IF EXISTS sessions ;

                CREATE  TABLE IF NOT EXISTS sessions (
                    id INT NOT NULL ,
                    browser_id VARCHAR(45) NOT NULL ,
                    segment VARCHAR(45) NULL ,
                    profiles_id INT NOT NULL ,
            PRIMARY KEY (id) ,
            CONSTRAINT fk_sessions_profiles1
            FOREIGN KEY (profiles_id )
            REFERENCES profiles (id )
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
"""
)
cursor.execute(
            """DROP TABLE IF EXISTS cart_has_products ;

                CREATE  TABLE IF NOT EXISTS cart_has_products (
                    products_id INT NOT NULL ,
                    sessions_id INT NOT NULL ,
            PRIMARY KEY (products_id, sessions_id) ,
            CONSTRAINT fk_products_has_sessions_products
            FOREIGN KEY (products_id )
            REFERENCES products (id )
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
            CONSTRAINT fk_products_has_sessions_sessions1
            FOREIGN KEY (sessions_id )
            REFERENCES sessions (id )
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
"""
)


connection.commit()
cursor.close()
connection.close()
print("PostgreSQL datebase is made")