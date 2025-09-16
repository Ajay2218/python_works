

word1 = input("enter first word : ")

word2 = input("enter second word : ")

if sorted(word1) == sorted(word2):

    print("it is an anagram")
    
else:

    print("not an anagram")