

def is_pangram(word):

    flag = True

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for ch in alphabets:

        if ch not in word.lower():

            flag = False

            break

    return flag

print(is_pangram("helllo world"))