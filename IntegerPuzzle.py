print("********************************")
print("welcome to the Odd even puzzle")
print("********************************")
number_1 = int(input("Enter the first number"))
if number_1 % 2 == 0 and number_1 in range(2, 5) and number_1 >20:
                 print("Not Weird")

         elif number_1 % 2 != 0 or number_1 in range(6,21):
          print("Weird")
else number_1 in range(6, 21):
    print("Weird")
print("********************************")
