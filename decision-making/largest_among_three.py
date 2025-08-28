
n1 = int(input("enter the 1st number = "))
n2 = int(input("enter the 2nd number = "))
n3 = int(input("enter the 3rd number = "))

if n1 > n2 and n1 > n3 :
    print(n1,"is greater")
elif n2 > n1 and n2 >n3:
    print(n2,"is greater")
elif n1 == n2 and n1 == n3:
    print("all are equal")
else:
    print(n3,"is greater")