import hashlib
from random import randint

"""Chaned Hash Table includes a hash table. Apart from usual hash table,
chained hash table hashes N times as you add a value into the table.
This data type is widely used to create 2-Step Authenticators.

 Examples
 ========

>>> from sympy.crypto.crypto import ChainedHashTable
>>> table = ChainedHashTable(64)
>>> table.addChain('HELLOWORLD', 5)
>>> table.addChain('HELLO', 7)
>>> table.addChain('WORLD', 11)
>>> table.printTable()

Printing the table
========
>>> table.printTable()
"""

class ItemInfo:
    key = 0
    data = ""
    layer = 0
 
    def __init__(self,key,data,layer):
        self.key = key
        self.data = data
        self.layer = layer
 
    def toString(self):
        print('Key: {}, Value: {}, Hash Layer: {}'.format(self.key, str(self.data), self.layer) )

class ChainedHashTable:
    def __init__(self, capacity=128):
        self.capacity = capacity
        self.size = 0
        self.table = [0]*self.capacity
        self.itemList = []
        for i in range(self.capacity):
            self.itemList.append(ItemInfo(0,"",0))
    
    #Returns size used.
    def getSize(self):
        print ('You are using {} size of {} capacity'.format(self.size, self.capacity))
        return self.size

    def printTable(self):
        for i in range(self.capacity):
            if(self.table[i] != 0):
                print('Index: {} -> {}\n'.format(i, self.table[i]))
    
    #Wipes the table and fills it with ZEROs as its initialized value.
    def wipeTable(self):
        self.table = [0]*self.capacity
        self.itemList = []
        self.size = 0
        for i in range(self.capacity):
            self.itemList.append(ItemInfo(0,"",0))
    
    #Hashes the given value in hexadecimal.
    def getHash(self,obj):
        return hashlib.md5(str(obj)).hexdigest()

    #Calculates where the given hash value maps
    def getKey(self, hashed_value):
        return long(hashed_value, 16) % self.capacity

    #Create an n layer hash chain and insert into the table(data)     
    def addChain(self, item, n=10):
        hashes = []
        hash0 = self.getHash(str(item))
        hashes.append(hash0)
        
        for i in range(n-1):
            hashes.append(self.getHash(hashes[i]))
        key = self.getKey(hashes[len(hashes)-1]) # map according to the last hashed value.
        item = ItemInfo(key, item, n)
        
        if(self.table[key] != 0):
            self.table[key] = hashes
            self.itemList[key] = item
        else:
            self.table[key] = hashes
            self.itemList[key] = item
            self.size += 1

    #Returns found item's index and hashed layer number
    def search(self, item):
        for i in range(self.capacity):
            if(long(self.getHash(self.itemList[i].data), 16) == long(self.getHash(item), 16)):
                return [True, i, self.itemList[i].layer]
        return [False, -1, -1]

    #Returns found hash value's index and hashed layer
    def searchHash(self, hashed_value):
        for i in range(self.capacity):
            if(self.table[i] != 0):
                for j in range(len(self.table[i])):
                    if(self.table[i][j] == hashed_value):
                        return [True, i ,j]

        return [False, -1]
    
    #Returns item's random hash value from its layers
    def randomize(self, item):
        if(item == ''):
            return -1

        result = self.search(item)
        if(result[0] == True):
            index = result[1]
            hashedLayer = result[2]
            
            if(self.table[index] != 0):
                return self.table[index][randint(0, hashedLayer-1)]
        else:
            return -1

    #Fetches the data at given line number
    def fetchAtLine(self, index):
        if((int(index) < self.capacity) and (int(index) >= 0)):
            return self.table[int(index)]
        return -1
    
    #Controls whether the fetched data is correct
    def controlData(self, taken_hash):
        result = self.searchHash(taken_hash)
        
        if(result[0] == False):
            return False
        else:
            currentLayer = result[2]
            currentIndexOnTable = result[1]
            rangeAtIndex = len(self.fetchAtLine(currentIndexOnTable)) - int(currentLayer)
            hashes = []
            valueToHash = self.fetchAtLine(currentIndexOnTable)[0]
            hashes.append(valueToHash)

            for i in range(rangeAtIndex-1):
                hashes.append(self.getHash(hashes[i]))
            
            for k in range(len(hashes)):
                if(self.table[currentIndexOnTable][k] != hashes[k]):
                    return False
            return True
