"""CRUD (Create, Read, Update, Delete) operations for user"""

from models.user import User

import sqlite3

db_filename = 'users.db'


def create_user_table():
    conn = sqlite3.connect(db_filename)

    sql = '''\
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100),
    email VARCHAR(100) NOT NULL,
    role VARCHAR(50),
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);    
    '''

    conn.execute(sql)

    conn.commit()

    conn.close()


def save_user(user: User):
    conn = sqlite3.connect(db_filename)

    sql = '''\
INSERT INTO users (username, name, email, role, password_hash)   
VALUES (?, ?, ?, ?, ?);
    '''

    try:
        conn.execute(sql, (user.username, user.name, user.email, user.role, user._password_hash))

    except Exception as ex:
        print(ex)

    finally:
        conn.commit()
        conn.close()


def get_user(id: int):
    conn = sqlite3.connect(db_filename)

    sql = '''\
    SELECT * FROM users WHERE id=?;'''

    cursor = conn.cursor()
    cursor.execute(sql, (id,))

    record = cursor.fetchone()

    conn.commit()

    conn.close()

    if record:
        id, username, name, email, role, password_hash, created = record

        user = User(username, name, email, role, id = id)
        user._password_hash = password_hash

        return user


def get_users():
    conn = sqlite3.connect(db_filename)

    sql = '''\
SELECT * FROM users;'''

    cursor = conn.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()

    conn.commit()

    conn.close()

    users = []
    if records:
        for record in records:
            id, username, name, email, role, password_hash, created = record

            user = User(username, name, email, role, id = id)
            user._password_hash = password_hash

            users.append(user)

    return users


def delete_user(id: int):
    conn = sqlite3.connect(db_filename)

    sql = 'DELETE FROM users WHERE id=?;'

    cursor = conn.cursor()
    cursor.execute(sql, (id,))

    conn.commit()

    conn.close()


def update_user():
    pass


if __name__ == '__main__':
    create_user_table()

    try:
        user = User('peter8', 'Peter Anema', 'peter@tip.nl', 'standard', 'Welkom!123')
        save_user(user)
    except Exception as ex:
        print(ex)

    delete_user(8)

    users = get_users()
    for user in users:
        print(user)

    print()
    print(get_user(7))
