import calendar


# This is the Georgian calender puzzle to show up the leap year or not We add a Leap Day on February 29, almost every
# four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year,
# February. In the Gregorian calendar three criteria must be taken into account to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year

def is_leap(year):
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 4 != 0 or year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 400 != 0:
        return False
    elif year % 4 != 0 and year % 400 == 0:
        return False

    else:
        year % 100 != 0
        return False


print("********Enter the Year***********")
year = int(input("******: "))
print(is_leap(year))

# Input = 1992-T,2100=F, 2000-T,1990-F,3455-F,2400-T