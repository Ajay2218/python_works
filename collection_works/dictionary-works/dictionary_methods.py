

"""
class dict:

    def keys(self) : return all keys

    def values(self) : returns all values

    def items(self) : return key and values 

    def pop(self,key) : remove the specific key value

    def get(self,key) : return the value of specified key

    def update(self,key) :
"""

#examples

course = {
    "id":"dj123",
    "name":"django",
    "duration":6,
    "fee":35000
}

all_keys = course.keys()

all_values = course.values()

print("------keys--------")

for k in all_keys:

    print(k)

print("----values-----")

for v in all_values:

    print(v)

print("----items-----")

for k,v in course.items():

    print(k,":",v)


print("----pop---")

course.pop("fee")

print(course)

print("------get-------")

print(course.get("name"))

print("----------")
