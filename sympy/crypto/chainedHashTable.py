import hashlib
from random import randint

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
    def getSize(self):
        print ('You are using {} size of {} capacity'.format(self.size, self.capacity))

    def getTable(self):
        print self.table

    def wipeTable(self):
        self.table = [0]*self.capacity
        self.itemList = []
        self.size = 0
        for i in range(self.capacity):
            self.itemList.append(ItemInfo(0,"",0))

    def getHash(self,obj):
        return hashlib.md5(obj).hexdigest()

    def getKey(self, hashed_value):
        return long(hashed_value, 16) % self.capacity

    #Create an n layer hash chain and insert into the table(data)     
    def addChain(self, item, n=10):
        hashes = []
        hash0 = self.getHash(item)
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

    #returns found item's index and hashed layer number
    def search(self, item):
        for i in range(self.capacity):
            if(long(self.getHash(self.itemList[i].data), 16) == long(self.getHash(item), 16)):
                return [True, i, self.itemList[i].layer]
        return [False, -1, -1]
    
    def searchHash(self, hashedItem):
        print ('')

    def control(self, givenItem, foundItem):
        print ('')

    def randomize(self, item):
        result = self.search(item)
       
       if(result[0] == True):
            index = result[1]
            return self.table[index][randint(0, int(result[2]))]
        else:
            return -1
            
    #def migrate

if __name__ == "__main__":
    table = ChainedHashTable(32)
    #table.addUpdate('52')
    #table.addUpdate('sarp')
    #table.addUpdate('dogac')
    #table.getSize()
    #print (table.table)
    table.addChain('dogaco', 5)
    table.addChain('heyho', 10)
    print (table.randomize('heyho'))
    print (table.search('dogac'))
#    print long((table.getHash('dogac')), 16) % 32
