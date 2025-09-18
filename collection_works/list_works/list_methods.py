
"""
class list:

    def append(self,object) -> adding new object to a list(listnte end il ane add aava)
    def insert(self,index position,object) -> to add new object to a list using index value(index vech evide venenkilum add cheyaam)
    def pop(self,index=-1) -> remove and return item at specified index(default aayitt -1 ane(last iln delete aavum))
    def index(self,object) -> return first index value of an object
    def count(self,object) -> return no of occurance of an object in a list
    def reverse(self) -> to reverse a list 
    def clear(self) -> to clear all objects in a list
    def copy(self) -> return shallow copy of a list
    def sort(self,reverse=False) -> to sort a list(value True aanel desending order,false aanenkil asending order)
    def extend(self,iterable) -> to extend a list with another list
    def remove(self,object) -> to remove an object from a list

""" 
# examples:

# colors = ['red','green','blue']
#           0       1       2

# colors.append('black')

# colors.insert(1,"yellow")

# colors.pop(1)

# value = colors.index("blue")

# print(value)

# count = colors.count("green")

# print(count)

# colors.reverse()

# colors.append("white")

# colors_copy = colors.copy()

# print(colors_copy)

# colors.sort(reverse=True)

# print(colors)

arr1 = [10,20,30,40]

arr2 = [100,200,300,400]

arr1.extend(arr2)

print(arr1)

arr2.remove(100)

print(arr2)
