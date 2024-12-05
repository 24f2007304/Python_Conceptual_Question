# def total_price_no_loops(fruit_prices: dict, purchases) -> float:
#     '''
#     Compute the total price without loops.
#     '''
#     ...

def total_price_no_loops(fruit_prices: dict, purchases):
  return sum(fruit_prices[fruit] * quantity for fruit, quantity in purchases)

print(total_price_no_loops({"Apple":63,"Banana":104,"Pineappie":62},[("Apple",50),("Banana",10)]))
    