def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


print("********Enter the Year***********")
year = int(input("******: "))
print(is_leap(year))


# Input = 1992-T,2100=F, 2000-T,1990-F,3455-F,2400-T

