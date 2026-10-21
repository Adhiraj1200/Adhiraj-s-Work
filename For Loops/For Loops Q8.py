total = 0
for x in range(5):
    number = float(input("Enter a number:"))
    include = str(input("Do you want numbers included(yes/no):"))
    if include == "yes":
       total = total + number
print(total)
   
   