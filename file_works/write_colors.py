

colors = ["red","blue","green","yellow","orange","black"]

file_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\file_works\\colors.txt"

fw = open(file_path,"a")

for clr in colors:

    fw.write(clr + "\n")
    
