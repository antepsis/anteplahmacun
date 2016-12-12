import hashlib

class ChainedHashTable:
    def __init__(self, capacity=128):
        self.capacity = capacity
        self.size = 0
        self.data = [0]*self.capacity

    def getSize(self):
        print ('You are using {} size of {} capacity'.format(self.size, self.capacity))

    def getString(self):
        print ('Hash table to the string: ')
    def getHash(self,obj):
        return sum([ord(c) for c in obj]) * 805306457

    def getKey(self, hashed_value):
        return hashed_value % self.capacity

    def addUpdate(self,item):
        hashed = self.getHash(item)
        key = self.getKey(hashed)
        
        if(self.size == 0):
            self.data[key] = hashed
            self.size += 1
        else:
            for i in range(self.capacity):
                if(self.data[i] == hashed):
                    self.data[key] = hashed #if the table includes the same item, override it.
                else:
                    self.data[key] = hashed
            self.size += 1

if __name__ == "__main__":
    table = ChainedHashTable(32)
    #table.addUpdate('52')
    table.addUpdate('sarp')
    table.addUpdate('dogac')
    table.getSize()
    print (table.data)
