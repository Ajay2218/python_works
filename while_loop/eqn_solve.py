
n = int(input(" enter the number = "))

sum = 0

while (n != 0):

    digit = n % 10

    cube = digit ** 3

    sum += cube

    n = n // 10

print(sum)