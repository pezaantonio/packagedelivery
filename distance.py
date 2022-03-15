#
# Antonio Peza
# C950 Data Structures and Algorithms 2
# Algorithm to find the distances 
#
import csv

# Open CSV file
distanceFile = "wgups/distancedata.csv"
addressesFile = "wgups/addresses.csv"

# Method to return the address index given the string
# Parameter: an address from a package object as a string
# Return: the address ID given the address string
# Space time complexity O(n)
def addressLookup(addressString):
    with open(addressesFile) as addressFile:
        addressDataCSV = csv.reader(addressFile, delimiter=',')
        next(addressDataCSV) # skip header
        for address in addressDataCSV:
            addressID = int(address[0])
            addressName = address[1]
            addressStreet = address[2]
            if addressStreet == addressString:
                return addressID

with open(distanceFile) as distances:
    distanceData = list(csv.reader(distances, delimiter=','))

with open(addressesFile) as addresses:
    addressNames = list(csv.reader(addresses, delimiter=','))

# function reads the distance data and returns the numeric mileage
# Parameter: Two ints, row and column and numbers
# Return: distance as a float
def getDistance(row, col):
    distance = distanceData[row][col]
    # if blank, mirror the two parameters
    if distance == '':
        distance = distanceData[col][row]
    
    return float(distance)

#print(getDistance(3,4))
for address in addressNames:
    print(address)