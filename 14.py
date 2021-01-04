# _*_ coding: utf-8 _*_

# Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number 
# of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def calWords(words):
    words = words.strip()
    result = {"Upper":0, "Lower":0}
    for w in list(words):
        if( w.isupper() ):
            result["Upper"]+=1
        elif( w.islower() ):
            result["Lower"]+=1
        else:
            continue
    
    return result

testWord = "Hello world!"
print(calWords(testWord))
