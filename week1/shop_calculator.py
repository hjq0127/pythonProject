# display menu
# get total
# get choice
# while choice != quit option
# total intms < 0
# print Invalid number of items!
# for total in range
#         get items input
#         display invalid input error message
#         get final total
TOTAL=0
total_items = int(input("Number of items"))
if total_items < 0:
  print("Invalid number of items!Please enter again")
  total_items = int(input("Number of items"))
for total_items in range(1, total_items+1, 1):
    items_price = float(input("Price of items:"))
    TOTAL = TOTAL+items_price
print("Total price for", total_items, "items is $", TOTAL)








