"""
CRUD operations to an SQLite Database

CRUD - Create, Read, Update, Delete
"""

import bcrypt

import sqlite3

try:
    from .user import User
    dbname = 'data/users.db'

except:
    from user import User
    project_path = '../../../'
    dbname = project_path + 'data/users.db'


def create_table():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = """\
    CREATE TABLE IF NOT EXISTS users (
        username	TEXT,
        password    TEXT,
        email	    TEXT,
        last_login	TEXT,
        active	    INTEGER DEFAULT 1,
        PRIMARY KEY (username));"""

    c.execute(sql)

    conn.commit()
    conn.close()


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())


def insert_user(user: User):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = """\
    INSERT OR IGNORE INTO users (username, password, email, last_login, active)
    VALUES (?, ?, ?, NULL, 1);"""

    password_hash = hash_password(user.password)

    c.execute(sql, (user.username, password_hash, user.email))

    conn.commit()
    conn.close()


def delete_user(username: str):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "DELETE FROM users WHERE username = ?;"

    c.execute(sql, (username, ))

    conn.commit()
    conn.close()


def block_user():
    pass

def select_user(username):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "SELECT * FROM users WHERE username = ?;"

    res = c.execute(sql, (username, ))

    data = res.fetchone()

    conn.commit()
    conn.close()

    user = User(*data)

    return user


def select_users():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "SELECT * FROM users;"

    res = c.execute(sql)

    data = res.fetchall()

    conn.commit()
    conn.close()

    users = [User(*row) for row in data]

    return users


def update_user():
    pass


def validate_password(username, password_to_check) -> bool:
    user = select_user(username)
    return bcrypt.checkpw(password_to_check.encode('utf8'), user.password)


if __name__ == '__main__':
    create_table()

    delete_user('Peter')
    delete_user('Daan')

    insert_user(User('Peter', 'p4ssw0rd', 'peter@tip.nl'))
    insert_user(User('Daan', 'p4ssw0rd', 'daan@tip.nl'))

    insert_user(User('PeterA', 'p4ssw0rd', 'peter@tip.nl'))

    delete_user('PeterA')

    insert_user(User('Peter', 'p4ssw0rd', 'peter@tip.nl'))

    result = select_user('Peter')
    print(result)

    result = select_users()
    print(result)

    print(validate_password('Peter', 'p4ssw0rd'))
    print(validate_password('Peter', 'wrong_p4ssw0rd'))
