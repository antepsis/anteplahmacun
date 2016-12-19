from sympy import *

def Mercator_Series(x):

##Mercator series help us for finding ln(x + 1) using series
    
##But this series just for │x│ ≤ 1 ∧ -x ≠ 1.
##This gap not very high but you have to carefull because this mercator series can also calculate rational numbers.
##It means you can calculate infite numbers with this series
    
## ⎛⎧                                    ⎞
## ⎜⎪  ∞                                 ⎟
## ⎜⎪ ____                               ⎟
## ⎜⎪ ╲                                  ⎟
## ⎜⎪  ╲       k  k                      ⎟
##-⎜⎨   ╲  (-1) ⋅x                       ⎟
## ⎜⎪   ╱  ────────                      ⎟
## ⎜⎪  ╱      k                          ⎟
## ⎜⎪ ╱                                  ⎟
## ⎜⎪ ‾‾‾‾                               ⎟
## ⎜⎪k = 1                               ⎟
## ⎝⎩                                    ⎠
##



    

    if(x == None): # This progress not complete
        print("geldi")
    if(x<=1 and x>-1):
        
        k = Symbol("k")
        function = ((-1)**(k+1))*(x**k)/k
        m = Sum(function ,(k,1,oo)).doit().evalf()

        return m

    elif(x>1 or x<=-1):
        raise ValueError("x have to be (-1< x <= 1)")

    else: # This progress not complete
        print("geldi")
        k = Symbol("k")
        x = Symbol("x")
        function = ((-1)**(k+1))*(x**k)/k
        m = Sum(function ,(k,1,oo)).doit().evalf()

        return m

print(Mercator_Series(0.5))

def BBP_type_Natural_logarithm_of_2():



##This identity follows immediately from setting x=1 in the Mercator series, yielding

## ⎛⎧                                            ⎞
## ⎜⎪          ∞                                 ⎟
## ⎜⎪         ____                               ⎟
## ⎜⎪         ╲                                  ⎟
## ⎜⎪          ╲       k+1                       ⎟
##-⎜⎨           ╲  (-1)                          ⎟
## ⎜⎪ln(2) =    ╱  ────────                      ⎟
## ⎜⎪          ╱      k                          ⎟
## ⎜⎪         ╱                                  ⎟
## ⎜⎪         ‾‾‾‾                               ⎟
## ⎜⎪        k = 1                               ⎟
## ⎝⎩                                            ⎠
##
    

    k = Symbol("k")
    function = (-1)**(k-1)/k
    bbp = Sum(function,(k,1,oo)).doit().evalf()
    
    return bbp

print(BBP_type_Natural_logarithm_of_2())




def Simple_Series_For_Natural_Logarithm_Of_2(x):

## You can choose you series for calculating ln(2)


    k = Symbol("k")

    if(x==1):
        
    ## ⎛⎧                                            ⎞
    ## ⎜⎪          ∞                                 ⎟
    ## ⎜⎪         ____                               ⎟
    ## ⎜⎪         ╲                                  ⎟
    ## ⎜⎪          ╲                                 ⎟
    ##-⎜⎨           ╲      k⎛  1       1       1   ⎞ ⎟
    ## ⎜⎪ln(2) =    ╱  (-1) ⎜───── - ───── + ───── ⎟ ⎟
    ## ⎜⎪          ╱        ⎜ 3k+1    3k+2    3k+3 ⎟ ⎟
    ## ⎜⎪         ╱         ⎝                      ⎠ ⎟
    ## ⎜⎪         ‾‾‾‾                               ⎟
    ## ⎜⎪        k = 1                               ⎟
    ## ⎝⎩                                            ⎠
        
        function = ((-1)**k)*((1/(3*k+1))-(1/(3*k+2))+(1/(3*k+3)))
        
    elif(x==2):

    ## ⎛⎧                                                            ⎞
    ## ⎜⎪          ∞                                                 ⎟
    ## ⎜⎪         ____                                               ⎟
    ## ⎜⎪         ╲                                                  ⎟
    ## ⎜⎪          ╲                                                 ⎟
    ##-⎜⎨           ╲      k⎛  1       1       1       1       1   ⎞ ⎟
    ## ⎜⎪ln(2) =    ╱  (-1) ⎜───── - ───── + ───── - ───── + ───── ⎟ ⎟
    ## ⎜⎪          ╱        ⎜ 5k+1    5k+2    5k+3    5k+4    5k+5 ⎟ ⎟
    ## ⎜⎪         ╱         ⎝                                      ⎠ ⎟
    ## ⎜⎪         ‾‾‾‾                                               ⎟
    ## ⎜⎪        k = 1                                               ⎟
    ## ⎝⎩                                                            ⎠
        
        function = ((-1)**k)*((1/(5*k+1))-(1/(5*k+2))+(1/(5*k+3))-(1/(5*k+4))+(1/(5*k+5)))
        
    l = Sum(function,(k,0,oo)).doit().evalf()
    y = str(l)
    y = y[0:17]
    l = float(y)
    return l

print(Simple_Series_For_Natural_Logarithm_Of_2(2))

##
##def inverse_cosecant_Mercator(x):
##    x = Symbol("x")
##    print(pretty(Mercator_Series(x**2)))
##
##x = Symbol("x")
##inverse_cosecant_Mercator(x)
##
##a = I**2
##print(a)

    
