# listItems = []

# size = int(input("Enter the size of the list: "))
# #n = int(input("Enter the list items now: "))

# for n in range (size):
#     item = int(input(f"Enter the item {n+1}th: "))
#     listItems.append(item)

# print(listItems)
# large = listItems[0]
# small = listItems[0]
# for num in listItems:
#     if num>large:
#         large = num
#     if num<small:
#         small = num

# print("Largest number among the list is:",large)
# print("Smaller number among the list is: ",small)

list_items = [10,80,7,96,100,78]

small = list_items[0]
large = list_items[0]

for i in list_items:
    if i > large:
        large = i
    if i<small:
        small = i

print("large item is : ",large)
print("small item is : ",small)

