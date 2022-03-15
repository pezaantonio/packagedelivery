#
# Antonio Peza
# C950 Data Structures and Algorithms 2
# Algorithm to find the distances 
#
import csv
from queue import Empty

# Truck leaving the hub at assigned time
firstTruckDepart = ['8:00:00']
secondTruckDepart = ['9:10:00']
thirdTruckDepart = ['11:00:00']

# Open CSV file
distanceFile = "wgups/distancedata.csv"
addressesFile = "wgups/addresses.csv"

# Method to return the address index given the string
# Parameter: an address from a package object as a string
# Return: the address ID given the address string
# Space time complexity O(n)
def addressLookupByName(addressString):
    with open(addressesFile) as addressFile:
        addressDataCSV = csv.reader(addressFile, delimiter=',')
        next(addressDataCSV) # skip header
        for address in addressDataCSV:
            addressID = int(address[0])
            addressName = address[1]
            addressStreet = address[2]
            if addressStreet == addressString:
                return addressID

def addressLookupByID(ID):
    with open(addressesFile) as addressFile:
        addressDataCSV = csv.reader(addressFile, delimiter=',')
        next(addressDataCSV) # skip header
        for address in addressDataCSV:
            addressID = int(address[0])
            addressName = address[1]
            addressStreet = address[2]
            if addressID == ID:
                return addressName

with open(distanceFile) as distances:
    distanceData = list(csv.reader(distances, delimiter=','))

with open(addressesFile) as addresses:
    addressNames = list(csv.reader(addresses, delimiter=','))

# function reads the distance data and returns the numeric mileage
# Parameter: Two ints, row and column and numbers
# Return: distance as a float
def getCurrentDistance(row, col):
    distance = distanceData[row][col]
    # if blank, mirror the two parameters
    if distance == '':
        distance = distanceData[col][row]
    
    return float(distance)

# function reads the distance data and returns the numeric mileage between two given addresses
# Parameter: Two ints, row and column and numbers, sumDist
# Return: sumDist as a float
def getDistanceBetween(row, col, sumDist):
    distance = distanceData[row][col]
    if distance == '':
        distance = distanceData[col][row]
    
    sumDist += float(distance)
    return sumDist

def deliverToClosestAddress(truckWithPackages, currentLocation):
    if truckWithPackages is Empty:
        print("empty truck")
    
    smallestDistance = 50.0
    location = 0

    print("\nCurrent location: " + str(addressLookupByID(location)))

    for packageOnTruck in truckWithPackages:
        pOT = addressLookupByName(packageOnTruck.address)
        if getCurrentDistance(currentLocation, pOT) <= smallestDistance:
            smallestDistance = getCurrentDistance(currentLocation, pOT)
            location = pOT
            print("\n" + str(smallestDistance))
            print("\nCurrent location: " + str(addressLookupByID(location)))
            packageOnTruck.status = "Delivered"
            truckWithPackages.pop(truckWithPackages.index(packageOnTruck))
            deliverToClosestAddress(truckWithPackages, currentLocation)
    
    for packageOnTruck in truckWithPackages:
        if getCurrentDistance(currentLocation, pOT) == smallestDistance:
            packageOnTruck.status = "Delivered"
            truckWithPackages.pop(truckWithPackages.index[packageOnTruck])
            currentLocation = location
            deliverToClosestAddress(truckWithPackages, currentLocation)