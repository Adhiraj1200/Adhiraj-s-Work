def num_test(number):
    if number > 10:
        return ("Greater than 10")
    elif number < 10:
        return ("Less than 10")
    return number
number = float(input("Enter a number:"))
value = num_test(number)
print(value)