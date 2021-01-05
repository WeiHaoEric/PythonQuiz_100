# _*_ coding: utf-8 _*_
# Question:
# You are required to write a program to sort the 
# (name, age, height) tuples by ascending order where 
# name is string, age and height are numbers. 

# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [
# ('John', '20', '90'), ('Jony', '17', '91'), 
# ('Jony', '17', '93'), ('Json', '21', '85'), 
# ('Tom', '19', '80')
# ]

# Hints:
# In case of input data being supplied to the question, 
# it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.


from operator import itemgetter, attrgetter


print("=== itemgetter in Tuple")

dataTuple = [
            ('Tom', '19', '80') , 
            ('John', '20', '90'), 
            ('Jony', '17', '91'), 
            ('Jony', '17', '93'), 
            ('Json', '21', '85'), 
            ]

print(sorted(dataTuple,key= itemgetter(0,1,2)))


print("\n=== itemgetter in List")     
dataList = [
            ['Tom' , '19', '80'], 
            ['John', '20', '90'], 
            ['Jony', '17', '91'], 
            ['Jony', '17', '93'], 
            ['Json', '21', '85'], 
           ]
print(sorted(dataTuple, key=itemgetter(0,1,2)))


# === attrgetter 必需要搭配Class-object的型式，才能處理 ===
print("\n=== attrgetter in Object")           
class Student(object):
    def __init__(self, data):
        self.name  = data[0]
        self.age   = data[1]
        self.score = data[2]
    
    def __repr__(self):
        return repr((self.name, self.age, self.score))


studentList = [Student(s) for s in dataList]

print(sorted(studentList, key=attrgetter("name", "age", "score")))