from __future__ import print_function

from string import whitespace, ascii_uppercase as uppercase, printable

from sympy import nextprime
from sympy.core import Rational, Symbol
from sympy.core.numbers import igcdex, mod_inverse
from sympy.core.compatibility import range
from sympy.matrices import Matrix
from sympy.ntheory import isprime, totient, primitive_root
from sympy.polys.domains import FF
from sympy.polys.polytools import gcd, Poly
from sympy.utilities.misc import filldedent, translate
from sympy.utilities.iterables import uniq
from sympy.utilities.randtest import _randrange
import hashlib

#The ideal cryptographic hash function has four main properties:
#1. it is easy to compute the hash value for any given message
#2. it is infeasible to generate a message that has a given hash
#3. it is infeasible to modify a message without changing the hash
#4. it is infeasible to find two different messages with the same hash.
#Because of the reasons above, there is no conversion from hashed string to the original one.

#multiply incoming msg with an prime number which is 982,451,653
def hash_function(msg):
    return hashlib.md5(msg).hexdigest()

#Hash the given message n(hash_layer) times.
def hash_chain_encrypt(msg, hash_layer):
	print ("")

#Decrypt the given message according to its layer depth.
def hash_chain_decrypt(msg_list, hash_layer):
	print ("")

#There must not be collisions and the table has to be flexible.
#Hash table will have l lines and every line containing n length LinkedList.
def hash_table_handler(msg, hash_layer, addOrDel):
    print("add/remove from hash table")


if __name__ == "__main__":
    msg = "dogac"
    hashed = hashlib.md5(msg).hexdigest()
    hashed2 = hash_function(hashed)
    print (hashed2)
