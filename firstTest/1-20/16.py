# _*_ coding: utf-8 _*_
# Question 16
# Level 2

# Question:
# Use a list comprehension to square each odd number in a list. 
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


#  === practice 1 ===
# testWords = "1,2,3,4,5,6,7,8,9"
# wordList = testWords.split(",")

# oddResult = [w for w in wordList if int(w)%2!=0]
# print(",".join(oddResult))

#  === practice 2 ===
testWords = "1,2,3,4,5,6,7,8,9"
print(",".join([w for w in testWords.split(",") if int(w)%2!=0]))

