#
# Antonio Peza
# C950 Data Structures and Algorithms 2
# Algorithm to find the distances 
#
import datetime
import csv
import csvreader
from queue import Empty

# Empty Trucks
firstTruckSorted =[]
secondTruckSorted =[]
thirdTruckSorted =[]

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

# Method to return the address index given the string
# Parameter: an address from a package object as a string
# Return: the address ID given the address string
# Space time complexity O(n)
def addressLookupByStreet(addressString):
    with open(addressesFile) as addressFile:
        addressDataCSV = csv.reader(addressFile, delimiter=',')
        next(addressDataCSV) # skip header
        for address in addressDataCSV:
            addressID = int(address[0])
            addressName = address[1]
            addressStreet = address[2]
            if addressStreet == addressString:
                return addressName

# Method to return the address string given the ID
# Parameter: an address from a package object as an int
# Return: the address ID given the address ID
# Space time complexity O(n)
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

with open(distanceFile, mode='r', encoding='utf-8-sig') as distances:
    distanceData = list(csv.reader(distances, delimiter=','))

with open(addressesFile) as addresses:
    addressNames = list(csv.reader(addresses, delimiter=','))

# function reads the distance data and returns the numeric mileage
# Parameter: Two ints, row and column and numbers
# Return: distance as a float
def getDistanceBetween(row, col):
    distance = distanceData[row][col]
    # if blank, mirror the two parameters
    if distance == '':
        distance = distanceData[col][row]
    
    return float(distance)

# function reads the distance data and returns the numeric mileage between two given addresses
# Parameter: Two ints, row and column and numbers, sumDist
# Return: sumDist as a float
def getAndStoreDistance(row, col, sumDist):
    distance = distanceData[row][col]
    if distance == '':
        distance = distanceData[col][row]
    
    sumDist += float(distance)
    return sumDist

# Function to sort packages and load them on the truck as a sorted stacked data structure
# The first for loop will loop through each package on the truck, until the smallest distance is found
# it will then store the smallest distance in the smallestDistance variable
# it will then change the location to the address of the package
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
# Once sorted, it will add the time stamp that is passed in as a parameter, and begin delivering
#
# Space time complexity: O(n^2)
# Justification: Each package will be iterated by two for loops
def loadAndSortTrucks(currentLocation, truckWithPackages, departureTime):
    if truckWithPackages is Empty:
        print("empty truck")

    smallestDistance = 30.0
    location = 0

    for packageOnTruck in truckWithPackages:
        addressOfPackage = addressLookupByName(packageOnTruck.address)
        if getDistanceBetween(currentLocation, addressOfPackage) <= smallestDistance:
            smallestDistance = getDistanceBetween(currentLocation, addressOfPackage)
            location = addressOfPackage
    
    for packageOnTruck in truckWithPackages:
        addressOfPackage = addressLookupByName(packageOnTruck.address)
        if getDistanceBetween(currentLocation, addressOfPackage) == smallestDistance:
            if packageOnTruck in csvreader.getFirstTruck():
                #print("\nWas in first truck")
                packageOnTruck.status = "---En Route---"
                packageOnTruck.deliveryTime = departureTime
                firstTruckSorted.append(packageOnTruck)
                #print("\nPopped package: " + str(packageOnTruck.id))
                truckWithPackages.pop(truckWithPackages.index(packageOnTruck))
                currentLocation = location
                loadAndSortTrucks(currentLocation, truckWithPackages, departureTime)
            elif packageOnTruck in csvreader.getSecondTruck():
                #print("\nWas in second truck")
                packageOnTruck.status = "---En Route---"
                packageOnTruck.deliveryTime = departureTime
                secondTruckSorted.append(packageOnTruck)
                #print("\nPopped package: " + str(packageOnTruck.id))
                truckWithPackages.pop(truckWithPackages.index(packageOnTruck))
                currentLocation = location
                loadAndSortTrucks(currentLocation, truckWithPackages, departureTime)
            elif packageOnTruck in csvreader.getThirdTruck():
                #print("\nWas in third truck")
                packageOnTruck.status = "---En Route---"
                packageOnTruck.deliveryTime = departureTime
                thirdTruckSorted.append(packageOnTruck)
                #print("\nPopped package: " + str(packageOnTruck.id))
                truckWithPackages.pop(truckWithPackages.index(packageOnTruck))
                currentLocation = location
                loadAndSortTrucks(currentLocation, truckWithPackages, departureTime)

# Function to find the smallest distance given a starting location and a list of packages
# Parameters: int currentLocaiton, list truckWithPackages
# Return: float smallest distance. This smallest distance is the smallest distance between the current location
# and the address on the package
def minDistance(currentLocation, truckWithPackages):
    if truckWithPackages is Empty:
        print("empty truck")

    smallestDistance = 30.0

    for packageOnTruck in truckWithPackages:
        addressOfPackage = addressLookupByName(packageOnTruck.address)
        if getDistanceBetween(currentLocation, addressOfPackage) <= smallestDistance:
            smallestDistance = getDistanceBetween(currentLocation, addressOfPackage)
            
    return smallestDistance

# 
# Function to keep track of time 
#
def timeToDeliver(currentTime, distance):
    timeTraveledAsHours = distance / 18 # truck goes 18 mph
    timeTraveledAsMinutes = timeTraveledAsHours * 60
    timeObj = currentTime + datetime.timedelta(minutes=timeTraveledAsMinutes)
    return timeObj

#
# Function: calculates total distance traveled
# Parameters: list of truck with packages, distance
# Return: Prints out calculated total trip distance
#
def deliverPackages(truckWithPackages, tripDistance, departureTime):
    currentLocation = 0
    for item in truckWithPackages:
        tripDistance = getAndStoreDistance(currentLocation, addressLookupByName(item.address), tripDistance)
        #print("From: " + str(currentLocation) + " " + str(addressLookupByID(currentLocation)) + "\nTO: " + str(addressLookupByStreet(item.address)))
        currentLocation = addressLookupByName(item.address)
        #print("\nDistance so far: " + str(tripDistance))
        item.status = "***Delivered***"
        item.deliveryTime = timeToDeliver(departureTime, tripDistance)
    tripDistance = getAndStoreDistance(currentLocation, 0, tripDistance)
    #print("From: " + str(currentLocation) + " " + str(addressLookupByID(currentLocation)) + "\nTO: " + str(addressLookupByID(0)))
    #print("\n++++++++Roundtrip total: " + str(tripDistance) + "++++++++")
    return tripDistance

# Function to return the the sorted truck 
# Parameter: an int from 1-3
# return: Optimal truck 
def getSortedTruck(truckNum):
    if truckNum == 1:
        return firstTruckSorted
    elif truckNum == 2:
        return secondTruckSorted
    elif truckNum == 3:
        return thirdTruckSorted
    else:
        print("Please enter a valid number")