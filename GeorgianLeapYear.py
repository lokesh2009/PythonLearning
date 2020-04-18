import calendar


def is_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100:
        return False
    elif year % 400 == 0:
        return True


print("********Enter the Year***********")
year = int(input("******: "))
print(is_leap(year))


