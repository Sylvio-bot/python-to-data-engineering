#create a super class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year

    def start(self):
        print('vehicule is starting')

    def stop(self):
        print("vehicul is stopping")

#create a subclasse 
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

car = Car('Ford','Focus',2005, 5,5)
print(car.__dict__)
