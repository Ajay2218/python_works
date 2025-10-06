

shirts = [
  { "id": 1, "title": "Classic White Shirt", "brand": "Allen Solly", "price": 1499, "sizes": ["S", "M", "L", "XL"] },
  { "id": 2, "title": "Slim Fit Denim Shirt", "brand": "Levi's", "price": 2299, "sizes": ["M", "L", "XL"] },
  { "id": 3, "title": "Casual Checked Shirt", "brand": "U.S. Polo Assn.", "price": 1799, "sizes": ["S", "M", "L"] },
  { "id": 4, "title": "Formal Blue Shirt", "brand": "Van Heusen", "price": 1999, "sizes": ["M", "L", "XL", "XXL"] },
  { "id": 5, "title": "Printed Cotton Shirt", "brand": "Flying Machine", "price": 1299, "sizes": ["S", "M", "L"] },
  { "id": 6, "title": "Black Party Shirt", "brand": "Peter England", "price": 1599, "sizes": ["M", "L", "XL"] },
  { "id": 7, "title": "Linen Striped Shirt", "brand": "Raymond", "price": 2499, "sizes": ["S", "M", "L", "XL"] },
  { "id": 8, "title": "Half Sleeve Polo Shirt", "brand": "Tommy Hilfiger", "price": 2699, "sizes": ["M", "L"] },
  { "id": 9, "title": "Checked Flannel Shirt", "brand": "H&M", "price": 1399, "sizes": ["S", "M", "L", "XL"] },
  { "id": 10, "title": "Casual Printed Shirt", "brand": "Zara", "price": 1899, "sizes": ["S", "M", "L", "XL"] }
]

# display all shirt title
print("\t---all shirts----")

all_shirts = [s.get("title") for s in shirts]

print(all_shirts)

print()

# display all shirt sizes
print("\t--all sizes---")

all_sizes = {size for s in shirts for size in s.get("sizes")}

print(all_sizes)

print()

# display shirts whos price > 1500
print("\t----size whose price > 1500----")

shirt_price_1500 = [s.get("title") for s in shirts if s.get("price") > 1500]

print(shirt_price_1500)

print()

# display shirts available in size S
print("\t---shirts with size S-----")

shirts_s = [s.get("title") for s in shirts for size in s.get("sizes") if size == "S"]

print(shirts_s)

print()

# display brand where price > 1500 and size not available in XL
print("\t--display brand where price>1500 and not in XL----")

brand = [b.get("brand") for b in shirts  if b.get("price") > 1500 and "XL" not in b.get("sizes")]

print(brand)

print()

# display costly shirts
print("\t---costly shirt----")

max_prices = max([s.get("price") for s in shirts])

costly_shirt = [s.get("title") for s in shirts if s.get("price") == max_prices]

print(costly_shirt)

print()

# display size along with count of shirt
print("\t---size along with count----")

all_sizess = [size for s in shirts for size in s.get("sizes")]

size_count = {s:all_sizess.count(s) for s in all_sizess}

print(size_count)