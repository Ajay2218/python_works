
"""
dictionary comprehension -> easy way for creating dictionary iterable

syntax :

    variable_name = {key:value iteration  condition}

"""
#examples

arr = [10,11,12,13,14,15]
#       0  1  2  3  4  5

# o/p = {10:10^0,11:11^1...}

# {10:100,11:121....}

square_dict = {num:num**2 for num in arr}

print(square_dict)

cube_dict = {num:num**3 for num in arr}

print(cube_dict)

for index,value in enumerate(arr):

    print(index,value)

output = {value:value**index for index,value in enumerate(arr)}

print(output)
