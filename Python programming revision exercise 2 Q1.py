length = int(input('Enter the length of the rectangle in metres:'))
width = int(input('Enter the width of the rectangle in metres:'))
perimeter = length  * 2 + width * 2
price = int(input('Enter the cost per metre:'))
total_price = perimeter * price
print('The total price is:€',total_price)