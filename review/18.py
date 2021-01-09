# _*_ coding: utf-8 _*_

# Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

import re


def checkPwd(pwd):
    checkStatus = True
    pwdList = list(pwd)

    if(len(pwdList) < 6 or len(pwdList) > 12):
        checkStatus = False

    if (not re.search("[a-z]", pwd)):
        checkStatus = False
    elif (not re.search("[0-9]",  pwd)):
        checkStatus = False
    elif (not re.search("[A-Z]",  pwd)):
        checkStatus = False
    elif (not re.search("[$#@]",  pwd)):
        checkStatus = False
    else:
        pass

    return checkStatus
    # if(not checkStatus):
    # print(f"${pwd} is invalid.")

    # else:
    # print(f"${pwd} is valid!!.")


testPwd = ["ABd1234@1", "a F1#", "2w3E*", "2We3345"]

print("=== 方法1: 外層用loop去呼叫func ===")
result = []
for pwd in testPwd:
    if(checkPwd(pwd)):
        result.append(pwd)
print(",".join(result))


print("=== 方法2: 定義一個func，裡頭用loop搭配continue來撰寫 ===")

def loopToCheckPwd(pwdList):
    result = []
    for pwd in pwdList:
        strList = list(pwd)

        if(len(strList) < 6 or len(strList) > 12):
            continue

        if (not re.search("[a-z]", pwd)):
            continue
        elif (not re.search("[0-9]",  pwd)):
            continue
        elif (not re.search("[A-Z]",  pwd)):
            continue
        elif (not re.search("[$#@]",  pwd)):
            continue
        else:
            pass

        result.append(pwd)
    return result

ans = loopToCheckPwd(testPwd)
print(",".join(ans))