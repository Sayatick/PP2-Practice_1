import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="123456"
)
cur = conn.cursor()

pagination_function_sql = """
CREATE OR REPLACE FUNCTION get_paginated_records(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, phone
    FROM phonebook
    ORDER BY id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;
"""

cur.execute(pagination_function_sql)
conn.commit()
print("Pagination function created successfully.\n")

limit = int(input("Enter how many records to display per page (LIMIT): "))
offset = int(input("Enter how many records to skip (OFFSET): "))

cur.execute("SELECT * FROM get_paginated_records(%s, %s);", (limit, offset))
rows = cur.fetchall()

print("\nPaginated Results:")
if rows:
    for row in rows:
        print("ID: ", row[0]," Name:", row[1]," Phone: ", row[2])
else:
    print("No data found!")

cur.close()
conn.close()