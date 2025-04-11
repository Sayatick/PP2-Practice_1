import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="123456"
)
cur = conn.cursor()

users = [
    ("Alice", "123456"),
    ("Bob", "abc123"), # no correct
    ("Charlie", "9876543210"),
    ("David", "9876"), # no correct
    ("Eve", "1234567890123456") # no correvt
]

NO_correct_data = []

for name, phone in users:
    if phone.isdigit() and 5 <= len(phone) <= 15:
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
        existing = cur.fetchone()
        if existing:
            cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
        else:
            cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s)", (name, phone))
    else:
        NO_correct_data.append((name, phone))

conn.commit()

if NO_correct_data:
    print("NO correct:")
    for entry in NO_correct_data:
        print("Name: ", entry[0]," Phone: ", entry[1])
else:
    print("All datas were correct.")

cur.close()
conn.close()