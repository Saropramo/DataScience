print("\n\t\t Cafe stock worth")
print("\t\t------------------")
menu = ["latte", "cappuccino", "flatwhite", "flatblack"]
# Dictionary for stock items
stock = {"latte": 100,
         "cappuccino" : 75,
         "flatwhite" : 50,
         "flatblack" : 75}
# Dictionary for item price
price = {"latte": 7,
         "cappuccino" : 10,
         "flatwhite" : 10,
         "flatblack" : 5}
total_stock = 0
# looping through items and calculates the individual stock value and total stock worth
for items in menu:
    item_value = stock[items] * price[items]
    print(f"\nStock value of {items} is £ {item_value}")
    total_stock = total_stock + item_value
# Displays the total stock worth in the cafe
print(f"\nTotal stock worth in cafe is £ {total_stock} \n")    
