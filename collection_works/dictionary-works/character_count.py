
text = "abcbcdbcd"

char_count = {}

for ch in text:

    if ch in char_count:

        char_count[ch] += 1
    
    else:

        char_count[ch] = 1

for k,v in char_count.items():

    if v == 1:

        print(k)

    

