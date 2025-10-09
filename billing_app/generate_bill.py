

items=[
   {"id":1,"code":"uda","name":"uzhunuvada","price":15},
   {"id":2,"code":"pda","name":"parippuvada","price":15},
   {"id":3,"code":"bfry","name":"bananafry","price":18},
   {"id":4,"code":"sma","name":"samoosa","price":15},
   {"id":5,"code":"cbn","name":"creambun","price":20},
   {"id":6,"code":"tea","name":"tea","price":12},
   {"id":7,"code":"cfe","name":"coffe","price":20},
   {"id":8,"code":"lme","name":"limejuice","price":20}
]

order_items = []

while(True):

    item_code = input("enter the item code :")

    qty = int(input("enter the quantity : "))

    item = [ it for it in items if it.get("code") == item_code][0]

    order_item = {"name":item.get("name"),"qty":qty,"total":item.get("price")*qty}

    order_items.append(order_item)

    response = input("do u want to continue press y for yes n for no :")

    if response == "n":

        break


print(order_items)

file_path = "C:\\Users\\AJAY\\OneDrive\\Desktop\\development_journey\\python_works\\billing_app\\bill.txt"

fw = open(file_path,"w")

fw.write("name\tqty\tprice"+"\n")

for item in order_items:

    fw.write(item.get("name")+"\t"+str(item.get("qty"))+"\t"+str(item.get("total"))+"\n")
