
n = int(input("enter the number = "))

i = n

j = n

sum = 0

n_count = 0

while (i != 0):

    digit = i % 10

    n_count += 1

    i = i // 10

while (j != 0):

    digit = j % 10

    exp = digit ** n_count

    sum += exp
    
    j = j // 10

if n == sum:
    print(n,"is armstrong number")
else:
    print(n,"is not an armstrong number")