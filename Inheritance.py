class Car():
    def __init__(self, gears, seats, maxSpeed):
        self.gears = gears
        self.seats = seats
        self.maxSpeed = maxSpeed

    def speedUp(self):
        print("Speed Increasing")

    def apply_brakes(self):
        print("Speed Decreasing")

class Harrier(Car):
    def race_mode(self):
        print("Race Mode on")

class Verna(Car):
    pass

h1 = Harrier(5, 5, 240)
print(h1.gears)
print(h1.seats)
print(h1.maxSpeed)
h1.race_mode()
c1 = Car(5, 7, 300)
print(c1.seats)
print(c1.gears)
print(c1.maxSpeed)
v1 = Verna(5, 5, 240)
print(v1.gears)
print(v1.seats)
print(v1.maxSpeed)
