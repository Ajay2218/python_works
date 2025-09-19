

numbers = [10,20,30,40,10,11,12,20,40,20]

duplicates = list()

for num in numbers:

    if numbers.count(num) > 1 and num not in duplicates:

        duplicates.append(num)


print(numbers)

print()

print("duplicates",duplicates)



print("method 2")

digits = [10,11,12,13,10,14,15,14,11]

digits.sort()

dup = list()

for c in range(0,len(digits)-1):

    n = c + 1

    c_element = digits[c]

    n_element = digits[n]
    
    difference = c_element - n_element

    if difference == 0 and c_element not in dup:

        dup.append(c_element)
    
print(dup)





