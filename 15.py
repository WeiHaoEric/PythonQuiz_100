# _*_ coding: utf-8 _*_
# Question 15
# Level 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def calResult(replaceWord, equation):
    word = list(replaceWord.keys())[0]
    val  = str(replaceWord[word])
    
    equation = equation.replace(word, val)

    sum = 0
    for p in equation.split("+"):
        sum+=int(p)

    return sum



equation = "a+aa+aaa+aaaa"
print(calResult({"a":9},equation))