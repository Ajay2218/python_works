"""

based on bmi display health condition

under weight
normal weight
over weight
obese
eqn  bmi = weight_in_kg/height_in m^2)
"""
height = int(input("enter a height in cm = "))

weight = int(input("enter weight in kg = "))

height_in_m = height / 100

bmi = weight/(height_in_m**2)
print("bmi value is",round(bmi))

if bmi >= 30:
    print("obese bmi")
elif bmi >= 25:
    print("over weight bmi")
elif bmi >= 20:
    print("normal bmi")
elif bmi < 20:
    print("under weight")
else:
    print("invalid value")