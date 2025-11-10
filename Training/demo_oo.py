class Person:

    def __init__(self, name, residence='Onbekend'):
        # attributen
        self._name = name
        self._residence = residence
        self._pin = '1234'

    # methods
    def tell(self):
        print(f'Ik ben {self._name} en ik woon in {self._residence}.')

    def move(self, new_residence):
        self._residence = new_residence


# -----------------------------------------------

naam = input('Wat is jouw naam? : ')
woonplaats = input('Waar woon je? : ')

p1 = Person(naam, residence=woonplaats)

p1.tell()

Person.tell(p1)

p1.move('Soesterberg')
p1.tell()

print(p1._pin)
