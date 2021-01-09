# _*_ coding: utf-8 _*_
# Question 24
# Level 1

# Question:
# Python has many built-in functions, and if you do not know how to use it, 
# you can read document online or find some books. But Python has a built-in document 
# function for every built-in functions.
# Please write a program to print some Python built-in functions documents, 
# such as abs(), int(), raw_input()
# And add document for your own function
    
# Hints:
#     The built-in document method is __doc__

print("每個python內建的func都有一個函式 func.__doc__ 可以讓你查詢，如下:")

explain = print.__doc__
print("=== explain how to use print func")
print(explain)