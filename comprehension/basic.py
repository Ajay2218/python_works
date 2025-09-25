

"""
list comprehension

syntax :

    variable = [return value  iteration   condition]
"""

#example

arr = [10,20,11,15,30,40]

squares = [num**2 for num in arr ]

print(squares)

cubes = [num**3 for num in arr]

print(cubes)

num_gt_25 = [num for num in arr if num > 25]

print(num_gt_25)

num_add_5 = [num+5 for num in arr ]

print(num_add_5)
