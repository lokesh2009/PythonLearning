
import random, operator

print("*************************************************")
print("******Design tick tack toe***********************")


def randomCalc(i, j):
ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}

num = [1, 2, 3, 4]
num1, num2 = num[i], num[j]
op = (list(ops.keys()))[i]
answer = round(ops.get(op)(num1, num2), 3)
print('What is {} {} {}?\n'.format(num1, op, num2))
return answer

