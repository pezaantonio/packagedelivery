#
# Antonio Peza
# C950 Data Structures and Algorithms 2
# This file will read the given csv files and store them
# in the appropriate data structure
#

import csv
from Hashmap import *
from Package import *
from distance import *

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
        packageStatus = "On delivery truck"

        packageContents = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadline, packageMass, packageNotes, packageStatus)

        # package 19 will always be on truck 1 due to its special notes
        if packageContents.id == 19:
            firstTruck.append(packageContents)

        # if the package deadline is 10:30 AM or before, and it has no special notes, make sure its on the first truck
        if packageContents.deadline != 'EOD':
            if 'Must be' in packageContents.notes or packageContents.notes == "No special notes":
                firstTruck.append(packageContents)
        
        # If the package can only be on truck 2, put it on truck 2
        if packageContents.notes == 'Can only be on truck 2':
            secondTruck.append(packageContents)
        
        # if the package is not on any trucks yet, put it on the second or third truck
        # depending on which is less full
        if packageContents not in firstTruck:
            if packageContents not in secondTruck:
                if packageContents not in thirdTruck:
                    if len(thirdTruck) > len(secondTruck):
                        secondTruck.append(packageContents)
                    else:
                        thirdTruck.append(packageContents)

        # regardless of which truck its on, put every package in the hashtable
        hashtable.add(packageID, packageContents)
        
#for i in range(1,41):
#   print(hashtable.get(i))

#hashtable.print()

# print(addressLookup(hashtable.get(27).address))
print("\nfirst truck: \n")
print(len(firstTruck))
for i in range(0, len(firstTruck)):
    print(firstTruck[i])

# print("\nsecond truck: \n")
# for i in range(0, len(secondTruck)):
#     print(secondTruck[i])

# print("\nthird truck: \n")
# for i in range(0, len(thirdTruck)):
#     print(thirdTruck[i])

# print("\n\n")
#print("first truck: " + str(len(firstTruck)) + "\n")
#print("second truck: " + str(len(secondTruck)) + "\n")
#print("third truck: " + str(len(thirdTruck)) + "\n")

deliverToClosestAddress(firstTruck, 0)

print("\nfirst truck: \n")
print(len(firstTruck))
#for i in range(0, len(firstTruck)):
#    print(firstTruck[i])