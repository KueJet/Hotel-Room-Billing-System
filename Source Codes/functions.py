import os
from room import Room
from bill import Bill

roomFile = "room.txt"
billFile = "bill.txt"

def functionMenu():
    return{
        "1": "Add room",
        "2": "Book room",
        "3": "Show records",
        "4": "Quit"
    }

def roomOptionMenu():
    rooms = {}
    with open(roomFile, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            roomData = line.strip().split(',')
            room = Room(roomData[0], int(roomData[1]), float(roomData[2]))
            rooms[str(i)] = room
    return rooms

def addRoom():
    while True:
        roomType = input("Enter room type: ").strip()
        if roomType:
            break
        else:
            print ("Room type cannot be empty. Please enter a value.")

    while True:
        try:
            capacity = int(input("Enter pax: "))
            break
        except ValueError:
            print("Invalid Input. Please try again")
        
    while True:
        try:
            price = float(input("Enter price: "))
            break
        except ValueError:
            print("Invalid Input. Please try again")
        
    with open(roomFile, 'a') as file:
        file.write(f"{roomType},{capacity},{price}\n")
    print(f"Room {roomType} added.")

def bookRoom():
    bill = Bill()
    if not os.path.exists(roomFile):
        print("No available room found.")
        return

    while True:
        rooms = roomOptionMenu()
        print("\nRoom available:")
        for key, room in rooms.items():
            print(f"{key}. {room}")

        selection = input("Enter selection: ")
        if selection not in rooms:
            print("Invalid selection. Try again.")
            continue

        room = rooms[selection]
        while True:
            try:
                quantity = int(input("Number of rooms: "))
                break
            except ValueError:
                print("Invalid Input. Please try again")

        while True:
            try:
                nights = int(input("Number of nights: "))
                break
            except ValueError:
                print("Invalid Input. Please try again")

        bill.addRoom(room, quantity, nights)

        while True:
            moreRooms = input("Book another room? y/n: ").lower()
            if moreRooms == 'y':
                break
            if moreRooms == 'n':
                break
            else:
                print("Invalid selection, Please try again!")

        if moreRooms == 'n':
            break

    bill.printInvoice()
    with open(billFile, 'a') as file:
        file.write(f"{bill.id},{bill.date},{bill.totalCharge():.2f}\n")

def showRecords():
    if not os.path.exists(billFile):
        print("No records found.")
        return
    
    with open(billFile, 'r') as file:
        lines = file.readlines()
        if not lines:
            print("No records found.")
            return
    
    print(f"Number of records: {len(lines)}")
    print("------------------------------------------")
    print(f"{'Bill No.':<10} {'Bill Date':20} {'Total':>10}")
    print("------------------------------------------")
    for line in lines:
        billData = line.strip().split(',')
        print(f"{billData[0]:<10} {billData[1]:20} {billData[2]:>10}")
    print("==========================================")


