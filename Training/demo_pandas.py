import pandas as pd
import sqlite3
from io import StringIO


print(pd.__version__)

pd.set_option('display.max_rows', 1000)

data = [
    {'Voornaam': 'Arthur', 'Achternaam': 'Samson', 'Woonplaats': 'Utrecht'},
    {'Voornaam': 'Nick', 'Achternaam': 'Waltmans', 'Woonplaats': 'Arnhem'},
    {'Voornaam': 'Peter', 'Achternaam': 'Anema', 'Woonplaats': 'Lhee'},
    {'Voornaam': 'Charlotte', 'Achternaam': 'Boersma', 'Woonplaats': 'Lhee'},
]

df = pd.DataFrame(data)

# filter
print(df.query('Achternaam.str.contains("a")'))

# sorteer
print(df.sort_values('Achternaam'))

# nieuw kolom
df['Naam'] = (df['Voornaam'] + ' ' + df['Achternaam']).str.upper()
print(df.sort_values('Achternaam'))

# ==============

conn = sqlite3.connect('student.db')
df = pd.read_sql(con=conn, sql='SELECT * FROM students;')
conn.close()

print(df)

# =============

df = pd.read_csv('ca-500.csv', sep=';')
print(df[['first_name','last_name','city']].query('city=="Montreal"'))

print(df['city'].value_counts().head(10))

# ===============

# url = 'https://nl.wikipedia.org/wiki/Provincies_van_Nederland'
#
# f = StringIO(url) # StringIO object
# df = pd.read_html(f)
#
# print(type(df))
