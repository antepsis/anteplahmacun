import sys
from sympy.crypto.chainedHashTable import ChainedHashTable

if __name__ == "__main__":
	table = ChainedHashTable(64)
	table.addChain('dogac0', 5)
	table.printTable()
