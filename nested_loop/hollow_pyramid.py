

for i in range(1,5):

    for j in range(1,8):

        if  i + j == 5 or j - i == 3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    
for i in range(4,0,-1):

    for j in range(7,0,-1):

        if  i + j == 5 or j - i == 3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    