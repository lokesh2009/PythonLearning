print("********************************")
print("welcome to the Odd even puzzle")
print("********************************")
number_1 = int(input("Enter the first number :"))
if number_1 % 2 == 0:
    if number_1 in range(2, 5):
        print("Number is  Not Weird")
    elif number_1 in range(6, 21):
        print("************Weird**************")
        print("Number is in range (6,21) and not greater than 20, that's why it is  called Weird")
    elif number_1 > 20:
        print("************Not Weird************")
        print(" number > 20 and  is even, so it isn't weird. Thus, we print Not Weird.")
elif number_1 % 2 == 1:
    print("***********Weird**************")
print("********************************")
print("#####################################")

# https://github.com/lokesh2009/PythonLearning