import string
import random

filename = 'basiswoorden-gekeurd.txt'

word_length = 6

words = []
with open(filename) as f:
    for line in f:
        line = line.rstrip('\n')
        if any(digit in line for digit in string.digits + string.punctuation):
            continue
        if len(line) == word_length:
            words.append(line.lower())

# print(f'Found {len(words)} words with {word_length} letters.')

secret_word = random.choice(words).upper()

# print(secret_word)

# poging = 1
# while True:
#     guess = input(f'Geef een woord (poging {poging}): ').upper()
#     poging += 1
#
#     if len(guess) != word_length:
#         print('Verkeerde lengte!')
#         continue
#     elif guess.lower() not in words:
#         print('Niet een bestaand woord!')
#         continue
#
#     for letter_guess, letter_secret in zip(guess, secret_word):
#         if letter_guess == letter_secret:
#             print(letter_guess.upper(), end=' ')
#         else:
#             print('_', end=' ')
#
#     print()
#
#     if guess == secret_word:
#         print(f'Goed geraden! Het woord was inderdaad {secret_word}. Daar heb je {poging - 1} pogingen voor nodig gehad.')
#         break



letters = set()
poging = 1
while True:
    guess = input(f'Geef het woord of vraag een letter: ').upper()
    poging += 1

    if guess == '?':
        remaining_letters = set(secret_word) - set(letters)
        guess = random.choice(list(remaining_letters))

    if len(guess) == 1:
        letters.add(guess)

    elif guess.lower() not in words:
        print('Niet een bestaand woord!')
        continue

    elif len(guess) != word_length:
        print('Verkeerde lengte!')
        continue

    else:
        letters.update(list(guess))

    aantal_goed = 0
    for letter in secret_word:
        if letter in letters:
            print(letter.upper(), end=' ')
            aantal_goed += 1
        else:
            print('_', end=' ')

    print()

    if aantal_goed == len(secret_word):
        print(f'Goed geraden! Het woord was inderdaad {secret_word}. Daar heb je {poging - 1} pogingen voor nodig gehad.')
        break
