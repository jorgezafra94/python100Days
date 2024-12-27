class Prueba:
    pass


p = Prueba()
p.id = 3029
p.name = "pepe"
print(p.id, p.name)


class BasicCar:

    def __init__(self):
        self.name = "Nissan"
        self.seats = 4


bcar1 = BasicCar()
print(bcar1.name, bcar1.seats)


class Car:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats
        self.type = "Automatic"


c1 = Car("Chevy Spark", 4)
c2 = Car("Nissan Versa", 4)
print(c1.name, c2.name)
