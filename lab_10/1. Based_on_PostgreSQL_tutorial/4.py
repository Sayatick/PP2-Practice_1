import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook_db",
    user = "postgres",
    password = "123456"
)

cur = conn.cursor()

print("1 - showing exact name\n2 - showing name starting with...\n3 - showing exact phone number\n4 - showing phone number starting with...\n5 - show all data")
choice = input("PLEASE choose what query you need :) -> ")

if choice == "1":
    name = input("Enter name: ")
    cur.execute("""SELECT * FROM phonebook WHERE name = %s""", (name,))
elif choice == "2":
    name_st = input("Enter starting letters of name: ")
    cur.execute("""SELECT * FROM phonebook WHERE name LIKE %s""", (name_st + '%s',))
elif choice == "3":
    phone_n = input("Enter phone number: ")
    cur.execute("""SELECT * FROM phonebook WHERE phone = %s""", (phone_n,))
elif choice == "4":
    phone_st = input("Enter starting digits of phone number: ")
    cur.execute("""SELECT * FROM phonebook WHERE phone LIKE %s""", (phone_st + '%s',))
elif choice == "5":
    cur.execute("""SELECT * FROM phonebook""")
else:
    print("You entered wrong option, try again!")    

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()