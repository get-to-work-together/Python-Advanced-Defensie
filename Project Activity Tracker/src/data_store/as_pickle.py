import sys
import os
import pickle
from datetime import date

sys.path.append(r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Activity Tracker/src')
from models.activity import Activity
from repository.repository import ActivityRepository


directory = r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Activity Tracker/data'
filename = 'data.pickle'


def store_repository(repository):
    full_path = os.path.join(directory, filename)
    with open(full_path, 'wb') as f:
        pickle.dump(repository, f)


def retrieve_repository():
    full_path = os.path.join(directory, filename)
    with open(full_path, 'rb') as f:
        return pickle.load(f)


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