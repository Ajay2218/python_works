
n1 = int(input("enter number1 = "))

n2 = int(input("enter number2 = "))

for i in range(1,min(n1,n2)+1,1):

    if n1 % i == 0 and n2 % 2 == 0:
        print(i)
