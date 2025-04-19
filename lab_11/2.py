import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="123456"
)
cur = conn.cursor()

procedure_sql = """
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;
"""

cur.execute(procedure_sql)
conn.commit()
print("Procedure created successfully.")

name = input("Enter name: ")
phone = input("Enter phone: ")

cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
conn.commit()
print("Procedure executed.")
cur.close()
conn.close()