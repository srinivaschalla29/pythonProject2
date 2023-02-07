old_prices=[1,2,3,4,5,7,8]
rs=6
def add_price(no):
    return no+6
new_price1=map(add_price,old_prices)
new_price1=list(map(lambda n:n+rs,old_prices))
print(list(new_price1))