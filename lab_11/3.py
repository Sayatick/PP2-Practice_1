import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="123456"
)
cur = conn.cursor()

procedure_sql = """
CREATE OR REPLACE PROCEDURE insert_users_with_check(
    names TEXT[],
    phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    invalid_entries TEXT := '';
BEGIN
    FOR i IN 1 .. array_length(names, 1) LOOP
        IF phones[i] ~ '^[0-9]+$' AND length(phones[i]) >= 5 THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = names[i]) THEN
                UPDATE phonebook SET phone = phones[i] WHERE name = names[i];
            ELSE
                INSERT INTO phonebook(name, phone) VALUES(names[i], phones[i]);
            END IF;
        ELSE
            invalid_entries := invalid_entries || format('(%s, %s), ', names[i], phones[i]);
        END IF;
    END LOOP;

    RAISE NOTICE 'Invalid entries: %', invalid_entries;
END;
$$;
"""

cur.execute(procedure_sql)
conn.commit()
print("Procedure created.")

name_input = input("Enter names: ")
phone_input = input("Enter phones: ")

names = name_input.strip().split(',')
phones = phone_input.strip().split(',')

cur.execute("CALL insert_users_with_check(%s, %s);", (names, phones))
conn.commit()
print("Data processed!")

cur.close()
conn.close()