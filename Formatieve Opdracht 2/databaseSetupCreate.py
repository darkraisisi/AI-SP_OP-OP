import psycopg2


""" Run this file to generate the whole database, you only need to personify the parameters of the postgresql database to acces your database """


connection = psycopg2.connect(user="postgres",
                              password="root",
                              host="localhost",
                              port="5432",
                              database="OpisOp")
cursor = connection.cursor()

cursor.execute(
<<<<<<< HEAD
            """DROP TABLE IF EXISTS brand CASCADE;

            CREATE  TABLE IF NOT EXISTS brand (
            id SERIAL ,
            name VARCHAR(255) NOT NULL ,
            PRIMARY KEY (id) )"""
)

cursor.execute(
            """DROP TABLE IF EXISTS products CASCADE;

                CREATE TABLE IF NOT EXISTS products (
                    id INT NOT NULL ,
=======
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
>>>>>>> c7c39c2d46b66c1d5a7fa61ebc0c517db0c9315e
                    name VARCHAR(255) NULL ,
                    gender VARCHAR(255) NULL ,
                    category VARCHAR(255) NULL ,
                    subcategory VARCHAR(255) NULL ,
                    subsubcategory VARCHAR(255) NULL ,
<<<<<<< HEAD
                    brand_id INT,

                    PRIMARY KEY (id),
                    CONSTRAINT fk_products_brand1
                    FOREIGN KEY (brand_id)
                    REFERENCES brand (id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE)"""
=======
                    brand_id INT NOT NULL ,
            PRIMARY KEY (id),
            FOREIGN KEY (brand_id )
            REFERENCES brand (id ) );
            """
>>>>>>> c7c39c2d46b66c1d5a7fa61ebc0c517db0c9315e
)

cursor.execute(
<<<<<<< HEAD
            """DROP TABLE IF EXISTS profiles CASCADE;
=======
            """DROP TABLE IF EXISTS profiles CASCADE ;
>>>>>>> c7c39c2d46b66c1d5a7fa61ebc0c517db0c9315e

                CREATE TABLE IF NOT EXISTS profiles (
                    id VARCHAR(255) NOT NULL ,
                    order_amount INT NOT NULL DEFAULT 0 ,
            PRIMARY KEY (id) );
"""
)

cursor.execute(
<<<<<<< HEAD
            """DROP TABLE IF EXISTS sessions CASCADE;

                CREATE TABLE IF NOT EXISTS sessions (
                    id INT NOT NULL ,
                    browser_id VARCHAR(255) NOT NULL ,
                    segment VARCHAR(255) NULL ,
                    profiles_id INT NOT NULL ,
            PRIMARY KEY (id) ,
            CONSTRAINT fk_sessions_profiles1
            FOREIGN KEY (profiles_id)
            REFERENCES profiles (id)
=======
            """DROP TABLE IF EXISTS sessions CASCADE ;

                CREATE TABLE IF NOT EXISTS sessions (
                    id VARCHAR(255) NOT NULL ,
                    browser_id VARCHAR(255) NOT NULL ,
                    segment VARCHAR(45) NULL ,
                    profiles_id VARCHAR(255) NOT NULL ,
            PRIMARY KEY (id) ,
            FOREIGN KEY (profiles_id )
            REFERENCES profiles (id )
>>>>>>> c7c39c2d46b66c1d5a7fa61ebc0c517db0c9315e
            ON DELETE NO ACTION
            ON UPDATE NO ACTION);
"""
)

cursor.execute(
<<<<<<< HEAD
            """DROP TABLE IF EXISTS cart_has_products CASCADE;

                CREATE TABLE IF NOT EXISTS cart_has_products (
                    products_id INT NOT NULL ,
                    sessions_id INT NOT NULL ,
                    bought BOOLEAN NOT NULL ,
=======
            """DROP TABLE IF EXISTS cart CASCADE ;

                CREATE TABLE IF NOT EXISTS cart(
                    products_id VARCHAR(255) NOT NULL ,
                    sessions_id VARCHAR(255) NOT NULL ,
                    bought VARCHAR(255) NOT NULL ,
>>>>>>> c7c39c2d46b66c1d5a7fa61ebc0c517db0c9315e
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