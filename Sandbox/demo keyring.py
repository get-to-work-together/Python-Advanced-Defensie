import keyring
from getpass import getpass

# keyring.set_password("DB_REMOTE", "peter", "welkom!123")

# password = keyring.get_password("DB_REMOTE", "peter")
# password = keyring.get_password("pgAdmin4", "pgAdmin4-postgres-1")

system = "MySecretDB"
account_name = "ABCDE"

password = keyring.get_password(system, account_name)

if password is None:
    password = getpass(f'Wat is jouw password voor {system}? ')
    keyring.set_password(system, account_name, password)

print(password)



