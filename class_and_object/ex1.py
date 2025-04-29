from encodings.punycode import selective_find


class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = species

    def make_sound(self, sound):
        print(f'Your animal is {self.species},\n '
              f'name of your {self.species} is {self.name}\n'
              f'  and sound like: {sound}')


class Rectangel:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return f'Area is {self.width * self.height}'


dog = Animal('Dudi', 'Dog', 3)
cat = Animal('Suchka', 'Cat', 2)
rec = Rectangel(3, 5)

print(rec.calculate_area())
print(dog.make_sound('GAV-GAV'))
print(cat.make_sound('MIAU'))
