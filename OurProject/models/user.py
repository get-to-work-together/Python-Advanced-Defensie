import hashlib
import re


from models.exceptions import *
from models.role import available_roles


class User:
    """User class

    Attributes: username, name, email, role, password

    :raises
    InvalidEmailException
    InvalidRoleException
    """
    def __init__(self, username, name, email, role='standard', password = None, id = None):
        self._username = username
        self._name = name
        self.email = email
        self.role = role
        if password is not None:
            self.set_password(password)
        self._id = id

    def __str__(self):
        return f'User {self._id}: {self._username} - {self._email}'

    def __repr__(self):
        return f'User {self._id}: {self._username} - {self._email}'

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
            self._email = value
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
