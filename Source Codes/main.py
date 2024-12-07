
#Importing the functions from functions.py
from functions import functionMenu, addRoom, bookRoom, showRecords

print("\n******Hotel******")

#The infinite loop that will constantly ask user, but will break if user picks "4"
while True:

    #Iterating the menu dictionary to display it tot he user
    menu = functionMenu()
    print("\nFunction Menu: ")
    for key, value in menu.items():
        print(f"{key}. {value}")

    #This part takes user input for the selection
    selection = input("Enter selection (1-4): ")
    if selection == "1":
        addRoom()
    elif selection == "2":
        bookRoom()
    elif selection == "3":
        showRecords()
    elif selection == "4":
         print("Thank you for using the system.")
         break
    else:
        #The error handler if user doesnt pick any of the provided options
        print("Invalid selection. Please try again.")
