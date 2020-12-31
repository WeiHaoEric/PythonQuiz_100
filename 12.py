# _*_ coding: utf-8 _*_
# Question 12
# Level 2

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

startVal = 1000
endVal = 3000

result = []
for i in range(startVal, endVal+1):
    num = list(str(i))
    status = True

    # check all digits
    for d in range(len((num))):
        if(int(num[d]) % 2):
            status = False
            break

    if (status):
        result.append(str(i))

print(",".join(result))


print("\n=== practice again ===")
def getNumAllDigitEven(start, end):
  ans = []
  for i in range(start, end+1):
    status = True
    digitList = list(str(i))
    for d in range(len(digitList)):
      if(d % 2 != 0):
        status = False
        break
      if (status):
        ans.append(str(i))
  return ans

print(",".join(getNumAllDigitEven(200, 300)))
