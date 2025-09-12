

def prime(n):

    flag = True

    for i in range(2,n):

       if n % i == 0:
           
           return False
           
           break
       
    return flag

n = int(input("enter a number = "))

print(prime(n))
        

