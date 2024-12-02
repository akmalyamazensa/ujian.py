class Car:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color
    
brand =input('enter the car brand : ')
type = input('enter the type : ')
color = input('enter the color : ')

print(f" A {color} {brand} type {type} was created.")
print('=' * 50)
