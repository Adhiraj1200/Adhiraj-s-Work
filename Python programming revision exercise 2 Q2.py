sale_price = float(input('Enter the sale price:'))
percent_1 =  sale_price / 100 * 8 + sale_price
percent_2 =  sale_price / 100 * 18 + sale_price
sale_region = str(input('Enter the sale region: national or foreign:'))
if sale_region == 'national':
    print('The price of the item is',percent_1)
elif sale_region == 'foreign':
    print('The price of the item is',percent_2)
else:
    print('Check spelling or type again!!!')