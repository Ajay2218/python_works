
file_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\file_works\\data.txt"

fr = open(file_path,"r")

all_words = []

for line in fr:

    words  = line.rstrip("\n").lower().split(' ')

    for w in words:

        all_words.append(w)

word_count = {w:all_words.count(w) for w in all_words}

print(word_count)