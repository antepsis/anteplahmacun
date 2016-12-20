

def calc_sarrus_det(matrix):
#checking for size property is suitable for Sarrus Theorem
  size1 = len(matrix)
  size2 = len(matrix[0])
 # if(size1 != size2 or (size1 != 2 or size1 != 3)):
    # print("Can not calculate determinant with Sarrus Theorem(Matrix must be 2x2 or 3x3)")
  try:  
   if(size1 == size2 and size1 == 2):
      det2x2 = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]) 	
      return det2x2
   elif(size1 == size2 and size1 == 3):
     det3x3 = ((matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1] * matrix[1][2] * matrix[2][0]) + (matrix[0][2] * matrix[1][0] *matrix[2][1])) - ((matrix[2][0] * matrix[1][1] * matrix[0][2]) + (matrix[0][1] * matrix[1][0] *matrix[2][2]) + (matrix[0][0] * matrix[1][2] *matrix[2][1]))
     return det3x3
  except IndexError:
     print("Can not calculate determinant with Sarrus Theorem(Matrix must be 2x2 or 3x3)") 


m =[[3,-2,1],[5,6,2],[1,0]]

x = calc_sarrus_det(m)

print(x)
