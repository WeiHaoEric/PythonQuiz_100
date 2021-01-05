# _*_ coding: utf-8 _*_
# Question 25
# Level 1

# Question:
# Define a class, which have a class parameter
# and have a same instance parameter.

# Hints:
# Define a instance parameter, need add it in __init__ method
# You can init a object with construct parameter or set the value later


class STUDENT(object):
    name = "CLASS-NAME: STUDENT"

    def __init__(self, name):
        self.name = name

eric = STUDENT("Eric")
print(f"This name ${STUDENT.name} is only for class, not instance ${eric.name}")
Ray = STUDENT("Ray")
print(f"This name ${STUDENT.name} is only for class, not instance ${Ray.name}")

