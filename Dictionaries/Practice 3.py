# def total_price(fruit_prices: dict, purchases) -> float:
#     '''
#     Compute the fruit prices give the quantity of each fruit. Do not use the sum function.

#     Arguments:
#     fruit_prices: dict - fruit name as key and price as value
#     purchases: list[tuple] - as list of tuples of (fruit, quantity)

#     Return:
#     total_price: float
#     '''
#     ...
# sum = None
# is_equal(
# total_price(
# {'Apple':2.0,'Banana':3.0,'Orange':4.0,
# 'Grapes':3.0,'Papaya':5.0},
# [("Apple",3),("Orange",5),("Grapes",4)]
# ),
# 38.0
# )

def total_price(fruit_prices: dict, purchases):
    Total = 0
    for element in purchases:
        Total += element[1]*fruit_prices[element[0]] 
    return Total

print(total_price({"Apple":140,"Orange":75,"Pineapple":25,},[("Apple",5),("Pineapple",3)]))
        