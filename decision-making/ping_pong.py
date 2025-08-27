
n = int(input("enter a number = "))

if n % 15 == 0 :
    print("PINGPONG")
elif n % 5 == 0 :
    print("PONG")
elif n % 3 == 0:
    print("PING")
else:
    print("invalid number")