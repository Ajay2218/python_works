

"""
lambda function
    definition: anonymous function with one expression

    syntax :
        reference_name = lambda p1,p2,p3....pn:expression

    eg:

       add = lambda n1,n2:n1+n2

       cube = lambda n:n**3

"""

add = lambda n1,n2:n1 + n2

print(add(10,20))

#create a lambda function with 2 parameter that return largest number and smallest

max_min = lambda n1,n2: n1 if n1 >n2 else n2

print(max_min(10,15))

min2 = lambda n1,n2: n1 if n1 < n2 else n2

print(min2(10,4))

# create a lambda fun with 1 parameter n return true if n is even else false

even1 = lambda n : True if n % 2 == 0 else False

print(even1(5))
