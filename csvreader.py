#
# Antonio Peza
# C950 Data Structures and Algorithms 2
# This file will read the given csv files and store them
# in the appropriate data structure
#

import csv
from struct import pack
from Hashmap import *
from Package import *

hashtable = Hashmap()
packageData = "wgups/package.csv"
addressData = "wgups/addresses.csv"

# Initialize the trucks as lists
firstTruck = []
secondTruck = []
thirdTruck = []

# loadPackageData
# Parameter: requires a file to be read into the function
# return: Will create package objects based on the csv, then add them to the hashtable
# Space time complexity: O(n), it will iterate through each item once
with open(packageData) as packagefile:
    packagedata = csv.reader(packagefile, delimiter=',')
    next(packagedata) # skips header
    for package in packagedata:
        packageID = int(package[0])
        packageAddress = package[1]
        packageCity = package[2]
        packageState = package[3]
        packageZip = package[4]
        packageDeadline = package[5]
        packageMass = package[6]
        if package[7] == '':
            packageNotes = "No special notes"
        else:
            packageNotes = package[7]
        packageStatus = "--Pending Delivery--"

        packageContents = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadline, packageMass, packageNotes, packageStatus)

        if packageContents.id == 19:
            firstTruck.append(packageContents)

        if packageContents.deadline != 'EOD':
            if 'Must be' in packageContents.notes or packageContents.notes == "No special notes":
                firstTruck.append(packageContents)
        
        if packageContents.notes == 'Can only be on truck 2':
            secondTruck.append(packageContents)
        
        if packageContents not in firstTruck:
            if packageContents not in secondTruck:
                if packageContents not in thirdTruck:
                    if len(thirdTruck) > len(secondTruck):
                        secondTruck.append(packageContents)
                    else:
                        thirdTruck.append(packageContents)

        hashtable.add(packageID, packageContents)

# Method to return the address index given the string
# Parameter: an address from a package object as a string
# Return: the address ID given the address string
# Space time complexity O(n)
def addressLookup(addressString):
    with open(addressData) as addressFile:
        addressDataCSV = csv.reader(addressFile, delimiter=',')
        next(addressDataCSV) # skip header
        for address in addressDataCSV:
            addressID = int(address[0])
            addressName = address[1]
            addressStreet = address[2]
            if addressStreet == addressString:
                return addressID
        
#for i in range(1,41):
#   print(hashtable.get(i))

#hashtable.print()

#print(addressLookup(hashtable.get(27).address))
print("\nfirst truck: \n")
for i in range(0, len(firstTruck)):
    print(firstTruck[i])

print("\nsecond truck: \n")
for i in range(0, len(secondTruck)):
    print(secondTruck[i])

print("\nthird truck: \n")
for i in range(0, len(thirdTruck)):
    print(thirdTruck[i])

print("\n\n")
print("first truck: " + str(len(firstTruck)) + "\n")
print("second truck: " + str(len(secondTruck)) + "\n")
print("third truck: " + str(len(thirdTruck)) + "\n")

print("\n\n")
hashtable.print()