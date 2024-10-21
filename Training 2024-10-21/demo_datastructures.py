# lists

lijst = ['boter', 'kaas', 'eieren']

print( type(lijst) )
print( len(lijst) )

lijst.append('melk')
lijst.insert(0, 'bier')

print( lijst )

print( lijst[2:] )

print( lijst.pop() )
print( lijst )

nieuw = []
for item in lijst:
    nieuw.append(len(item))
print(nieuw)

# list comprehension

nieuw = [len(item) for item in lijst]
print(nieuw)

nieuw = [len(item) for item in lijst if item.startswith('b')]
print(nieuw)


nieuw = (len(item) for item in lijst if item.startswith('b'))
print(nieuw)


