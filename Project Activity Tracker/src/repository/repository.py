import sys
import os
from datetime import date

sys.path.append(r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Activity Tracker/src')
from models.activity import Activity



class ActivityRepository:

    def __init__(self):
        self._activities = []

    def add(self, activity):
        self._activities.append(activity)

    def print_all(self):
        for activity in self._activities:
            print(activity.info())

    def to_json(self):
        return [activity.to_dict() for activity in self._activities]

    @classmethod
    def from_json(cls, list_of_activities):
        repo = ActivityRepository()
        for d in list_of_activities:
            repo.add( Activity.from_dict(d) )
        return repo


if __name__ == '__main__':

    repository = ActivityRepository()

    repository.add(Activity('Testen', 'testen', date_due = date.today()))
    repository.add(Activity('Onderhoud', 'onderhoud', date_due = '2024-05-21'))
    repository.add(Activity('Retour', 'retour', days_due = 10))

    print( *repository.to_json(), sep='\n' )
