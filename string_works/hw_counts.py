

text = "python has more than 3 frameworks 1 django 2 flask > @"

vowels = "aeiou"

digits = "0,1,2,3,4,5,6,7,8,9"

v_count = 0

symbols = "/,@,<,>,(,),[,]"

d_count = 0

s_count = 0

a_count = 0

con_count = 0

for ch in text:

    if ch in vowels:
        
        v_count += 1

    elif ch in digits:

        d_count += 1

    elif ch in symbols:

        s_count += 1
    
    elif ch != vowels and ch != symbols and ch != digits and ch != " ":

        con_count+= 1
    
a_count = v_count + con_count


print("vowels count = ",v_count)
print("digits count = ",d_count)
print("symbol count = ",s_count)
print("consonants count = ",con_count)
print("alphabet count = ",a_count)

