import hashlib
import sys
from sympy.crypto.chainedHashTable import ChainedHashTable

def test_getSize():
    table = ChainedHashTable(32)
    table.addChain('test0', 5)
    table.addChain('test1', 3)
    assert table.getSize() == 2

def test_wipeTable():
    table = ChainedHashTable(16)
    table.addChain('test0', 5)
    table.addChain('test1', 23)
    table.addChain('test2', 7)
    table.addChain('test3', 4)
    size = table.getSize()
    
    table.wipeTable()
    assert size != table.getSize()
    for i in range(16):
        assert table.fetchAtLine(i) == 0

def test_getHash():
    table = ChainedHashTable(16)
    hexHash0 = hashlib.md5('test').hexdigest()
    hexHash1 = hashlib.md5('').hexdigest()
    assert hexHash0 == table.getHash('test')
    assert hexHash1 == table.getHash('')

def test_getKey():
    table = ChainedHashTable(16)
    hashedValue0 = hashlib.md5('test').hexdigest()
    hashedValue1 = hashlib.md5('').hexdigest()
    key0 = table.getKey(hashedValue0) 
    key1 = table.getKey(hashedValue1)
    assert key0 >= 0 and key0 <= 16
    assert key1 >= 0 and key1 <= 16

def test_addChain():
    print ('Going to be filled.')

def test_search():
    print ('Going to be filled.')

def test_searchHash():
    print ('Going to be filled.')

def test_randomize():
    print ('Going to be filled.')

def test_fetchAtLine():
    print ('Going to be filled.')

def test_controlData():
    print ('Going to be filled.')


if __name__ == "__main__":
    test_getSize()
    test_wipeTable()
    test_getHash()
    test_getKey()
    test_addChain()
    test_search()
    test_searchHash()
    test_randomize()
    test_fetchAtLine()
    test_controlData()
