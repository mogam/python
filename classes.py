# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(5, 8)
# print(p.y)
# print(p.x)

# from sre_constants import SUCCESS


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(10)

people = ["Pushpak", "Anjali"]
for person in people:
        success = flight.add_passenger(person)
        if success:
            print(f"Added {person} to flight successfully")
        else:
            print(f"No available seats for {person}")




