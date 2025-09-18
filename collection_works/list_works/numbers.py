
numbers=[10,11,14,3,8,19,20,21,22,23,56]

print(numbers)

print()

print("odd numbers :")

for od in numbers:

    if od % 2 != 0:

        print(od)

print()

print("even numbers :")

sum = 0

for ev in numbers:

    if ev % 2 == 0:

        print(ev)

        sum += ev

print()

print("sum of all even numbers : ",sum)
