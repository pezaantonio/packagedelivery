#
# Antonio Peza
# Student ID: 001174649
# WGU C950 Data Structures and Algorithms 2
# 
# Purpose: Main python file to run interface for program
#
import distance
import csvreader
import datetime

# Truck leaving the hub at assigned time
firstTruckDepart = datetime.timedelta(hours=int(8))
secondTruckDepart = datetime.timedelta(hours=int(9), minutes=int(10))
thirdTruckDepart = datetime.timedelta(hours=int(11))

# At this time, each truck will be sorted for optimal delivery
# The package is loaded onto the truck, then the status changes from "At the hub" to "En route"
distance.loadAndSortTrucks(0, csvreader.getFirstTruck(), firstTruckDepart)
distance.loadAndSortTrucks(0, csvreader.getSecondTruck(), secondTruckDepart)
distance.loadAndSortTrucks(0, csvreader.getThirdTruck(), thirdTruckDepart)

# Calculating distance traveled, as well as the timestamping upon delivery
distance.deliverPackages(distance.getSortedTruck(1),0, firstTruckDepart)
distance.deliverPackages(distance.getSortedTruck(2),0, secondTruckDepart)
distance.deliverPackages(distance.getSortedTruck(3),0, thirdTruckDepart)

firstTruckDone = distance.getSortedTruck(1)
secondTruckDone = distance.getSortedTruck(2)
thirdTruckDone = distance.getSortedTruck(3)

# for i in range(0,41):
#     print(csvreader.getHashmap().get(i))

hashm = csvreader.getHashmap()

print("-----------------")
print("Welcome to WGUPS!")
print("-----------------")
print("Total distance traveled: " + 
    str(distance.deliverPackages(distance.getSortedTruck(1),0, firstTruckDepart) + 
    distance.deliverPackages(distance.getSortedTruck(2),0, secondTruckDepart) + 
    distance.deliverPackages(distance.getSortedTruck(3),0, thirdTruckDepart)))

userInput = input("""\nPlease select an option
    1. Track a package by its ID number
    2. Track all packages

    Type 'quit' or 'q' to exit the program\n
    """)
# User input 1 is to check individual packages
if userInput == '1':
    print("Choice 1")
#User input 2 is to check all packages at a given time
elif userInput == '2':
    timeInput = input("Enter a time to check the status of all packages (HH:MM:SS): ")
    (hrs, min, sec) = timeInput.split(':')
    dateTimeInput = datetime.timedelta(hours=int(hrs), minutes=int(min), seconds=int(sec))

    for item in range(1,41):
        timeOnPackage = hashm.get(item).deliveryTime
        if timeOnPackage >= dateTimeInput:
            if hashm.get(item) in firstTruckDone:
                if dateTimeInput >= firstTruckDepart:
                    hashm.get(item).status = "En Route"
                    print(str(hashm.get(item).id) + "\t" + str(hashm.get(item).status))
                else:
                    hashm.get(item).status = "At the hub"
                    print(str(hashm.get(item).id) + "\t" + str(hashm.get(item).status))
            elif hashm.get(item) in secondTruckDone:
                if dateTimeInput >= secondTruckDepart:
                    hashm.get(item).status = "En Route"
                    print(str(hashm.get(item).id) + "\t" + str(hashm.get(item).status))
                else:
                    hashm.get(item).status = "At the hub"
                    print(str(hashm.get(item).id) + "\t" + str(hashm.get(item).status))
            elif hashm.get(item) in thirdTruckDone:
                if dateTimeInput >= thirdTruckDepart:
                    hashm.get(item).status = "En route"
                    print(str(hashm.get(item).id) + "\t" + str(hashm.get(item).status))
                else:
                    hashm.get(item).status = "At the hub"
                    print(str(hashm.get(item).id) + "\t" + str(hashm.get(item).status))
        else:
            hashm.get(item).status = "Delivered"
            print(str(hashm.get(item).id) + "\t" + str(hashm.get(item).status))

elif userInput == "quit" or userInput == 'q':
    exit()