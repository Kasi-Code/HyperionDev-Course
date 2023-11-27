"""
# num_list = ['1', '5', '8', '14', '25', '31'] 
# new_num_list_ints = [int(element) for element in num_list]

# by_two_num_list = [x * 2 for x in new_num_list_ints]

# print(new_num_list_ints, by_two_num_list)

Practical Task

Follow these steps:

● Imagine you are running a cafe. Create a new Python file in your folder called cafe.py.

● Create a list called menu, which should contain at least four items sold in the cafe.

● Next, create a dictionary called stock, which should contain the stock value for each item on your menu.

● Create another dictionary called price, which should contain the prices for each item on your menu.

● Next, calculate the total_stock worth in the cafe. You will need to remember to loop through the appropriate dictionaries and lists to do this.

Tip: When you loop through the menu list, the ‘items’ can be set as keys to access the corresponding ‘stock’ and ‘price’ values. Each ‘item_value’ is calculated by multiplying the stock value by the price value. For example: item_value = (stock[items] * price[items])

● Finally, print out the result of your calculation.

"""

#  Variable (list) of relevants. 

menu = ["coffee", "tea", "latte", "hot-chocolate"]
stock_value = [23, 55, 5, 13]
price_value = [5.5, 2.5, 6, 12.5]

# The comprehension syntaxes will create dictionaries for the (stock) and (price).
# It'll use the (menu) list as the (key), and assign the (value) from the stock and price list.
# The (for) loop will iterate through the stock and price dictionaries for its values.
# Then, it'll add the total values for each dictionary.
# Fianlly, it'll calculate the grand total of the stock values. 

stock = {k:v for k, v in zip(menu, stock_value)}
price = {k:v for k, v in zip(menu, price_value)}

value = 0
total_stock = 0
total_price = 0

for (k,v), (k2,v2) in zip(stock.items(), price.items()):

    total_stock += v
    total_price += v2

    value = total_price * total_stock

    message = f"\nYour Cafe total stock value is £{value}!\n"

print(message)