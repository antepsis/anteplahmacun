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

def hash_chain_encrypt(msg, key):
	print ("")

def hash_chain_decrypt(msg, key):
	print ("")
