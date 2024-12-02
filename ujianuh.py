class Car:
    def __init__(self, brand, type, power, color):
        self.brand = brand
        self.type = type
        self.power = power
        self.color = color
    
brand =input('enter the car brand : ')
type = input('enter the type : ')
power = input('enter the power:')
color = input('enter the color : ')
print('=' * 50)

print(f" A {color} {brand} type {type} has {power} was created.")
print('=' * 50)
