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

# calculate distance traveled for all trucks
distance.getDistanceTraveled(distance.getSortedTruck(1),0)

for item in distance.getSortedTruck(1):
    print(str(item))