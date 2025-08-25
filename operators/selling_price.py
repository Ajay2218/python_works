

product_price = int(input("enter the purchase amount = "))

profit = int(input("enter the profit percentage value = "))

profit_cal  = (profit/100)*product_price

selling_price = product_price + profit_cal

print("the selling price will be",selling_price )