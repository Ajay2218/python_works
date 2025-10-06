
words = ["listen","act","post","earth","silent","cat","heart","stop"]

# o/p = {"listen":"silent", "act":"cat","earth":"heart","post":stop }
anagram_dict = {}

for w in words:

    if w not in anagram_dict:

        anagram_dict[w] = ""
    
    else:

        anagram_dict[w] = w