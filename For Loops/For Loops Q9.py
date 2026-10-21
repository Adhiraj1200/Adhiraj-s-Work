direction = str(input("Enter the direction you want to count(up/down):"))
if direction == "up":   
    number = int(input("Enter a number:"))
    for x in range(1,number+1):        
        print(x)
elif direction == "down":
    number = int(input("Enter a number below 20:"))
    for x in range(20,number-1,-1):        
        print(x)
else:
    print("I don't understand")
    
