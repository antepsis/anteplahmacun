from sympy.combinatorics.combinations import combinations
import unittest
class test_combinations():
	

	def test_combination_norep():
		c = combinations()
		#c.combination_norep(5, 2)
		assert c.combination_norep(5, 3) == 10
		assert c.combination_norep(10, 3) == 120
		assert c.combination_norep(7, 4) == 35
		assert c.combination_norep(5, 2) == 10
		#assert c.combination_norep(5, "s") == 10

	def test_combination_withrep():
		c = combinations()
		assert c.combination_withrep(5, 3) == 35
		assert c.combination_withrep(10, 3) == 220
		assert c.combination_withrep(7, 4) == 210
		assert c.combination_withrep(5, 2) == 15
		#assert c.combination_withrep(5, "s") == 15




	test_combination_norep()
	test_combination_withrep()