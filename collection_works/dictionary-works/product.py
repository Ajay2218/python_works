
product = {
    "code":123,
    "title":"shoes",
    "catagory":"sneakers",
    "brand":"nike"
}

if "stock" not in product:

    product["stock"] = 50

if "price" in product:

    product["price"] += 500

else:

    product["price"] = 2000


if "offer" in product:

    product["offer"] += 300

else:

    product["offer"] = 250

print(product)