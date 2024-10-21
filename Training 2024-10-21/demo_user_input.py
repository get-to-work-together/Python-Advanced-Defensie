from csv import DictWriter

# try:
#     naam = input('Geef naam: ')
#     adres = input('Geef adres: ')
#     postcode = input('Geef postcode: ')
#     plaats = input('Geef plaats: ')
#
#     with open('addressen_boek.csv', 'a') as f:
#         f.write(f'{naam}, {adres}, {postcode}, {plaats}\n')
#
# except:
#     print('OOPS!!')
#


d = dict()

d['naam'] = input('Geef naam: ')
d['adres'] = input('Geef adres: ')
d['postcode'] = input('Geef postcode: ')
d['plaats'] = input('Geef plaats: ')

# with open('addressen_boek.csv', 'a') as f:
#     line = ','.join(d.values())
#     f.write(line + '\n')



import csv

with open('addressen_boek.csv', 'a') as f:
    writer = csv.DictWriter(f, ['naam', 'adres', 'postcode', 'plaats'], delimiter=';', quotechar='"')
    writer.writerow(d)




