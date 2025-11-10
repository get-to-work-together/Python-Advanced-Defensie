import random

geheim_getal = random.randint(1, 100)

print('Raad een getal tussen 1 en 100.')

while True:
    s = input('Wat denk je dat het getal is? : ')
    gok = int(s)

    if gok > geheim_getal:
        print('lager ...')

    elif gok < geheim_getal:
        print('hoger ...')

    else:
        print(f'Yes. Goed geraden. Het getal was inderdaad {geheim_getal}')
        break
