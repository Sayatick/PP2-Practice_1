import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook_db",
    user = "postgres",
    password = "123456"
)

cur = conn.cursor()

with open("lab_10/file1.csv", "r") as file:
    for line in file:
        name, phone_n = line.strip().split(",")
        cur.execute("""INSERT INTO phonebook(name, phone) VALUES(%s, %s)""", (name, phone_n))

conn.commit()

cur.close()
conn.close()