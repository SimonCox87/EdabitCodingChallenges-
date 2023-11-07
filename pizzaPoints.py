# Google is launching a network of autonomous pizza delivery drones and wants you to create a flexible rewards system (Pizza Points™) 
# that can be tweaked in the future. The rules are simple: if a customer has made at least N orders of at least Y price, they get a 
# FREE pizza!

# Create a function that takes a dictionary of customers, a minimum number of orders and a minimum order price. Return a list of 
# customers that are eligible for a free pizza.

# Examples

# customers = {
#   "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
#   "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
# }

#   pizza_points(customers, 5, 20) ➞ ["Spider-Man"]

#   pizza_points(customers, 3, 10) ➞ ["Batman", "Spider-Man"]

#   pizza_points(customers, 5, 100) ➞ []

# Notes

# ⚠️Sort the returned array of customer names in alphabetical order.

customers = {
  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
}

def pizza_points(customers, min_orders, min_price):
	return sorted([i for i in customers if sum(map(lambda x: x >= min_price, customers[i])) >= min_orders])

print(pizza_points(customers, 5, 20)) # ➞ ["Spider-Man"]
print(pizza_points(customers, 3, 10)) # ➞ ["Batman", "Spider-Man"]
print(pizza_points(customers, 5, 100)) # ➞ []

# def pizza_points(customers, min_orders, min_price):
# 	return sorted([k for k, v in customers.items() if sum(1 for i in v if i >= min_price) >= min_orders])

def pizza_points(customers, min_orders, min_price):
	return sorted([customer for customer,orders in customers.items() if len([price for price in orders if price >= min_price]) >= min_orders])