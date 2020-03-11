import psycopg2


""" Run this file to generate the whole database, you only need to personify the parameters of the postgresql database to acces your database """


connection = psycopg2.connect(user="postgres",
                              password="niels16",
                              host="localhost",
                              port="5432",
                              database="OpisOp")
cursor = connection.cursor()

cursor.execute(
    """
        DROP TABLE IF EXISTS brand CASCADE ;

        CREATE  TABLE IF NOT EXISTS brand (
            id SERIAL, 
            name VARCHAR(45) NOT NULL ,
            PRIMARY KEY (id) );
    """
)

cursor.execute(
            """DROP TABLE IF EXISTS products CASCADE ;

                CREATE TABLE IF NOT EXISTS products (
                    id VARCHAR(255) NOT NULL ,
                    name VARCHAR(45) NULL ,
                    gender VARCHAR(45) NULL ,
                    category VARCHAR(45) NULL ,
                    subcategory VARCHAR(45) NULL ,
                    subsubcategory VARCHAR(45) NULL ,
                    brand_id INT NOT NULL ,
            PRIMARY KEY (id),
            FOREIGN KEY (brand_id )
            REFERENCES brand (id ) );
            """
)
cursor.execute(
            """DROP TABLE IF EXISTS profiles CASCADE ;

                CREATE TABLE IF NOT EXISTS profiles (
                    id VARCHAR(255) NOT NULL ,
                    order_amount INT NOT NULL DEFAULT 0 ,
            PRIMARY KEY (id) );
"""
)
cursor.execute(
            """DROP TABLE IF EXISTS sessions CASCADE ;

                CREATE TABLE IF NOT EXISTS sessions (
                    id VARCHAR(255) NOT NULL ,
                    browser_id VARCHAR(255) NOT NULL ,
                    segment VARCHAR(45) NULL ,
                    profiles_id VARCHAR(255) NOT NULL ,
            PRIMARY KEY (id) ,
            FOREIGN KEY (profiles_id )
            REFERENCES profiles (id )
            ON DELETE NO ACTION
            ON UPDATE NO ACTION);
"""
)
cursor.execute(
            """DROP TABLE IF EXISTS cart CASCADE ;

                CREATE TABLE IF NOT EXISTS cart(
                    products_id VARCHAR(255) NOT NULL ,
                    sessions_id VARCHAR(255) NOT NULL ,
                    bought VARCHAR(255) NOT NULL ,
            PRIMARY KEY (products_id, sessions_id) ,
            FOREIGN KEY (products_id )
            REFERENCES products (id )
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
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