
file_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\file_works\\years.txt"

fw = open(file_path,"w")

for y in range(1890,2026):

    fw.write(str(y)+"\n")