# _*_ coding: utf-8 _*_
# Question 7
# Level 2

# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints:
# Note: In case of input data being supplied to the question,
# it should be assumed to be a console input in a comma-separated form.

def dimFunc(X, Y):
  result = []
  for i in range(X):
    tmp = []
    for j in range(Y):  
      tmp.append(j*i)
    result.append(tmp)

  return result

val = input("type 2 digits and separated by common for X,Y:")


# print(dimFunc(3,5)) # for test

dimVal = [int(v) for v in val.split(",")]
print( dimFunc(dimVal[0],dimVal[1]) )


