from sympy.matrices.sarrus import sarrus
import unittest
class test_sarrus():

  def test_calc_sarrus_det():
    s = sarrus()
    m =[[2,1,0],[0,2,0],[2,0,1]]
    assert s.calc_sarrus_det(m) == 4


  test_calc_sarrus_det()
