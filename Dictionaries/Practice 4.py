# def find_cheapest_fruit(fruit_prices:dict) -> str:
#     '''
#     Find the cheapest fruit from the fruit_prices dict, do not use min function

#     Arguments:
#     fruit_prices: dict - fruit name as key and price as value

#     Return:
#     cheapest_fruit: str - the fruit with the lowest price
#     '''

def find_cheapest_fruit(fruit_prices:dict):
    min = float('inf')  # It is important Value that can help to find the min without useing list values. .
    fruit_Name = ''
    for key in fruit_prices:
        if fruit_prices[key]<min:
             min = fruit_prices[key]
             fruit_Name = key
    return fruit_Name

print(find_cheapest_fruit({"Apple":63,"Banana":104,"Pineappie":62}))


''' With useing the Value of .vlaues() to get all the Values'''

def find_cheapest_fruit_Price(fruit_price:dict):
    Price = fruit_price.values()
    Cheap_Price = min(Price)
    return Cheap_Price

print(find_cheapest_fruit_Price({"Apple":63,"Banana":104,"Pineappie":62}))