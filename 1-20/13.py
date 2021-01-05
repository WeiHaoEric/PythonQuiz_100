# _*_ coding: utf-8 _*_
# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def statistic(setence):
    result = {"letters": 0, "digits": 0}
    setence = setence.replace(" ", "")
    setence = setence.replace("!", "")
    for c in list(setence):
        # === method1 ===
        # isInt = True
        # try:
        #     int(c)
        # except:
        #     isInt = False

        # if(isInt):
        #     result["digits"] += 1
        # else:
        #     result["letters"] += 1

        # === method2 ===
        if (c.isdigit()):
          result["digits"] += 1
        else:
          result["letters"] += 1

    return result


setence = "hello world! 123"
print(statistic(setence))
