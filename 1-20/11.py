# _*_ coding: utf-8 _*_
# Question 11
# Level 2

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers 
# as its input and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# === 練習1 ===
# inVal = input("type 4 digits and add common-separated:")
# inVal = "0100,0011,1010,1001"
# result = [v for v in inVal.split(",") if int(v,2)%5==0]
# print(",".join(result))

# === 練習2 ===
inVal = "0100,0011,1010,1001"
print(",".join([v for v in inVal.split(",") if int(v,2)%5==0 ]))
