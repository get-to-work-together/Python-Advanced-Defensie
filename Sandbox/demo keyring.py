import keyring
from getpass import getpass

# keyring.set_password("DB_REMOTE", "peter", "welkom!123")

# password = keyring.get_password("DB_REMOTE", "peter")
# password = keyring.get_password("pgAdmin4", "pgAdmin4-postgres-1")


password = keyring.get_password("MySecretDB", "ABCDE")

if password is None:
    password = getpass('Wat is jouw master password? ')
    keyring.set_password("MySecretDB", "ABCDE", password)

print(password)



