from sympy import *

def Mercator_Series(x):
    
    if(x<=1 and x>-1):
        
        k = Symbol("k")
        function = ((-1)**(k+1))*(x**k)/k
        m = Sum(function ,(k,1,oo)).doit().evalf()

        return m

    else:
        raise ValueError("x have to be (-1< x <= 1)")

print(Mercator_Series(1))

def BBP_type_Natural_logarithm_of_2():

    k = Symbol("k")
    function = (-1)**(k-1)/k
    bbp = Sum(function,(k,1,oo)).doit().evalf()
    
    return bbp

print(BBP_type_Natural_logarithm_of_2())

def Lerch_Transcendent_For_Natural_Logarithm_Of_2():

    k = Symbol("k")
    function1 = ((-1)**k)*((1/(3*k+1))-(1/(3*k+2))+(1/(3*k+3)))
    function2 = ((-1)**k)*((1/(5*k+1))-(1/(5*k+2))+(1/(5*k+3))-(1/(5*k+4))+(1/(5*k+5)))
    lerch = Sum(function2,(k,0,oo)).doit().evalf()
    
    return pretty(lerch)

print(Lerch_Transcendent_For_Natural_Logarithm_Of_2())


    
