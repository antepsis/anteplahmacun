class ChainedHashTable:
    def __init__(self, capacity=128):
        self.capacity = capacity;
        self.size = 0;
        self.keys = []
        self.data = [[] for _ in range(self.capacity)]


    def __str__(self):
        table_status = ""
        for cells in self.data:
            table_status += str(cells)
        return table_status


    def __len__(self):
        length = 0
        for i in self.data:
            length += len(i)
        return length


    def hash_it(obj, tablesize):  # gotta take mod through table size
        return sum([ord(c) for c in obj]) * 805306457


    def addUpdate(self, obj):
        hashed = self.hash_it(obj, self.capacity)
        for i in enumerate(self.data[hashed%self.capacity]):
            if self.data[i%self.capacity] == self.data[hashed%self.capacity]:
                print "Insert ERROR. This object already exists in the table."
            else:
                self.data.append(obj)

    def remove(self, key):

if __name__ == "__main__":
    table = ChainedHashTable(64)
                


    