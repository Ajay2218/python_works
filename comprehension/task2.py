

words = ["ab","cd","ef","gh","ab","cde","ef"]

new_words = [w.upper() for w in words]

print(new_words)

# create new dictionary from words set word as key and value as lent=gth of that word

new_dict = {w:len(w) for w in words}

print(new_dict)
