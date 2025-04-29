# Ex. 3
fragen = input('Enter country to know capital: ')
my_fav_spman = {
    'Name': 'Kirill',
    'Age': '21',
    'Sport': 'LABA',
    'Team': 'LABAEVERYDAY'
}
my_fav_book = {
        'Name': 'Lord of the Ring',
        'Year of public': '1999'
}
my_fav_book.update({'Name': 'Harry Potter'})
my_fav_book.update({ 'Year of public': '2000'})
countries = {
    'Ukraina': 'Kiev',
    'German': 'Berlin',
    'Spanish': 'Madrid',
    'Rusen': 'Moskow'
}

if countries.get(fragen, False):
    print(f'Capital of {fragen} is {countries.get(fragen)}')
else:
    print('Our program does not know the capital\n or you entered the country with pomilka')

print(my_fav_spman)
print(my_fav_book)