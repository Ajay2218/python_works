
n = int(input("enter a number = ")) # 123

while(n != 0): # 123 != 0 (true) 12 ! = 0 (t) , 1 != 0 (t)
        last_digit = n % 10 # 123 % 10 = 3 ,12 % 10 = 2 , 1 % 10 = 1

        print(last_digit) # display 3 2 1

        n = n // 10 # 123 // 10 = 12  , 12 // 10 = 1
        
