# _*_ coding: utf-8 _*_
# Question 20
# Level 3

# Question:
# Define a class with a generator 
# which can iterate the numbers, 
# which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield

def TestFunc(start, end):
    i = start
    while(i<end):
        if(i%7==0):
            yield i #<-- yield 宣告i為generator的object, 把它當作return來看，就好懂多了
        i+=1

# 方法1: 直接轉為generator -> list
print("=== 方法1 ===")
print(list(TestFunc(0, 10)))

# 方法2: 用for-loop直接對generator-object取值
print("=== 方法2 ===")
for i in TestFunc(start=0, end=10):
    print(i)

