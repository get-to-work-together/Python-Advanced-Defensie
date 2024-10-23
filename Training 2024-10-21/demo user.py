import hashlib
import re

available_roles = ['admin', 'standard', 'keyuser']


class InvalidEmailException(Exception):
    pass


class InvalidRoleException(Exception):
    pass


class User:
    """User class

    Attributes: username, name, email, role, password

    :raises
    InvalidEmailException
    InvalidRoleException
    """
    def __init__(self, username, name, email, role='standard', password = None):
        self._username = username
        self._name = name
        self.email = email
        self.role = role
        if password is not None:
            self.set_password(password)

    def __str__(self):
        return f'User: {self._username}'

    # getters

    @property
    def username(self):
        return self._username

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def role(self):
        return self._role

    # setters

    @name.setter
    def name(self, value):
        self._name = value

    @email.setter
    def email(self, value):
        email_regex = r'\w+@\w+\.\w{2,3}'
        if re.match(email_regex, value):
            self._name = value
        else:
            raise InvalidEmailException(f'Invalid e-mail.')


    @role.setter
    def role(self, value):
        if value in available_roles:
            self._role = value
        else:
            raise InvalidRoleException(f'Role "{value}" does not exist. Available roles are: {available_roles}')

    # other methods

    def set_password(self, password):
        self._password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self._password_hash == hashlib.sha256(password.encode()).hexdigest()

    # class wide methods

    @staticmethod
    def generate_anomynous_user():
        return User('anonymous', 'Anonymous', 'anonymous@gmail.com')



# -------------------------------

if __name__ == '__main__':

    username = input('Geef gebruikersnaam: ')
    name = input('Geef naam: ')
    email = input('Geef email: ')
    role = input('Geef rol: ')
    password = input('Geef wachtwoord: ')

    while True:
        try:

            user1 = User(username = username,
                         name = name,
                         email = email,
                         role = role,
                         password = password)

            print('User created!')

            print(user1.__dict__)

            break

        except InvalidEmailException as ex:
            print(ex)
            email = input('Geef email: ')

        except InvalidRoleException as ex:
            print(ex)
            role = input('Geef rol: ')

    user2 = User(username='jan',
                 name='Jan',
                 email='dfsjklh',
                 role='x',
                 password='abc')

    while True:
        user_input = input('Geef wachtwoord: ')
        if user1.check_password(user_input):
            print('Welkom. That was the correct password.')
            break
        else:
            print('Incorrect')


