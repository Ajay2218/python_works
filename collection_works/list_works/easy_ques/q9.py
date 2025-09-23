

numbers = [10,20,15,2,40,100,120,50]

numbers.sort()

for i in range(0,len(numbers)-1):

    j = i + 1

    i_elem = numbers[i]

    j_elem = numbers[j]

print(numbers)

print("second largest number is ",i_elem)
