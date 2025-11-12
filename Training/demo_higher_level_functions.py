
def maak_groet(language='nl'):
    def groet(aanhef):
        if language == 'nl':
            return f'Beste {aanhef}. Hoe gaat het?'
        elif language == 'en':
            return f'Dear {aanhef}. How do you do?'
    return groet

# --------------------------------

f = maak_groet('en')
print(f('Nienke'))
print(f('Mario'))

s = '20'
value = int(s, base=16)

from functools import partial

parse_hex = partial(int, base=16)

print(parse_hex(s))
print(f'{s} => {value}')

crazy_print = partial(print, end='😀\n')
crazy_print('Hello world')


import pandas as pd

filename = 'data.csv'
pd.read_csv(filename, sep=';', decimal=',', dayfirst=True)
read_csv_nl = partial(pd.read_csv, sep=';', decimal=',', dayfirst=True)
read_csv_nl(filename)