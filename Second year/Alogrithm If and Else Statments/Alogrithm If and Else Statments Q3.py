monthly_sales = float(input("Enter you monthly sales:"))
if monthly_sales > 40000:
   commission_15 = (monthly_sales / 100) * 15    
   print("Your commission for the month is",commission_15)
else:
    commission_5 = (monthly_sales / 100) * 5
    print("Your commission for the month is",commission_5)