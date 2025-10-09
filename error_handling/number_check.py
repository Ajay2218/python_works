
#create a function is_positive with 1 parameter num return True if num is +ve else return false

def is_positive(num):

    result = True
    
    result = num > 0
    
    return result

assert is_positive(10) == True,"text case1 failed with num > 0"

assert is_positive(-10) == False,"test case2 failed with num < 0"

assert is_positive(0) == False,"test case3 is failed"