import hashlib


class User:

    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        self.password_hash = None

    def __str__(self):
        return f'User: {self.username}'

    def set_password(self, password):
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()


# -------------------------------

user1 = User('panema', 'Peter Anema', 'email@peteranema.nl')

user1.set_password('Welkom!123')

print(user1)

print(user1.__dict__)

while True:
    user_input = input('Geef wachtwoord: ')
    if user1.check_password(user_input):
        print('Welkom. That was the correct pasword.')
        break
    else:
        print('Incorrect')
