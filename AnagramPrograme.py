# Python program to check whether two strings are
# anagrams of each other

# function to check whether two strings are anagram
# of each other
str1 = input("Enter the first string")
str2 = input("enter the Second string")

lenstr1 = len(str1)
print(lenstr1)
lenstr2 = len(str2)
print(lenstr2)
if lenstr1 != lenstr2:
    print("Both string never be anagram")
else:
    sort1 = sorted(str1)
    sort2 = sorted(str2)
    print('Sorted list 1', format(sort1))
    print("Sorted list 2",format(sort2))
    if sort1 == sort2:
        print("This string is anagram")
    else:
        print("This string is not anagram")

        # print(sort1 and sort2)
