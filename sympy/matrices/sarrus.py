from numbers import Number
from decimal import Decimal
from fractions import Fraction
import copy

"""
SARRUS THEOREM TO CALCULATE DETERMINANT
Sarrus' rule or Sarrus' scheme is a method and a memorization scheme to compute the determinant of a 3×3 matrix. It is named after the French mathematician Pierre Frédéric Sarrus.

Consider a 3×3 matrix.

M= ( a11 a12 a13)
   ( a21 a22 a23)
   ( a31 a32 a33)


then its determinant can be computed by the following scheme:

Write out the first 2 columns of the matrix to the right of the 3rd column, so that you have 5 columns in a row. Then add the products of the diagonals going from top to bottom (solid) and subtract the products of the diagonals going from bottom to top (dashed). This yields:

a11  a12   a13 . a11 a12
   \     \      \
a21  a22   a23 . a21 a22                  |a11 a12 a13|
     \         \        \        det(M) = |a21 a22 a23| = a11*a22*a33 + a12*a23*a31 + a13*a21*a12 - a31*a22*a13 - a32*a23*a11 - a33*a21*a12 
a31  a32   a33 . a31 a32                  |a31 a32 a33|


A similar scheme based on diagonals works for 2x2 matrices:

         |a11 a12|  
det(M) = |a21 a22| = a11*a22 - a21*a12

(https://en.wikipedia.org/wiki/Rule_of_Sarrus)

CALCULATING INVERSE MATRIX USING SARRUS DETERMINANT
                    | |a22 a23|   |a13 a12|   |a12 a13| | 
                    | |a32 a33|   |a33 a32|   |a22 a23| |
                    |                                   |
  A^(-1) = 1/|A| *  | |a23 a21|   |a11 a13|   |a13 a11| |
                    | |a33 a31|   |a31 a33|   |a23 a21| |
                    |                                   |
                    | |a21 a22|   |a12 a11|   |a11 a12| |
                    | |a31 a32|   |a32 a31|   |a21 a22| |

(mathworld.wolfram.com/MatrixInverse.html)
"""

 #call calc_sarrus_det(m)
def calc_sarrus_det(matrix):
 #checking for size property is suitable for Sarrus Theorem
   size1 = len(matrix)
 
   size2 = len(matrix[0])
 
   for i in range(size1-1):

     for j in range(size2-1):

       if not (isinstance(matrix[i][j],Number)):

         #checking is the instance number or not
          raise ValueError("Matrix should be consist of only NUMBERS!")
  
   try:  

    if(size1 == size2 and size1 == 2):

       det2x2 = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]) 	

       return det2x2

    elif(size1 == size2 and size1 == 3):

      det3x3 = ((matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1] * matrix[1][2] * matrix[2][0]) + (matrix[0][2] * matrix[1][0] *matrix[2][1])) - ((matrix[2][0] * matrix[1][1] * matrix[0][2]) + 

 (matrix[0][1] * matrix[1][0] *matrix[2][2]) + (matrix[0][0] * matrix[1][2] *matrix[2][1]))

      return det3x3

   except IndexError:

      print("Can not calculate determinant with Sarrus Theorem(Matrix must be 2x2 or 3x3)")

    #call  calc_reverse_matrix(m)
def calc_reverse_matrix(matrix):

    determinant = calc_sarrus_det(matrix)

    print(determinant)

    printMatrix(matrix)

    reverseMatrix = copy.deepcopy(matrix)

    sizeR = len(reverseMatrix)

    if(sizeR == 3 and determinant !=0):

       reverseMatrix[0][0] = ((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1]))/determinant

       reverseMatrix[0][1] = ((matrix[0][2]*matrix[2][1])-(matrix[0][1]*matrix[2][2]))/determinant
	
       reverseMatrix[0][2] = ((matrix[0][1]*matrix[1][2])-(matrix[1][1]*matrix[0][2]))/determinant

       reverseMatrix[1][0] = ((matrix[1][2]*matrix[2][0])-(matrix[1][0]*matrix[2][2]))/determinant
     
       reverseMatrix[1][1] = ((matrix[0][0]*matrix[2][2])-(matrix[2][0]*matrix[0][2]))/determinant
     
       reverseMatrix[1][2] = ((matrix[0][2]*matrix[1][0])-(matrix[0][0]*matrix[1][2]))/determinant

       reverseMatrix[2][0] = ((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0]))/determinant

       reverseMatrix[2][1] = ((matrix[0][1]*matrix[2][0])-(matrix[0][0]*matrix[2][1]))/determinant

       reverseMatrix[2][2] = ((matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0]))/determinant
     
    
    elif(sizeR == 2 and determinant!=0):
       reverseMatrix[0][0] = matrix[1][1]/determinant
       reverseMatrix[0][1] = ((matrix[0][1])*-1)/determinant
       reverseMatrix[1][0] = (matrix[1][0]*-1)/determinant
       reverseMatrix[1][1] = matrix[0][0]/determinant
    else:
       raise ValueError("This matrix can not be reversed")
    return reverseMatrix
   
def printMatrix(matrix):

    size1 = len(matrix)

    size2 = len(matrix[0])

    for i in range(size1):

     for j in range(size2):

        print(matrix[i][j])

     print("\n")
    

#m =[[2,1,0],[0,2,0],[2,0,1]]
m=[[1,2,3],[0,1,4],[5,6,0]]
#m1 = [[1,2],[3,4]]
x = calc_reverse_matrix(m)
printMatrix(x)

