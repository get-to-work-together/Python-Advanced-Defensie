class Person:

    def __init__(self, name, residence = 'unknown'):
        self.name = name
        self.residence = residence

    def tell(self):
        return f'I am {self.name} and I live in {self.residence}'

    def move(self, new_residence):
        self.residence = new_residence


# ----------------------------------------------

p1 = Person('Peter', 'Lhee')
p2 = Person('Dave', 'Angeren')

print( p1.tell() )
p1.move('Soesterberg')
print( p1.tell() )

print( p2.tell() )

