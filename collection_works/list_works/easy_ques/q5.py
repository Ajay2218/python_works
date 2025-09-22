

numbers = [1,2,3,1,2,3,4,1]

out = []

print(numbers)

for num in numbers:

    if num not in out :

        out.append(num)

print(out)