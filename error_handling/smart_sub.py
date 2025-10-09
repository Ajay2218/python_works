

#create a fn smart_sub with two parameters return +num as result after suntraction

def smart_sub(n1,n2):

    result = n1 - n2

    return abs(result)



assert smart_sub(10,2) ==8,"test case1 failed with n1>n2"
assert smart_sub(2,10) ==8,"test case2 failed with n1<n2"

assert smart_sub(50,40) == 10,"test case3 failed"

print(smart_sub(10,20))

