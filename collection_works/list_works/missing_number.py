

numbers = [1,8,4,5,7,3,6,2]

numbers.sort()



for cu in range(0,len(numbers)-1):

    nex = cu + 1

    cu_element = numbers[cu]

    nex_element = numbers[nex]

    difference = nex_element - cu_element

    if difference != 1 :

       print("missing number is ",cu_element+1)

       break
if numbers[nex] == numbers[-1]:

    print(nex_element+1,"is missing")

        


