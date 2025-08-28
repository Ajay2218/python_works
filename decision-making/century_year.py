

"""
read a year

dsiplay century year if last 2 digit of year is 00
else display non century year

"""

year = int(input("enter a year = "))

if year % 100 == 0:
    print(year,"is a century year")
else:
    print(year,"is not a century year")