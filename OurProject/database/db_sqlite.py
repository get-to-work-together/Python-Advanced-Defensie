"""CRUD (Create, Read, Update, Delete) operations for user"""

import sqlite3

db_filename = 'users.db'


def create_user_table():
    conn = sqlite3.connect(db_filename)

    sql = '''\
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);    
    '''

    conn.execute(sql)


def save_user():
    pass


def get_user():
    pass


def get_users():
    pass


def delete_user():
    pass


def update_user():
    pass


if __name__ == '__main__':
    create_user_table()