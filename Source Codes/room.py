class Room:
    #Constructor to initialise a room instance and its attributes
    def __init__(self, roomType, capacity, price):
        self.roomType = roomType
        self.capacity = capacity
        self.price = price
    
    #Method to return string of the Room object
    def __str__(self):
        return f"{self.roomType} ({self.capacity} pax) - RM {self.price:.2f}"