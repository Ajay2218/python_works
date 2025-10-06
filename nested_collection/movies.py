

movies = [
  {"id": 1, "title": "3 Idiots", "runtime": 171, "director": "Rajkumar Hirani", "rating": 8.4, "genre": "Comedy/Drama", "language": "Hindi"},
  {"id": 2, "title": "Dangal", "runtime": 161, "director": "Nitesh Tiwari", "rating": 8.3, "genre": "Biography/Sports", "language": "Hindi"},
  {"id": 3, "title": "Gully Boy", "runtime": 153, "director": "Zoya Akhtar", "rating": 7.9, "genre": "Musical/Drama", "language": "Hindi"},
  {"id": 4, "title": "Piku", "runtime": 123, "director": "Shoojit Sircar", "rating": 7.6, "genre": "Drama/Comedy", "language": "Hindi"},
  {"id": 5, "title": "Andhadhun", "runtime": 139, "director": "Sriram Raghavan", "rating": 8.2, "genre": "Thriller/Crime", "language": "Hindi"},

  {"id": 6, "title": "Baahubali: The Beginning", "runtime": 159, "director": "S. S. Rajamouli", "rating": 8.0, "genre": "Action/Fantasy", "language": "Telugu"},
  {"id": 7, "title": "Arjun Reddy", "runtime": 182, "director": "Sandeep Reddy Vanga", "rating": 8.1, "genre": "Romance/Drama", "language": "Telugu"},
  {"id": 8, "title": "Jersey", "runtime": 160, "director": "Gowtam Tinnanuri", "rating": 8.5, "genre": "Sports/Drama", "language": "Telugu"},
  {"id": 9, "title": "Eega", "runtime": 145, "director": "S. S. Rajamouli", "rating": 7.7, "genre": "Fantasy/Action", "language": "Telugu"},
  {"id": 10, "title": "Rangasthalam", "runtime": 170, "director": "Sukumar", "rating": 8.4, "genre": "Action/Drama", "language": "Telugu"},

  {"id": 11, "title": "Drishyam", "runtime": 160, "director": "Jeethu Joseph", "rating": 8.3, "genre": "Thriller/Crime", "language": "Malayalam"},
  {"id": 12, "title": "Premam", "runtime": 156, "director": "Alphonse Puthren", "rating": 8.3, "genre": "Romance/Drama", "language": "Malayalam"},
  {"id": 13, "title": "Kumbalangi Nights", "runtime": 135, "director": "Madhu C. Narayanan", "rating": 8.6, "genre": "Drama/Comedy", "language": "Malayalam"},
  {"id": 14, "title": "Bangalore Days", "runtime": 171, "director": "Anjali Menon", "rating": 8.3, "genre": "Romance/Drama", "language": "Malayalam"},
  {"id": 15, "title": "Uyare", "runtime": 125, "director": "Manu Ashokan", "rating": 8.0, "genre": "Drama", "language": "Malayalam"},

  {"id": 16, "title": "Super Deluxe", "runtime": 176, "director": "Thiagarajan Kumararaja", "rating": 8.4, "genre": "Thriller/Drama", "language": "Tamil"},
  {"id": 17, "title": "Kaithi", "runtime": 145, "director": "Lokesh Kanagaraj", "rating": 8.5, "genre": "Action/Thriller", "language": "Tamil"},
  {"id": 18, "title": "Pariyerum Perumal", "runtime": 155, "director": "Mari Selvaraj", "rating": 8.8, "genre": "Drama", "language": "Tamil"},
  {"id": 19, "title": "Vikram", "runtime": 173, "director": "Lokesh Kanagaraj", "rating": 8.3, "genre": "Action/Thriller", "language": "Tamil"},
  {"id": 20, "title": "Soorarai Pottru", "runtime": 153, "director": "Sudha Kongara", "rating": 8.7, "genre": "Biography/Drama", "language": "Tamil"}
]

# display all movie names
print("----all movies-----")
all_movies = [m.get("title") for m in movies]

print(all_movies)

print()

# display malayalam movie names
print("---malayalam movies----")

mal_movies = [mal.get("title")  for mal in movies if mal.get("language") == "Malayalam"]

print(mal_movies)

print()

# movie with run time > 150
print("---movie with runtime > 150----")

runtime_greater_150 = [mov.get("title") for mov in movies if mov.get("runtime") > 150]

print(runtime_greater_150)

print()

# malayalam movie with runtime > 150
print("---mal movies with runtime > 150----")

mal_movies_150  = [ma.get("title") for ma in movies if ma.get("language")=="Malayalam" and ma.get("runtime") > 150]

print(mal_movies_150)

print()

# display movies with rating > 7.5
print("-----movie with rating > 7.5------")

rating_7 = [rat.get("title") for rat in movies if rat.get("rating")> 7.5]

print(rating_7)

print()

# display tamil movies with rating > 8
print("---movie with rating > 8-----")

rat_8 = [ra.get("title") for ra in movies if ra.get("rating") > 8 and ra.get("language") == "Tamil"]

print(rat_8)

print()

# no of malayalam movies
print("---no of malayalam movies----")

count = len(all_movies)

print(count)
