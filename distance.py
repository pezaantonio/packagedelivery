#
# Antonio Peza
# C950 Data Structures and Algorithms 2
# Algorithm to find the distances 
#
import csv

# Open CSV file
distanceFile = "wgups/distancedata.csv"
addressesFile = "wgups/addresses.csv"

with open(distanceFile) as distances:
    distanceData = list(csv.reader(distanceFile, delimter=','))

with open(addressesFile) as addresses:
    addressNames = list(csv.reader(addressesFile, delimiter=','))