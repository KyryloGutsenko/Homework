from traceback import print_tb


class Vachile:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def display(self):
        print(f'Maker is {self.make}. You have model {self.model} and year of manufacture is {self.year}---<')

class Bicycle(Vachile):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color


    def display(self):
        print(f'Maker is {self.make}. You have model {self.model}. Color is {self.color} '
              f'\n and year of manufacture is {self.year}---<')


    def STO(self):
        if int(self.year) < 2015:
            print(f'Yor vachile need check out')
        else:
            print(f'You can enjoy your {self.model}')


class Car(Vachile):
    def __init__(self,make, model, year, eng_type):
        super().__init__(make, model, year)
        self.eng_type = eng_type


    def display(self):
        print(f'Maker is {self.make}. You have model {self.model}. Engine type is {self.eng_type}'
              f'\n and year of manufacture is {self.year}---<')


    def start_eng(self):
        print(f'Your {self.model} is starting moving')


class Motorcycle(Vachile):
    def __init__(self, make, model, year, count_wheel):
            super().__init__(make,model,year)
            self.count_wheel = count_wheel


    def display(self):
        print(f'Maker is {self.make}. You have model {self.model}.Quantity wheels are {self.count_wheel}'
              f'\n  and year of manufacture is {self.year}---<')


    def check_eng(self):
        print(f'Are you suicide? Take a ticket and go to your bus!')


bicycle = Bicycle('Trek', 'MTB', '2022', 'Blue')
bicycle.STO()
bicycle.display()
car = Car('Mercedes', 'Gelintwagen', '2015', 'WG3')
car.start_eng()
car.display()
motorcycle = Motorcycle('BMW', 'A15', '2003', '2')
motorcycle.check_eng()
motorcycle.display()