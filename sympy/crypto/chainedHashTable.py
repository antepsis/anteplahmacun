def hash_it(key, tablesize):
    return sum([ord(c) for c in key]) * 805306457

class chainedHashTable:
	
	def __init__(self, capacity = 128):
		self.capacity = capacity;
		self. size = 0;
		self.keys = []
		self.data = [[] for _ in range(capacity)]

    def addUpdate(self, obj):
        

    def remove(self, key):


    def fetch(self, key):
        def fetch_item(item, _):
            if item:
                return item[1]
            else
                raise KeyError(key)
                


    