inventory = []

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    inventory.append(item)
    print("Item added successfully.")

def update_item():
    name = input("Enter the name of the item to update: ")

    for item in inventory:
        if item["name"] == name:
            item["price"] = float(input("Enter new price: "))
            item["quantity"] = int(input("Enter new quantity: "))
            item["category"] = input("Enter new category: ")
            print("Item updated successfully.")
            return

    print("Item not found.")

def view_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for item in inventory:
            print("Name:", item["name"])
            print("Price:", item["price"])
            print("Quantity:", item["quantity"])
            print("Category:", item["category"])
            print("---------------------")

def remove_item():
    name = input("Enter the name of the item to remove: ")

    for item in inventory:
        if item["name"] == name:
            inventory.remove(item)
            print("Item removed successfully.")
            return

    print("Item not found.")

def search_by_category():
    category = input("Enter category to search: ")
    found = False

    for item in inventory:
        if item["category"] == category:
            print("Name:", item["name"])
            print("Price:", item["price"])
            print("Quantity:", item["quantity"])
            print("Category:", item["category"])
            print("---------------------")
            found = True

    if not found:
        print("No items found in that category.")

while True:
    print("\n--- Market Inventory System ---")
    print("1. Add Item")
    print("2. Update Item")
    print("3. View Inventory")
    print("4. Remove Item")
    print("5. Search by Category")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_item()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        search_by_category()
    elif choice == "6":
        print("Goodbye.")
        break
    else:
        print("Invalid choice.")
