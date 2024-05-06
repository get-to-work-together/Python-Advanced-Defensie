from datetime import date, datetime


def to_date(date_arg=None, format='%Y-%m-%d'):
    if date_arg is None:
        return date.today()
    if isinstance(date_arg, date):
        return date_arg
    elif isinstance(date_arg, str):
        return datetime.strptime(date_arg, format).date()
