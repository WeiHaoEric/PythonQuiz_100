# _*_ coding: utf-8 _*_
# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

class StrProcess(object):
  def __init__(self):
    self.data = None
    print("Create a StrProcess object....")

  def getString(self):
    self.data = input("type the string: ")
    print(f"you type {self.data}")

  def printString(self):
    print(self.data.upper())

strProcessor = StrProcess()
strProcessor.getString()
strProcessor.printString()