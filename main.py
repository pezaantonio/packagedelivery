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

for item in csvreader.getFirstTruck():
    print(str(item))

for item in csvreader.getSecondTruck():
    print(str(item))

for item in csvreader.getThirdTruck():
    print(str(item))

# At this time, each truck will be sorted for optimal delivery
# The package is loaded onto the truck, then the status changes from "At the hub" to "En route"
distance.loadAndSortTrucks(0, csvreader.getFirstTruck(), firstTruckDepart)
distance.loadAndSortTrucks(0, csvreader.getSecondTruck(), secondTruckDepart)
distance.loadAndSortTrucks(0, csvreader.getThirdTruck(), thirdTruckDepart)

print("\n\n\n\n\n")
for item in distance.getSortedTruck(1):
    print(str(item))

for item in distance.getSortedTruck(2):
    print(str(item))

for item in distance.getSortedTruck(3):
    print(str(item))


# Calculating distance traveled, as well as the timestamping upon delivery
distance.deliverPackages(distance.getSortedTruck(1),0, firstTruckDepart)
distance.deliverPackages(distance.getSortedTruck(2),0, secondTruckDepart)
distance.deliverPackages(distance.getSortedTruck(3),0, thirdTruckDepart)

print("Total distance traveled: " + 
str(distance.deliverPackages(distance.getSortedTruck(1),0, firstTruckDepart) + 
distance.deliverPackages(distance.getSortedTruck(2),0, secondTruckDepart) + 
distance.deliverPackages(distance.getSortedTruck(3),0, thirdTruckDepart)))

for i in range(0,41):
    print(csvreader.getHashmap().get(i))