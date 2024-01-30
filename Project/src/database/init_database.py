import sqlite3

dbname = 'applications.db'

def create_table():
    connection = sqlite3.connect(dbname)

    connection.execute("DROP TABLE IF EXISTS applications")
    connection.execute("""\
    CREATE TABLE applications
    (ID          INT PRIMARY KEY NOT NULL,
     NAME		 TEXT NOT NULL,
     VERSION	 TEXT NOT NULL);""")

    connection.execute("INSERT INTO applications (id, name, version) VALUES (1, 'Kibana', '17.8.1')")
    connection.execute("INSERT INTO applications (id, name, version) VALUES (2, 'Confluence', '7.2')")

    connection.close()


def read_database():
    connection = sqlite3.connect(dbname)

    cursor = connection.execute("SELECT * FROM applications")

    # display all data from hotel table
    for row in cursor:
        print(row)

    connection.close()

# --------------------------

create_table()
read_database()