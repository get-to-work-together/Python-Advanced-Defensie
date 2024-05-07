import sys

sys.path.append(r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Activity Tracker/src')

from utils.utils import to_date

from datetime import date, datetime, timedelta

from dataclasses import dataclass
from typing import List



class Activity:

    def __init__(self,
                 name: str,
                 activity_type: str,
                 date_due: date|str = None,
                 days_due: int = None,
                 note: str = None,
                 duration: int = 0,
                 object_id: str = None,
                 object_name: str = None,
                 assigned_to: str = None,
                 date_entered: date|str = None,
                 status: str = 'open',
                 date_updated: date|str = None):

        self._name = name
        self._note = note
        self._activity_type = activity_type
        self._duration = duration
        self._object_id = object_id
        self._object_name = object_name
        self._assigned_to = assigned_to

        if date_due is not None:
            self._date_due = to_date(date_due)
        elif days_due is not None:
            self._date_due = to_date(date.today() + timedelta(days = days_due))
        else:
            self._date_due = None

        self._date_entered = to_date(date_entered)
        self._status = status
        self._date_updated = to_date(date_updated)

    def info(self):
        return f'{self._activity_type} - {self._name} | due: {self._date_due} status: {self._status} on {self._date_updated}'

    def to_dict(self):
        d = {k[1:]: v if k.startswith('_') else k for k, v in self.__dict__.items()}
        d['date_due'] = d['date_due'].strftime('%Y-%m-%d')
        d['date_entered'] = d['date_entered'].strftime('%Y-%m-%d')
        d['date_updated'] = d['date_updated'].strftime('%Y-%m-%d')
        return d

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    @staticmethod
    def from_dict(d):
        return Activity(**d)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.title()


    def update(self, status, note = None):
        self._status = status
        self._date_updated = date.today()
        if note:
            self._note += '\n' + note + '\n'


if __name__ == '__main__':

    activity = Activity('Ophalen boek',
                        'geleend retour',
                        date.today() + timedelta(days = 14))

    print(activity.info())

    activity.update('done')

    print(activity.info())

    activity = Activity('Ophalen boek',
                        'geleend retour',
                        date_due = '2024-05-10')

    print(activity.info())

    activity.name = 'hacked by peter'
    print(activity.name)

