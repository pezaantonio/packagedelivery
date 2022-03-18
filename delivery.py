#
# Antonio Peza
# Student ID: 001174649
# WGU C950 Data Structures and Algorithms 2
# 
# Purpose: Main python file to run interface for program
#
import distance
import csvreader
import Hashmap

# Truck leaving the hub at assigned time
firstTruckDepart = ['8:00:00']
secondTruckDepart = ['9:10:00']
thirdTruckDepart = ['11:00:00']

# sort the trucks
distance.deliverToClosestAddress(0, csvreader.getFirstTruck())
distance.deliverToClosestAddress(0, csvreader.getSecondTruck())
distance.deliverToClosestAddress(0, csvreader.getThirdTruck())

# currentLocation = 0
# for item in distance.getSortedTruck(1):
#     firstTripDistance = distance.getAndStoreDistance(currentLocation, distance.addressLookupByName(item.address), firstTripDistance)
#     print("From: " + str(currentLocation) + " " + str(distance.addressLookupByID(currentLocation)) + "\nTO: " + str(distance.addressLookupByStreet(item.address)))
#     currentLocation = distance.addressLookupByName(item.address)
#     print("\nDistance so far: " + str(firstTripDistance))

# calculate distance traveled for all trucks
#distance.getDistanceTraveled(distance.getSortedTruck(1),0)

currentLocation = 0
for item in distance.getSortedTruck(1):
    print("This package is being delivered: " + str(csvreader.getHashmap().get(item.id)))
    print("\nFrom: " + str(distance.addressLookupByID(currentLocation)))
    print("\nTo: " + str(distance.addressLookupByStreet(item.address) + "\n"))
    currentLocation = distance.addressLookupByName(item.address)
    if currentLocation == distance.addressLookupByName(item.address):
        item.status = "---DELIVERED---"
        distance.getSortedTruck(1).pop(distance.getSortedTruck(1).index(item))

print(len(distance.getSortedTruck(1)))

# for i in range(0, 40):
#     print(csvreader.getHashmap().get(i))