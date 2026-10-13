class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed 
        self.owner = owner

    def bark(self):
        print("whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

owner1 = Owner("Danny", "Soatsidina", "038 20 358 25")
dog1 = Dog("Bruce", "scottish terrier",owner1)
dog1.bark()
print(dog1.owner.name)
print(dog1.name)
print(dog1.breed)
