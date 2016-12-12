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
        return str(sum([ord(c) for c in obj]) * 805306457)

    def getKey(self, hashed_value):
        return long(hashed_value) % self.capacity

    def addUpdateToTable(self,item, key):
        hashed = self.getHash(item)
        #key = self.getKey(hashed)
        
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
    #create a chain    
    def addChain(self, item, n=10):
        hashes = []
        hash0 = self.getHash(item)
        hashes.append(hash0)
        for i in range(n-1):
            hashes.append(self.getHash(hashes[i]))
        print hashes
        print len(hashes)
        key = self.getKey(hashes[len(hashes)-1])
        print ('key: {}'.format(key))
        self.addUpdateToTable(hashes, key)


    #def migrate

if __name__ == "__main__":
    table = ChainedHashTable(32)
    #table.addUpdate('52')
    #table.addUpdate('sarp')
    #table.addUpdate('dogac')
    #table.getSize()
    #print (table.data)
    table.addChain('dogac', 5)
