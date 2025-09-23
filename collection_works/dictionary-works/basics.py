

"""
dictionary

define {key:value,..}

key: value pair(unique key)

mutable




"""


dog = {"name":"dobermann","color":"black","price":30000,"gender":"male"}

#add
dog["age"] = 4

#update
dog["color"] = "white"

print(dog)

if "color" in dog:

    print(dog["color"])

else:

    print("not in dog")

