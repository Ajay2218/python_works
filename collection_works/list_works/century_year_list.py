
years = [1899,1900,2000,2021,2022,2023,1991,1992]

century_years = list()

non_century_years = list()

for yr in years:

    if yr % 100 == 0:

        century_years.append(yr)
    
    else:

        non_century_years.append(yr)

print("years",years)



print("century years",century_years)



print("non century years",non_century_years)