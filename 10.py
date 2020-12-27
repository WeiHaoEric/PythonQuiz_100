# _*_ coding: utf-8 _*_
# Question 10
# Level 2

# Question:
# Write a program that accepts a sequence of whitespace separated words as 
# nput and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.


# inVal = input("input with whitespace-separated, ex: a b c: ")
inVal = "hello world and practice makes perfect and hello world again"
inVal = set(inVal.split(" ")) # set type
inVal = list(inVal)

# list type
#sort method 1:可針對list進行排序
inVal.sort() 
print("Sort Mehod 1: ",' '.join(inVal))

#sort method 2:也可透過一個sorted func針將list當作輸入參數，進行排序
inVal2 = sorted(inVal)


print("Sort Mehod 2: ",' '.join(inVal2))
