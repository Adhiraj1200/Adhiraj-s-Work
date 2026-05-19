print ("a_notebook = 1.00")
print("a_pen = 2.50")
print("a_mug = 6.00")
print("a_keyring = 1.50")
item_1 = float(input("Enter the cost of a item: "))
item_2 = float(input("Enter the cost of second item: "))
item_3 = float(input("Enter the cost of third item: "))
total_cost = item_1 + item_2 + item_3
print("This is the total cost of the items:",total_cost)
vat = (total_cost / 100) * 20
vat_1 = total_cost - vat
print("This is the VAT of the items:",vat_1)
discount = str(input("Do you have a discount code?:"))
discount_price = vat_1 / 100 * 15
final_cost = vat_1 - discount_price
if discount == "yes":
   print("The final cost is",final_cost)






