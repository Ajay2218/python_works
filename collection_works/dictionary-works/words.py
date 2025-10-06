

text = "hai hello hello hai goodmorning hello goodmorning"

words = text.split()

word_count = {}

for ch in words:

    if ch in word_count:

        word_count[ch] += 1
    
    else:

        word_count[ch] = 1

print(word_count)

sorted_arr = sorted(word_count,reverse=False,key =word_count.get)

print(sorted_arr)