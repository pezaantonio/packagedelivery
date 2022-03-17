#
# Antonio Peza
# Student ID: 001174649
# WGU C950 Data Structures and Algorithms 2
# 
# Purpose: Main python file to run interface for program
#
import distance
import csvreader

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
distance.getDistanceTraveled(distance.getSortedTruck(1),0)