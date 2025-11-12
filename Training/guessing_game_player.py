"""Dit is documentatie van mijn module.

Let the computer play the guessing game.
"""

upper = 100
lower = 1

print('Ik ga een getal raden tussen 1 en 100')

aantal_keer_geraden = 0
while True:
    # strategy: guess half way between lower and lower bounds
    gok = (lower + upper) // 2

    response = input(f'Is het getal {gok}? [h]oger, [l]ager of [y]es: ')
    aantal_keer_geraden += 1

    if response.lower().startswith('h'):
        lower = gok + 1

    elif response.lower().startswith('l'):
        upper = gok - 1

    else:
        print(f'Ik heb het geraden in {aantal_keer_geraden} keer!')
        break