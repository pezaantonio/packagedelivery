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

#print(distance.minDistance(0, csvreader.getFirstTruck()))

# Load the trucks
distance.deliverToClosestAddress(0, csvreader.getFirstTruck())
distance.deliverToClosestAddress(0, csvreader.getSecondTruck())
distance.deliverToClosestAddress(0, csvreader.getThirdTruck())

