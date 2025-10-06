
file_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\file_works\\years.txt"

fr = open(file_path,"r")

for y in fr: # "1890\n"
    year =int(y.rstrip("\n"))

    if year % 400 == 0 and year % 100 == 0 or year % 100 != 0 and year % 4 == 0:

        print(year)

