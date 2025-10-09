

file_input_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\file_works\\numbers.txt"

file_write_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\file_works\\result.txt"

numbers = []

fr = open(file_input_path,"r")

fw = open(file_write_path,"w")

for line in fr:

    number = int(line.rstrip("\n"))

    for num in number:

        numbers = numbers.append(num)

print(numbers)