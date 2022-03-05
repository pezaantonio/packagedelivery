#
# Antonio Peza
# C950 Data Structures and Algorithms 2
# This file will read the given csv files and store them
# in the appropriate data structure
#

import csv
from email.headerregistry import Address
from Hashmap import *
from Package import *

hashtable = Hashmap()
packageData = "wgups/package.csv"
addressData = "wgups/addresses.csv"

# loadPackageData
# Parameter: requires a file to be read into the function
# return: Will create package objects based on the csv, then add them to the hashtable
def loadPackageData(filename):
    with open(filename) as packagefile:
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

            myPackage = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadline, packageMass, packageNotes)
            hashtable.add(packageID, myPackage)
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
        
loadPackageData(packageData)
#for i in range(1,41):
#    print(hashtable.get(i))

#print(hashtable.get(27))

print(addressLookup(hashtable.get(27).address))