#import "datetime" module
import datetime

#THis classs helps with making and handling the bill records
class Bill:
    #This is initialised so we cna help to keep track of how many bills are created
    count = 0

    #Constructor to make a new bill
    def __init__(self):
        Bill.count += 1
        self.id = f"B{Bill.count}"
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.roomCharge = 0.0
        self.roomItems = []

    #A method to add a room to the bill
    def addRoom(self, room, quantity, nights):
        subtotal = room.price * quantity *nights
        self.roomItems.append([room.roomType, room.price, quantity, nights, subtotal])
        self.roomCharge += subtotal

    #Method to calculate service charge
    def serviceCharge(self):
        return self.roomCharge * 0.10
    
    #Method to calculate tax charge
    def taxCharge(self):
        return self.roomCharge * 0.06
    
    #Method to calculate total room charge
    def totalCharge(self):
        return self.roomCharge + self.serviceCharge() + self.taxCharge()
    
    #This method prints the invoice
    def printInvoice(self):
        print("---------------------------------------------------------")
        print("\t\t\tInvoice")
        print("---------------------------------------------------------\n")
        print(f"Date: {self.date}")
        print(f"Bill No: {self.id}\n")
        print(f"{'Type':<15} {'Price':<10} {'Quantity':<10} {'Nights':<10} {'Subtotal':<10}")
        print("---------------------------------------------------------")
        for item in self.roomItems:
            print(f"{item[0]:<15} {item[1]:<10.2f} {item[2]:>8} {item[3]:>8} {item[4]:>11.2f}")
        print("---------------------------------------------------------")
        print(f"Room charges {self.roomCharge:43.2f}")
        print(f"Service charge (10%) {self.serviceCharge():35.2f}")
        print(f"Tax (6%) {self.taxCharge():47.2f}")
        print("---------------------------------------------------------")
        print(f"Total {self.totalCharge():50.2f}")
        print("=========================================================")