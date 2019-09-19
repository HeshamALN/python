
items=list()
while(1 == 1):
    item = input('please enter the Item (enter "done" when finished):')
    if(str(item) != "done"):
        price = input('please enter the price: ')
        quantity=input("please enter the quantity: ")
        items.append({"name":item, "price":price, "quantity":quantity})
    else:
        break

total=0
print("\n\n-------------------------------")
print("            Receipt            ")
print("-------------------------------")
#print(items) #remove
print("Quantity---Name---Price")
for item in items:
    print(item["quantity"],"  ",item["name"],"  ",str("{0:.3f}".format(round(float(item["price"]),3)))+"KD")
    total =total + round(float(item["price"]),2)

print("-------------------------------")
print('Total Price:',str("{0:.3f}".format(total))+"KD");
print("-------------------------------")

