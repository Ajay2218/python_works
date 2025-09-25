
"""
wap to display most recursive character

text = "ababc

"""


text = "ababca"

word = {}

for ch in text:

    if ch in word:

        word[ch] += 1
    
    else:

        word[ch] = 1

print(word)
