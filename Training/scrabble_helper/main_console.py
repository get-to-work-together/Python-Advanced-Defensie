from src.models.scrabble_helper import get_matches

pattern = input('Geef regular expression patroon: ')
available_letters = input('Welke letters heb je: ')

words = get_matches('^' + pattern + '$', available_letters)

for word in words:
    print(word)
