#
# Antonio Peza
# Student ID: 001174649
# WGU C950 Data Structures and Algorithms 2
# 
# Purpose: Main python file to run interface for program
#
import distance
import csvreader

firstTrip = []
secondTrip = []
thirdTrip =[]

distance.deliverToClosestAddress(csvreader.getFirstTruck(), 0)
distance.deliverToClosestAddress(csvreader.getSecondTruck(), 0)
distance.deliverToClosestAddress(csvreader.getThirdTruck(), 0)

print("\n")
distance.getSortedTruck(1)
print("\n")
distance.getSortedTruck(2)
print("\n")
distance.getSortedTruck(3)