
"""
read a year

dsiplay leap year 
else display non leap year

condition 
century year cheching
 year % 100 == 0 and year % 400 == 0

non century year checking
year % 100 !=0 and year % 4 == 0
"""

year = int(input("enter a year = "))

if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
