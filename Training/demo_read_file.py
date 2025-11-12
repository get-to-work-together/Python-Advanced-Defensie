import re
import string

filename = '../Datasets/basiswoorden-gekeurd.txt'


def can_be_formed(word: str, letters: str):
    for c in word:
        if c in letters:
            if word.count(c) > letters.count(c):
                return False
        else:
            return False
    return True


def get_matches(pattern: str = '.*',
                avalaible_letters: str = string.ascii_lowercase):
    words = []
    with open(filename) as f:
        for line in f:
            line = line.strip().lower()
            if re.match(pattern, line) and can_be_formed(line, avalaible_letters):
                words.append(line)
    return words


# -------------------------------------------------

if __name__ == '__main__':

    pattern = input('Geef regular expression patroon: ')
    available_letters = input('Welke letters heb je: ')

    words = get_matches('^' + pattern + '$', available_letters)

    for word in words:
        print(word)



