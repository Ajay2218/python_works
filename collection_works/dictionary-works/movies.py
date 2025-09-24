

movies = {
    "id":1,
    "title":"kgf",
    "language":"malayalam",
    "duration":120,
    "genre":"action"
}

print("----values----")

for v in movies.values():

    print(v)

print(movies.get("language"))

print("----key and values")

for k,v in movies.items():

    print(k,":",v)

movies.update(duration=160,director="yash")

print(movies)