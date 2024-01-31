from Project.src.database import persistence


def get_applications():
    applications = persistence.get_all_application_records()
    temp = []
    for id, name, version in applications:
        t = version.split('.')
        if len(t) == 1:
            t += ('', '')
        elif len(t) == 2:
            t += ('',)
        major, minor, rev = t
        temp.append((name, major, minor, rev))
    return temp

def get_applications():
    applications = persistence.get_all_application_records()
    for id, name, version in applications:
        t = version.split('.')
        if len(t) == 1:
            t += ('', '')
        elif len(t) == 2:
            t += ('',)
        major, minor, rev = t
        yield (name, major, minor, rev)
