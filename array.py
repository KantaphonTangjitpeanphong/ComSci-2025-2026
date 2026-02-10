#array
list1 = []
n = None
while True:
    n1 = input("enter number")
    try:
        num = int(n1)
    except ValueError:
        print("Invalid number, try again")
    if num > 25:
        print("number must be less than 25")
        continue
    break


for i in range(num):
    temp = input("enter username")
    list1.append(temp)
    print(list1)
print("List complete")

print(f"list of usernames: {list1}")

#linear seach
def search():
    found = False
    search = input("enter username to search: ")
    for x in range(len(list1)):
        if list1[x] == search:
            print(f"{search} found at position {x}")
            found = True
            break

    if not found:
        print(f"{search} not found in the list")

# Bubble Sort
def sort():
    for i in range(len(list1)-1):
        for j in range(len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]

    print(f"sorted list: {list1}")

print("1. Search")
print("2. Sort")
print("3. Exit")

choice =int(input("Enter your choice: "))




if choice == 1:
    search()
elif choice == 2:
    sort()
elif choice == 3:
    print("Exiting...")
else:
    print("Invalid choice")