
n = int(input("enter the number = "))

i = n
sum = 0

while (i != 0):
    
    last_digit = i % 10

    sum += last_digit

    i = i // 10

print("sum of digits in",n,"=",sum)