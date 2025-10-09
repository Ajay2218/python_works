numbers = [10,12,0,14,15,0,16,17,0]

pos1 = int(input("enter postion 1 = "))

pos2 = int(input("enter postion 2 = "))
"""
try:

    div = numbers[pos1] / numbers[pos2]

    print(div)
    
except Exception as e:

    print(e)
"""
try:
    elem1 = numbers[pos1]
    elem2 = numbers[pos2]
    try:
        div = elem1 /elem2

        print(div)
    
    except ZeroDivisionError as ze:

        print(ze)
        
except IndexError as ie:

    print(ie)

finally:

    print("write data to file")

    print("database commit")

    print("prgm completed")
