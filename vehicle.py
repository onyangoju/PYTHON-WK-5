# Base class
class Vehicle:
    def move(self):
        pass

# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# --- Running the code ---
print("🚗✈️⛵ Polymorphism in Action")

vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
