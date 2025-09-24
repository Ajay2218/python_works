

text = "this is a python programming language this is a simple python language"

words = text.split(" ")

frequency = {}

for c in words:

    if c in frequency:
        
        frequency[c] +=1

    else:

        frequency[c]=1

print(frequency)

for k,v in frequency.items():

    if v > 1:

        print(k)

