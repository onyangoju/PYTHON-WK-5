
# Smartphone class definition
class Smartphone:
    def __init__(self, brand, model, battery_life, storage_capacity, color):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
        self.storage_capacity = storage_capacity
        self.color = color

    def display_specs(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nBattery Life: {self.battery_life} hours\nStorage: {self.storage_capacity} GB\nColor: {self.color}"

    def make_call(self, number):
        return f"Making a call to {number}..."

    def charge(self):
        self.battery_life = 100
        return "Charging... Battery is now 100%."

# Inheritance example (optional polymorphism or encapsulation)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, storage_capacity, color, refresh_rate):
        super().__init__(brand, model, battery_life, storage_capacity, color)
        self.refresh_rate = refresh_rate

    def display_specs(self):
        base_specs = super().display_specs()
        return f"{base_specs}\nRefresh Rate: {self.refresh_rate}Hz"

# --- Running the code ---
print("📱 Smartphone Demo")
phone = Smartphone("Samsung", "Galaxy S21", 20, 256, "Black")
print(phone.display_specs())
print(phone.make_call("0712-345-678"))
print(phone.charge())

print("\n🎮 Gaming Phone Demo")
gaming = GamingPhone("Asus", "ROG Phone 6", 25, 512, "Red", 144)
print(gaming.display_specs())
