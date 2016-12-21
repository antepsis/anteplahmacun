import hashlib
import sys
from sympy.crypto.chainedHashTable import ChainedHashTable

def test_getSize():
    table = ChainedHashTable(32)
    table.addChain('test0', 5)
    table.addChain('test1', 3)
    assert table.getSize() == 2

def test_fetchAtLine():
    table = ChainedHashTable(32)
    assert table.fetchAtLine(5) == 0
    assert table.fetchAtLine('5') == 0

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
    table = ChainedHashTable(16)
    table.addChain('test', 7)
    table.addChain(66, 5)
    table.addChain('', 10)

    assert table.getSize() == 3


def test_search():
    table = ChainedHashTable(16)
    table.addChain('test1', 5)
    table.addChain('', 3)

    searchResults = [table.search('test1'), table.search(''), table.search('notexist')]
    for i in range(2):
        assert searchResults[i][0] == True
        assert searchResults[i][1] != -1
        assert searchResults[i][2] != -1
    assert searchResults[2][0] == False

def test_searchHash():
    table = ChainedHashTable(16)
    testHash = hashlib.md5('test').hexdigest()
    hashes = []
    hashes.append(testHash)

    for i in range(4):
        hashes.append(hashlib.md5(hashes[i]).hexdigest())
    key = table.getKey(hashes[len(hashes)-1])
    table.addChain('test', 5)
    tableData = table.fetchAtLine(key)
    
    for j in range(5):
        assert hashes[j] == tableData[j]

def test_randomize():
    table = ChainedHashTable(16)
    table.addChain('test0', 16)
    table.addChain('test1', 64)
    
    assert table.randomize('test0') != -1
    assert table.randomize('test1') != -1
    assert table.randomize('notexist') == -1
    assert table.randomize('') == -1

def test_controlData():
    table = ChainedHashTable(16)
    table.addChain('test1', 64)
    hashedValue0 = hashlib.md5('test1').hexdigest()
    hashedValue1 = hashlib.md5('notexist').hexdigest()
    hashes = []
    hashes.append(hashedValue0)

    for i in range(50):
        hashes.append(hashlib.md5(hashes[i]).hexdigest())
    assert table.controlData(table.randomize('test1')) == True
    assert table.controlData(hashes[45]) == True
    assert table.controlData(hashedValue1) == False
