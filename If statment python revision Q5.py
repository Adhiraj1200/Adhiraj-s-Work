colour = str(input("Enter a colour of an item:"))
if colour == "red":
    fruit = input("Is it a fruit:")
    if fruit == "yes":
        print("It could be an Apple or a Tomato")
    if fruit == "no":
        print("It could be a Rose")
elif colour == "yellow":
     fruit = input("Is it a fruit:")
     if fruit == "yes":
        print("It could be a Banana")
     if fruit == "no":
        print("It could be Corn or a Marigold")
else:
    print("I can not assist in identifing the item")
    