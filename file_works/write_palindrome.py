
words = ["hello","hai","madam","amma","malayalam","hey","neveroddoreven"]

file_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\file_works\\palindromes.txt"

fw = open(file_path,"w")

for w in words:

    if w == w[::-1]:

        fw.write(w+"\n")

        