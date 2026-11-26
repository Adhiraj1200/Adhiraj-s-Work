def function(number):
    total = 0
    for x in number:
        total = total + 1
    return total
number = input("Enter a number:")
value = function(number)
print(value,"digits in number")
