from console.input_user import get_user


if __name__ == '__main__':
    user = get_user()

    print(user)
    print(user.__dict__)

    while True:
        user_input = input('Geef wachtwoord: ')
        if user.check_password(user_input):
            print('Welkom. That was the correct password.')
            break
        else:
            print('Incorrect')
