import psycopg2

def show_page(limit, offset):
    conn = psycopg2.connect(
        host="localhost",
        dbname="phonebook_db",
        user="postgres",
        password="123456"
    )
    cur = conn.cursor()

    cur.execute("""SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s""", (limit, offset))

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print("ID: ", row[0], "Name: ", row[1], "Phone: ",row[2])
    else:
        print("No data found for this page.")

    cur.close()
    conn.close()

page = int(input("Enter page number: "))
limit = 2
offset = (page - 1) * limit

show_page(limit, offset)