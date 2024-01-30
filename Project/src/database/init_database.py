import sqlite3

dbname = 'applications.db'

def create_table():
    connection = sqlite3.connect(dbname)

    connection.execute("DROP TABLE IF EXISTS applications")
    connection.execute("""\
    CREATE TABLE applications
    (ID          INTEGER PRIMARY KEY AUTOINCREMENT,
     NAME		 TEXT NOT NULL,
     VERSION	 TEXT NOT NULL);""")

    connection.commit()

    connection.close()

def fill_database():
    connection = sqlite3.connect(dbname)

    connection.execute("INSERT INTO applications (name, version) VALUES ('Kibana', '17.8.1')")
    connection.execute("INSERT INTO applications (name, version) VALUES ('Confluence', '7.2')")

    connection.commit()

    connection.close()


def read_database():
    connection = sqlite3.connect(dbname)

    cursor = connection.execute("SELECT * FROM applications")

    # display all data from hotel table
    for row in cursor:
        print(row)

    connection.close()

# --------------------------

# create_table()
fill_database()
read_database()