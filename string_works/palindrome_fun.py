

def is_palindrome(word):

    flag = True

    rev = word[::-1]

    if rev != word:

        flag = False

    return  flag

print(is_palindrome("malayalam"))

print(is_palindrome("man"))
