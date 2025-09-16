

def merge_string(word1,word2):

    result = ""

    for i in range(0,len(word1)):

        merge_value = word1[i] + word2[i]

        result += merge_value

    return result

print(merge_string("abcd","pqrs"))
