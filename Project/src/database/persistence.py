import sqlite3

dbname = 'applications.db'


def save_application_record(name, version):
    sql = "INSERT INTO applications (name, version) VALUES (?, ?)"
    connection = sqlite3.connect(dbname)
    connection.execute(sql, (name, version))
    connection.commit()
    connection.close()


def get_all_application_records():
    sql = "SELECT * FROM applications"
    connection = sqlite3.connect(dbname)
    result = connection.execute(sql).fetchall()
    connection.commit()
    connection.close()
    return result


def remove_application_record(name):
    sql = "DELETE FROM applications WHERE name = ?"
    connection = sqlite3.connect(dbname)
    connection.execute(sql, (name,))
    connection.commit()
    connection.close()


# -----

if __name__ ==  '__main__':
    # save_application_record('XXX', 'Version 3')
    remove_application_record('XXX')
    print(get_all_application_records())