#
# Antonio Peza
# C950 Data Structures & Algorithms 2
# Hashmap implemented with Python
#

class Hashmap:

    # Constructor
    def __init__(self):
        # initilize hashmap length to 10
        self.size = 10
        # initialize variable map to an empty list with the same length as size
        self.map = [None] * self.size

    # private function to return the hash key
    # adds the unicode value of each letter in the word, then mods it by 5
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    # function to add items w/ values to the hashmap
    # if the key already exists, update the value
    def add(self, key, value):
        # key_hash is used to store the index that the private get_hash function returns
        key_hash = self._get_hash(key)
        # key_value is used to store the list of the key and the value from the add function
        key_value = [key, value]

        # if the map at index of key hash is empty, put the list from key_value in there
        # else, check to see if the key is the same, if it is just update, if its not, add a new value
        # the use of the append function is how the collisions are being handled
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                        pair[1] = value
                        return True
            self.map[key_hash].append(key_value)
            return True

    # function: given the key, find the pair
    # will first check to make sure that the map is not empty
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # first check to make sure that the selected key exists
    # then iterate through the lists in the index until you find the right list
    # uses the pop function to remove it from the list
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print('---HashMap---')
        for item in self.map:
            if item is not None:
                print(str(item))