import sys
import os
import json
from datetime import date

sys.path.append(r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Activity Tracker/src')
from models.activity import Activity
from repository.repository import ActivityRepository


directory = r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Activity Tracker/data'
filename = 'data.json'


def store_repository(repository):
    full_path = os.path.join(directory, filename)
    with open(full_path, 'w') as f:
        json.dump(repository.to_json(), f)


def retrieve_repository():
    full_path = os.path.join(directory, filename)
    with open(full_path, 'r') as f:
        return ActivityRepository.from_json(json.load(f))



if __name__ == '__main__':

    # repository = ActivityRepository()
    #
    # repository.add(Activity('Testen', 'testen', date_due = date.today()))
    # repository.add(Activity('Onderhoud', 'onderhoud', date_due = '2024-05-21'))
    # repository.add(Activity('Retour', 'retour', days_due = 10))
    #
    # store_repository(repository)

    repository = retrieve_repository()
    repository.print_all()