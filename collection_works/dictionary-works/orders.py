

orders = ["tea","coffee","tea","tea","coffee","coldcoffee","cappiccino","coldcoffee"]

orders_count = {}

for o in orders:

    if o in orders_count:

        orders_count[o] += 1
    
    else:

        orders_count[o]=1

print(orders_count)
