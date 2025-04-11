import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook_db",
    user = "postgres",
    password = "123456"
)
cur = conn.cursor()

c_data = input("Do you want to delete whole row or just 1 data (1/2)? ")
choice = input("Delete by phone or name (1/2)? ")
if choice == "1":
    d_data = input("Enter Phone number: ")
elif choice == "2":
    d_data = input("Enter your name: ")

if c_data == "1":
    cur.execute("""DELETE FROM phonebook WHERE name = %s or phone = %s """, (d_data, d_data))
    print("Data in the row deleted.")
elif c_data == "2":
    if choice == "1":
        cur.execute("""UPDATE phonebook SET phone = NULL WHERE phone = %s""", (d_data,))
        print("Name is deleted.")
    elif choice == "2":
        cur.execute("""UPDATE phonebook SET name = NULL WHERE name = %s """, (d_data,))
        print("Phone is deleted.")

conn.commit()

cur.execute("""SELECT * FROM phonebook""")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()