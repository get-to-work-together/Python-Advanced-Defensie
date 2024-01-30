import sqlite3

dbname = 'applications.db'


def save_application_record(name, version):
    sql = "INSERT INTO applications (name, version) VALUES (?, ?)"

    connection = sqlite3.connect(dbname)
    connection.execute(sql, (name, version))
    connection.commit()
    connection.close()


# -----

if __name__ ==  '__main__':
    save_application_record('XXX', 'Version 3')
