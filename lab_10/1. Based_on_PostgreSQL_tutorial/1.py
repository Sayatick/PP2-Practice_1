import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook_db",
    user = "postgres",
    password = "123456"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook(
        if SERIAL PRIMARY KEY,
        name VARCHAR(600),
        phone VARCHAR(20)
    )            
""")

name = input("Enter your name: ")
phone_n = input("Enter your phone number: ")
cur.execute("""
    INSERT INTO phonebook(name, phone) VALUES(%s, %s)""", (name, phone_n))

conn.commit()

cur.close()
conn.close()