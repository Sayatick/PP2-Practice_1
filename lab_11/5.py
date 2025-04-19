import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="123456"
)
cur = conn.cursor()

delete_proc_sql = """
CREATE OR REPLACE PROCEDURE delete_user_by_info(info TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = info OR phone = info;

    RAISE NOTICE 'Deleted records with name or phone = %', info;
END;
$$;
"""

cur.execute(delete_proc_sql)
conn.commit()
print("Delete procedure created.")

user_input = input("Enter username or phone number to delete: ")

cur.execute("CALL delete_user_by_info(%s);", (user_input,))
conn.commit()

print("If any records matched ", user_input, " they were deleted.")

cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()
print("\nRemaining data in phonebook:")
for row in rows:
    print("ID: ", row[0], " Name: ", row[1]," Phone: ", row[2])

cur.close()
conn.close()