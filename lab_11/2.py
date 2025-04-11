import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="123456"
)
cur = conn.cursor()

n_name = input("Enter a new name: ")
n_phone = input("Enter a new phone number: ")

cur.execute("""SELECT * FROM phonebook""")
c_name = cur.fetchone()

if c_name:
    cur.execute("""UPDATE phonebook SET phone = %s WHERE name = %s""", (n_phone, n_name))
    print("Updated !!!")
else:
    cur.execute("""INSERT INTO phonebook(name, phone) VALUES(%s, %s)""", (n_name, n_phone))
    print("Inserted !!!")

conn.commit()

cur.close()
conn.close()