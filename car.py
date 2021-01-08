# Class

class Car():
    """ This is a car class that will display the make, model and color """

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.gas = 100

    def __str__(self):
        return "{}, {}, {}".format(self.make, self.model, self.color)

    def drive(self):
        self.gas -= 10
        # print(f"Vrooom {self.gas}")
    
    def fill_tank(self):
        self.gas = 100
        # print(f"{self.make} {self.model} now full")

    def check_gas(self):
        print(f"You have {self.gas} fuel remaining")




car1 = Car("Dodge", "Charger", "Charcoal Grey")

car1.drive()
car1.drive()
car1.drive()
car1.fill_tank()
car1.drive()
car1.drive()
car1.drive()
car1.fill_tank()
car1.drive()
car1.drive()
car1.drive()
car1.drive()
car1.check_gas()

class Pet():
    def __init__(self, animal,name, color, energy_level):
        self.animal = animal
        self.name = name
        self.color = color
        self.energy_level = energy_level
        self.belly = 100

    def play(self):
        if self.energy_level > 30:
            print("Playing")
            self.energy_level -= 30
        else:
            print(f"{self.name} I am too tired to play")
    
    def rest(self):
        if self.energy_level >= 100:
            print(f"{self.name} has too much energy to sleep.")
        else:
            self.energy_level = 100
            print(f"{self.name} is ready to play!")

    def eat(self):
        if self.belly >= 100:
            print(f"{self.name} is too full to eat")
        else:
            self.belly = 100
            print(f"{self.name} has eaten")

my_pet = Pet("dog", "Lancelot", "Black/Brown", 200)

my_pet.play()
my_pet.play()
my_pet.play()
my_pet.play()
my_pet.play()
my_pet.play()
my_pet.play()
my_pet.play()
my_pet.play()
my_pet.play()
my_pet.play()
my_pet.play()
    
    