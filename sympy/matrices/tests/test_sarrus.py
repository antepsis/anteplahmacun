from sympy.matrices.sarrus import sarrus
import unittest
class test_sarrus():

  def test_calc_sarrus_det():
    s = sarrus()
    m =[[2,1,0],[0,2,0],[2,0,1]]
    #testing proper value for proper entry
    assert s.calc_sarrus_det(m) == 4
    m1 =[[1,2],[3,4]]
    assert s.calc_sarrus_det(m1) == -2
    
  def test_calc_sarrus_det():
    s = sarrus()
    m =[[2,1,0],[0,2,0],[2,0,1]]
    #testing proper value for proper entry
    assert s.calc_reverse_matrix(m) == 4
    m1 =[[1,2],[3,4]]
    assert s.calc_reverse_matrix(m1) == -2
     

  test_calc_sarrus_det()
