
start_year = int(input("enter start year = "))

end_year = int(input("enter end year = "))

i = start_year

while(i <= end_year):

    if i % 100 == 0 and i % 400 == 0 or i % 100 != 0 and i % 4 == 0 :

        print(i)
    
    i += 1