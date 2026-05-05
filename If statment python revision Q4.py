age = int(input("Enter your age:"))
if age <= 12:
    print("The fare is 2 euros")
elif age >= 65:
    travel_card = input("Do yo have a travel card:")
    if travel_card == "yes":
        print("There is no fare")
    else:
        print("The fare is 3 euros")
else:
    print("The fare is 5 euros")
    