

arr = [3,4,5,6,7,8,9,10]

#create  new list that contain cube of all  numbers

cube = [num**3 for num in arr]

print(cube)

# create a new list which contain only even numbers

even_numbers = [num for num in arr if num % 2 == 0]

print(even_numbers)

# create a new list which contain only odd numbers

odd_numbers = [num for num in arr if num % 2 != 0]

print(odd_numbers)

