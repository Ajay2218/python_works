

def arm(n):

    copy = n

    count = len(str(n))

    result = 0

    while(n != 0):

        last_digit = n % 10

        exp = last_digit**count

        result+=exp

        n = n // 10
    return copy == result

n = int(input("enter the number = "))

print(arm(n))