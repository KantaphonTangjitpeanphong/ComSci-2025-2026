items = []
price = []

def getPositiveInteger(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")    
            
rounds = getPositiveInteger("Enter number of items: ")
for i in range(rounds):
    item = input("Enter item name: ")
    items.append(item)
    item_price = getPositiveInteger("Enter item price: ")
    price.append(item_price)
    

print("finding items:")
find = input("Enter item name to find: ")
found = False
for i in range(len(items)):
    if items[i] == find:
        
        print("Item found: ", items[i], "Price: ", price[i])
        found = True
        break
    if not found:
        print("Item not found.")
