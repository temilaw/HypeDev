menu_list = ['matcha latte', 'banana cake', 'tea', 'scones']

stock_dict = {'matcha latte' : 10,
              'banana cake' : 9,
              'tea' : 20,
              'scones' : 15
              }

price_dict = {'matcha latte' : 3.5,
              'banana cake' : 4.0,
              'tea': 2.5,
              'scones' : 4.0
              }

total_stock = 0 # initialise total_stock variable

for item in menu_list:
    item_value = stock_dict[item] * price_dict[item] # iterates through each item in menu, multiplies quantity and price
   
    total_stock += item_value # sums all item values

print("Total stock is worth : ", total_stock)