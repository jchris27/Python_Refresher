class Vehicle:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')

    def get_maker(self):
        print(f"I'm a {self.make}")

    def get_model(self):
        print(f"Model is: {self.model}")

my_car = Vehicle("Mazda", "Model 3")
# print(my_car.make)
# print(my_car.model)

my_car.moves()
my_car.get_maker()
my_car.get_model()

your_car = Vehicle("Cadillac", "Escalade")
your_car.get_model()
your_car.get_maker()

# INHERITANCE

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id) -> None:
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along..")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along..")

class Golf_Cart(Vehicle):
    pass

cessna = Airplane("Cessna", "SkyHawk", "N-12345")
mack = Truck("Mack", "Pinnacle")
golfwagon = Golf_Cart("Yamaha", "GC100")

cessna.get_maker()
print(cessna.faa_id)
cessna.moves()

mack.get_maker()
mack.moves()

golfwagon.get_maker()
golfwagon.moves()

print('\n\n')

# POLYMORPHISM

for x in (my_car, your_car, cessna, mack, golfwagon):
    x.get_maker()
    x.moves()