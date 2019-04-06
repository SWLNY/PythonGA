"""
This program operates a self checkout line at a CVS store.
The customer is prompted for the name and price of each item selected for purchase.
When all items have been processed, the customer enters 'exit'.
"""
#
#  Initialize all variables
#
groceries = []  # each entry is the name of the item purchased
grocery_prices = []  # each entry is the price of an item
balance = 0.0  # amount of money spent so far
tax = .0875

#
#  Accept and save the name of each item and its price. As each item is added,
#  increment balance by the price of the current item.

while True:
    gitem = input("Enter name of  item or exit ")
    if gitem == "exit":
        break
    else:
        groceries.append(gitem)
    grocery_prices.append(float(input("Enter price of item ")))
    balance += grocery_prices[-1]

coupon_value = float(input("Enter value of coupon or 0.00 "))
adjusted_balance = balance - coupon_value
tax_amount = adjusted_balance * tax
total_balance = tax_amount + adjusted_balance

#
#  Format and print a receipt
#
print("\nCVS Receipt\n")
for i in range(len(groceries)):
    print(groceries[i]+"\t$"+"{:8.2f}".format(grocery_prices[i]))
print("\nAmount spent\t$"+"{:8.2f}".format(balance))
print("Coupon value\t$"+"{:8.2f}".format(coupon_value))
print("Tax\t$"+"{:8.2f}".format(tax_amount))
print("\nAmount due\t$"+"{:8.2f}".format(total_balance))







