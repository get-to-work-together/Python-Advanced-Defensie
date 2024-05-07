import sys
import os
import sqlite3
from datetime import date

sys.path.append(r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Activity Tracker/src')
from models.activity import Activity
from repository.repository import ActivityRepository


directory = r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Activity Tracker/data'
filename = 'data.db'


def create_table():
    sql = """\
CREATE TABLE IF NOT EXISTS activities (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    activity_type VARCHAR(50),
    date_due DATE,
    note VARCHAR(255),
    duration INT,
    object_id VARCHAR(20),
    object_name VARCHAR(50),
    assigned_to VARCHAR(50),
    date_entered DATE,
    status VARCHAR(20),
    date_updated DATE
);"""

    full_path = os.path.join(directory, filename)
    db = sqlite3.connect(full_path)
    db.execute(sql)
    db.close()


def store_activity(activity):

    full_path = os.path.join(directory, filename)
    conn = sqlite3.connect(full_path)
    cur = conn.cursor()

    fields = (
        # 'id',
        'name',
        'activity_type',
        'date_due',
        'note',
        'duration',
        'object_id',
        'object_name',
        'assigned_to',
        'date_entered',
        'status',
        'date_updated'
    )

    values = (
        activity._name,
        activity._activity_type,
        activity._date_due,
        activity._note,
        activity._duration,
        activity._object_id,
        activity._object_name,
        activity._assigned_to,
        activity._date_entered,
        activity._status,
        activity._date_updated
    )
    sql = f"INSERT INTO activities ({','.join(fields)}) VALUES (?,?,?,?,?,?,?,?,?,?,?);"
    cur.execute(sql, values)

    conn.commit()
    conn.close()


def store_repository(repository):
    for activity in repository._activities:
        store_activity(activity)

def retrieve_repository():
    ...



if __name__ == '__main__':

    # create_table()

    repository = ActivityRepository()

    repository.add(Activity('Testen', 'testen', date_due = date.today()))
    repository.add(Activity('Onderhoud', 'onderhoud', date_due = '2024-05-21'))
    repository.add(Activity('Retour', 'retour', days_due = 10))

    store_repository(repository)

    # repository = retrieve_repository()
    # repository.print_all()