number_people = int(input("Enter how many people do you want to invite:"))
if number_people < 10:
    for x in range(number_people):
        people = str(input("Enter the people's names(One by one):"))
        print(people,"has been invited")
elif number_people >= 10:
    print("Too high")
    
    
       
