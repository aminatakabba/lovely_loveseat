toppings = ['pepperoni' ,'pineapple' ,'cheese' ,'sausage' ,'olives' ,'anchovies' ,'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizzas!")
pizzas = list(zip(toppings, prices))
print(pizzas)
pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizza = cheapest_pizza[-1]
three_cheapest = cheapest_pizza[:3]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)