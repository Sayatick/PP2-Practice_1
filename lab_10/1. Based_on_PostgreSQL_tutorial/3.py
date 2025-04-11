import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook_db",
    user = "postgres",
    password = "123456"
)

cur = conn.cursor()

choice = input("What do you wanna update ? 'name' or 'phone' brother :) : ")

if choice == "name":
    cur_name = input("Which name ?: ")
    new_name = input("Enter your new name: ")
    cur.execute("""UPDATE phonebook set name = %s WHERE name = %s""", (new_name, cur_name))
elif choice == "phone":
    cur_phone_n = input("Which phone number?: ")
    new_phone_n = input("Enter your new phone number: ")
    cur.execute("""UPDATE phonebook set name = %s WHERE name = %s""", (new_phone_n, cur_phone_n))
else:
    "There are noother options :("

conn.commit()

cur.execute("""SELECT * FROM phonebook""")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()