class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.openSeats():
            return False
        self.passengers.append(name)  # Corrigido de passenger para passengers
        return True

    def openSeats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight Successfully")  # Corrigido "Succesfully" para "Successfully"
    else:
        print(f"No available Seat for {person}")  # Corrigido "avaiable" para "available"