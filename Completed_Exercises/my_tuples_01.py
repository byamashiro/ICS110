from collections import namedtuple

Automobile = namedtuple('Automobile',['number_of_doors', 'manual', 'colors'])

my_car = Automobile('4 doors', True, ['black', 'red', 'black'])

print(my_car.number_of_doors, ' ', my_car.manual, ' ', my_car.colors)