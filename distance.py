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
    distanceData = list(csv.reader(distances, delimiter=','))

with open(addressesFile) as addresses:
    addressNames = list(csv.reader(addresses, delimiter=','))

def getDistance(row, col):
    distance = distanceData[row][col]
    if distance == '':
        distance = distanceData[col][row]
    
    return float(distance)

print(getDistance(3,4))