
arr = [10,11,12,13,14,15,16]

#o/p = {10:even,11:odd...}

odd_even_dict = {num:"odd"if num %2 != 0 else "even" for num in arr}

print(odd_even_dict)
