
"""
text = "ababc"

wap to display 1st recursive character

"""

text = "ababc"

word = {}

for ch in text:

    if ch in word:

        word[ch] += 1
    
    else:

        word[ch] = 1

print(word)
