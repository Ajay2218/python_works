
n1 = int(input("enter number1 = ")) # 12

n2 = int(input("enter number2 = ")) # 24

i = 1

j =1

print( "common divisors are ") 

while(i <= n1 or j <= n2): # 1 <= 12 or 1 <= 24 (true)

    if n1 % i == 0 and n2 % j == 0: # 12 % 1 == 0 and 24 % 1 == 0 (true)

        if i == j: # 1 == 1 (true)

            print(i)#display 1

    i += 1 # i = 2

    j += 1 # j = 2