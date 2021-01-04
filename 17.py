# _*_ coding: utf-8 _*_
# Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction log 
# from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

isLoop = True
balance = 0
while (isLoop):
    action = input("Hello~tell me your action:")

    if("bye" in action):
        isLoop = False
        break

    actList = action.split()
    if actList[0]=="D":
        balance+=int(actList[1])
    elif actList[0]=="W":
        if(balance>int(actList[1])):
            balance-=int(actList[1])
        else:
            print("sorry, your balance is not enough...")
    
    print(f"===> your balance is ${balance}")


print("exit...")
    
        

    
    
