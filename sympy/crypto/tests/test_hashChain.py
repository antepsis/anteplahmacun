import sys
from sympy.crypto.chainedHashTable import ChainedHashTable

if __name__ == "__main__":
	table = ChainedHashTable(32)
	table.addChain('sikik', 7)
	table.printTable()
	print (table.randomize('sikik'))
