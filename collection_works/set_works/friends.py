

all_users = {"sachin","ajay","akhil","amal","dhoni","kohli","akash"}

ajay_frnds = {"sachin","amal","akhil","dhoni"}

sachin_frnds = {"ajay","akhil","amal"}

suggestions = all_users.difference(ajay_frnds)

suggestions.remove("ajay")

print(suggestions)

mutual_frnds = ajay_frnds.intersection(sachin_frnds)

print(mutual_frnds)