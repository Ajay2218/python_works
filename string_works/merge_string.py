

word1 ="abcd"

word2 = "pqrs"

merged_string =""

for index in range(0,len(word1)):

    conc_value = word1[index] + word2[index]

    merged_string += conc_value

print(merged_string)

