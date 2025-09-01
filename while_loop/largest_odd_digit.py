
n =int(input("enter the number = "))

while (n != 0):
    
    last_digit = n % 10

    if last_digit % 2 != 0 :
        
        print("largest odd number is =",n)

        break 
    
    n = n // 10
