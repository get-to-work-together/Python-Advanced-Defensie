from models.user import User
from models.exceptions import *


def get_user():

    username = input('Geef gebruikersnaam: ')
    name = input('Geef naam: ')
    email = input('Geef email: ')
    role = input('Geef rol: ')
    password = input('Geef wachtwoord: ')

    while True:
        try:

            return User(username = username,
                         name = name,
                         email = email,
                         role = role,
                         password = password)

        except InvalidEmailException as ex:
            print(ex)
            email = input('Geef email: ')

        except InvalidRoleException as ex:
            print(ex)
            role = input('Geef rol: ')
