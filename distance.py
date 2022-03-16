#
# Antonio Peza
# C950 Data Structures and Algorithms 2
# Algorithm to find the distances 
#
from cgitb import small
import csv
import csvreader
from queue import Empty

# Empty Trucks
firstTruckSorted =[]
secondTruckSorted =[]
thirdTruckSorted =[]

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

# Function to sort packages and load them on the truck as a sorted stacked data structure
# The first lines of code will check to see if the list is empty, if empty it will return an empty truck string
# It will then assign the smallest distance with the float of 30, since 30 is higher than all distances in the csv
# the location will be equal the given currentLocation
# 
# Next, the for loop will iterate through each package
# it will take the package address and then calculate the distance between the current location and the address
# if the distance between the current location and the package address is less than or equal to the smallest distance, it will 
# change the the smallest distance to current distance and move to that location
#
# Finally, it will again iterate through each package on the truck
# if the distance matches the new smallestDistance, it will check 
# each package to determine which truck it is supposed to be on.
# Once determined which truck it will go on, it will sort that package into that truck
# Once everything is completed, each truck will be sorted in the optimal order it will deliver them
#
# Space time complexity: O(n^2)
# Justification: Each package will be iterated by two for loops
def deliverToClosestAddress(truckWithPackages, currentLocation):
    if truckWithPackages is Empty:
        print("empty truck")
    
    smallestDistance = 30.0
    location = currentLocation

    print("\nCurrent location: " + str(addressLookupByID(location)))

    for packageOnTruck in truckWithPackages:
        addressOfPackage = addressLookupByName(packageOnTruck.address)
        print("\ndistance checked: " + str(smallestDistance))
        if getCurrentDistance(currentLocation, addressOfPackage) <= smallestDistance:
            smallestDistance = getCurrentDistance(currentLocation, addressOfPackage)
            location = addressOfPackage
            print("\nFound new smallest distance: " + str(addressLookupByID(location) + "\t" + str(packageOnTruck.address)))
            print("\nHere is the distance: " + str(smallestDistance))
    
    for packageOnTruck in truckWithPackages:
        addressOfPackage = addressLookupByName(packageOnTruck.address)
        if getCurrentDistance(currentLocation, addressOfPackage) == smallestDistance:
            if packageOnTruck in csvreader.getFirstTruck():
                #print("\nWas in first truck")
                firstTruckSorted.append(packageOnTruck)
                #print("\nPopped package: " + str(packageOnTruck.id))
                truckWithPackages.pop(truckWithPackages.index(packageOnTruck))
                currentLocation = location
                deliverToClosestAddress(truckWithPackages, currentLocation)
            elif packageOnTruck in csvreader.getSecondTruck():
                #print("\nWas in second truck")
                secondTruckSorted.append(packageOnTruck)
                #print("\nPopped package: " + str(packageOnTruck.id))
                truckWithPackages.pop(truckWithPackages.index(packageOnTruck))
                currentLocation = location
                deliverToClosestAddress(truckWithPackages, currentLocation)
            elif packageOnTruck in csvreader.getThirdTruck():
                #print("\nWas in third truck")
                thirdTruckSorted.append(packageOnTruck)
                #print("\nPopped package: " + str(packageOnTruck.id))
                truckWithPackages.pop(truckWithPackages.index(packageOnTruck))
                currentLocation = location
                deliverToClosestAddress(truckWithPackages, currentLocation)

            

    # for packageOnTruck in truckWithPackages:
    #     addressOfPackage = addressLookupByName(packageOnTruck.address)
    #     print("\n" + str(addressLookupByID(packageOnTruck.id)) + "\t" + str(packageOnTruck.id) + "\n")
    #     if getCurrentDistance(currentLocation, addressOfPackage) <= smallestDistance:
    #         smallestDistance = getCurrentDistance(currentLocation, addressOfPackage)
    #         location = addressOfPackage
    #         print("\n" + str(smallestDistance))
    #         print("\nNew location: " + str(addressLookupByID(location)))
    
    # for packageOnTruck in truckWithPackages:
    #     addressOfPackage = addressLookupByName(packageOnTruck.address)
    #     if getCurrentDistance(currentLocation, addressOfPackage) == smallestDistance:
    #         if packageOnTruck in csvreader.getFirstTruck():
    #             firstTruckSorted.append(packageOnTruck)
    #             currentLocation = location
    #             deliverToClosestAddress(truckWithPackages)
    #         elif packageOnTruck in csvreader.getSecondTruck():
    #             secondTruckSorted.append(packageOnTruck)
    #             currentLocation = location
    #         elif packageOnTruck in csvreader.getThirdTruck():
    #             thirdTruckSorted.append(packageOnTruck)
    #             currentLocation = location