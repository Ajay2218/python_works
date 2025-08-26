

veh_num = int(input("enter the last 4 digit = "))

last_digit = veh_num % 10 

print(last_digit % 2 == 0 and last_digit > 5)