# Read an integer .

# Without using any string methods, try to print the following:
# Sample input = 3 and output should be 123
# Range have functions End will give you result horizontal ,Sep will give you result in vertical, Flush
var, var1, var2 = 1, 2, 3
print(var)
print(var1, var2)

print("****************************************")
print("*******Enter the number")
# var = input("Enter the no")
print(*range(1, int(input())+1), sep='')
for i in range(3):
    print(i, end=" ")
print()

print("*******************************")
# using range for iteration
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=" ")
print()

print("=====================================")
summ = 0
for i in range(1, 11):
    summ = summ + i
print("Sum of first 10 natural number :", summ)