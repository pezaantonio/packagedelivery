#
# Antonio Peza
# C950 Data Structures and Algorithms 2
# Class for packages
#

# Package class to store all package from the csv as objects
class Package():

    def __init__(self, id, address, city, state, zip, deadline, kilo, notes, status, deliveryTime):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.kilo = kilo
        self.notes = notes
        self.status = status
        self.deliveryTime = deliveryTime

    # __str__ overwriting print function so when we print, it will not print the reference but the actual information
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s" %(self.id, self.address, self.city, self.state, self.zip, self.deadline, self.kilo, self.notes, self.status, self.deliveryTime)