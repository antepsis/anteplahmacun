import hashlib
class ItemInfo:
    key = 0
    data = ""
 
    def __init__(self,key,data):
        self.key = key
        self.data = data
 
    def toString(self):
        print("  '" + self.key + "' / " + str(self.value) )

class ChainedHashTable:
    def __init__(self, capacity=128):
        self.capacity = capacity
        self.size = 0
        self.itemList = [0]*self.capacity
        self.table = [0]*self.capacity

    def getSize(self):
        print ('You are using {} size of {} capacity'.format(self.size, self.capacity))

    def getTable(self):
        print self.table

    def wipeTable(self):
        self.table = [0]*self.capacity
        self.itemList = [0]*self.capacity
        self.size = 0

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
       # print hashes
       # print len(hashes)
        key = self.getKey(hashes[len(hashes)-1]) # map according to the last hashed value.
        item = ItemInfo(key, item)
       # print ('key: {}'.format(key))
        #self.addUpdateToTable(hashes, key)
        if(self.table[key] != 0):
            self.table[key] = hashes
            self.itemList[key] = item
        else:
            self.table[key] = hashes
            self.itemList[key] = item
            self.size += 1
        print self.table 

    def find(self, item):
        print ('found value')
    
    def randomizeMsg(self):
        print ('')
    #def migrate

if __name__ == "__main__":
    table = ChainedHashTable(32)
    #table.addUpdate('52')
    #table.addUpdate('sarp')
    #table.addUpdate('dogac')
    #table.getSize()
    #print (table.table)
    table.addChain('dogaco', 5)
#    print long((table.getHash('dogac')), 16) % 32
