

gender = input("enter gender = ")

height = int(input("enter the height in cm = "))

weight = int(input("enter the weight in kg = "))

age = int(input("enter the age = "))

activity_level = 1.2

if gender == "male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5 
else:
     bmr = 10 * weight + 6.25 * height - 5 * age - 161

calories = bmr * activity_level

print(calories)