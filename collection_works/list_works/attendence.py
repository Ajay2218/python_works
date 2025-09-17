

last_week_attendence = ["H","O",'O','P','H','A','O']

last_week_attendence[2] = 'P'


"""
for at in last_week_attendence:

    if at == 'H':

        print("holiday")

    elif at == 'O':

        print("online")

    elif at == 'P':

        print("offline")

    elif at == 'A':

        print("absent")
"""
h_count = 0

O_count = 0

p_count = 0

a_count = 0

for at in last_week_attendence:

    if at == "H":

        h_count += 1

    elif at == "O":

        O_count += 1
        
    elif at == "P":

        p_count += 1

    elif at == "A":

        a_count += 1



print(last_week_attendence)

print(h_count,"holiday")

print(O_count,"online")

print(p_count,"offline")

print(a_count,"absent")

