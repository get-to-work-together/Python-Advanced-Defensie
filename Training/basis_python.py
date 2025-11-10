# Strings

s = 'dit is een string'

print(type(s))

print(s.upper())

print( s.index('t') )
print( s.index('t', 3) )
print( s.count('t') )

print(s[7:10])

print('regel 1\nregel 2\nregel 3')
print('''\
regel 1
regel 2
regel 3''')

print('\u20B2')
print('\U0001f383')
print('🎃')
print('\u2714')
print('✔')

naam = 'jan'
leeftijd = 45

print(f'{naam.capitalize()} is {leeftijd} jaar oud.')


# Datastructuren
# - list
# - tuple
# - set
# - dict

boodschappen = []         # lege lijst

boodschappen.append('brood')
boodschappen.append('eieren')
boodschappen.append('melk')

boodschappen.insert(0, 'bier')

print(boodschappen)
print(len(boodschappen))



# Flow control
# - if ... elif ... else
# - while
# - for

# Opdracht print alleen de woorden die langer zijn dan 3 letters

s = 'de kat krabt de krullen van de trap'
woorden = s.split()
for woord in woorden:
    if len(woord) > 3:
        print(woord)


magicnumber = 11
for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)






# Functies

counter = 0
while counter < 5:
    print('Hoi')
    print('Hoe gaat het?')
    print('Met mij goed.')
    counter += 1

for _ in range(5):
    print('Hoi')
    print('Hoe gaat het?')
    print('Met mij goed.')



def print_regels(naam, n=1):
    print(f'Hoi {naam * n}')
    print('Hoe gaat het?')
    print('Met mij goed.')

def bereken_bmi(gewicht, lengte):
    bmi = gewicht / lengte ** 2
    return bmi


print_regels('Peter')
print_regels('Mario')
print_regels('Kars', 5)
print_regels('Nienke', 4)
print_regels('Patrick')
print_regels('Ozcan', 4)

bmi = bereken_bmi(80, 1.82)
print( bmi )