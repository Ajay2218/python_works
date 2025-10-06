

numbers = [1,2,3,4,5,6,7,8,9,10]

odd_file_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\file_works\\odd_numbers.txt "

even_file_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\file_works\\even_numbers.txt" 

fw_even = open(even_file_path,"w")

fw_odd = open(odd_file_path,"w")

for num in numbers:

    if num % 2 == 0:

        fw_even.write(str(num) + "\n")
    
    else:

        fw_odd.write(str(num) + "\n")

