

arr = [2,3,4,5,6,7,12,1,13,14,15]

odd_nums = []

even_nums = list()

for num in arr:

    if num % 2 == 0:

        even_nums.append(num)
    
    else:

        odd_nums.append(num)


print(arr)

print(odd_nums)

print("-------")

print(even_nums)
