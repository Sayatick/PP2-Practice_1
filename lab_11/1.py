import psycopg2

def do_sql():
    conn = psycopg2.connect(
        host="localhost",
        dbname="phonebook_db",
        user="postgres",
        password="123456"
    )
    cur = conn.cursor()

    pattern = input("Enter part of name or phone number: ")

    cur.execute("""
        SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s""", (f"%{pattern}%", f"%{pattern}%"))

    results = cur.fetchall()
    if results:
        print("Results found:")
        for row in results:
            print("ID: ",row[0], " Name: ",row[1]," Phone: ",row[2])
    else:
        print("No data found.")
    cur.close()
    conn.close()
    
do_sql()