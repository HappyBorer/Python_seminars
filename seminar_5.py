# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# newlst = filter(lambda x: x[0] == 'i', products)
# print(*newlst)

# prices = ['1578.4', '892.4', '354.1', '871.5']
#
# new_list = tuple(map(float, prices))
# print(new_list)

'''
ЗАДАЧА
применить скидку к товарам и округлить до 2 знака
'''
DISCOUNT = 7
prices = ['1578.4', '892.4', '354.1', '871.5']

new_list = list(map(lambda x: round(float(x)*(100 - DISCOUNT)/100, 2), prices))
print(new_list)
