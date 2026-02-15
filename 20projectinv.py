inventory = []

def find_item_index(name):
    target = name.strip().lower()
    for i, item in enumerate(inventory):
        if item["name"].strip().lower() == target:
            return i
    return -1

def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number.")

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid whole number.")

def add_item():
    name = read_non_empty("Enter item name: ")

    if find_item_index(name) != -1:
        print("Item already exists.")
        return

    price = read_float("Enter price: ")
    while price < 0:
        print("Price cannot be negative.")
        price = read_float("Enter price: ")

    quantity = read_int("Enter quantity: ")
    while quantity < 0:
        print("Quantity cannot be negative.")
        quantity = read_int("Enter quantity: ")

    category = read_non_empty("Enter category: ")

    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    })

    print("Item added.")

def update_item():
    name = read_non_empty("Enter item name to update: ")
    idx = find_item_index(name)

    if idx == -1:
        print("Item not found.")
        return

    item = inventory[idx]

    new_price = input(f"New price (current {item['price']}): ").strip()
    if new_price:
        try:
            price_val = float(new_price)
            if price_val >= 0:
                item["price"] = price_val
        except ValueError:
            print("Invalid price.")

    new_qty = input(f"New quantity (current {item['quantity']}): ").strip()
    if new_qty:
        try:
            qty_val = int(new_qty)
            if qty_val >= 0:
                item["quantity"] = qty_val
        except ValueError:
            print("Invalid quantity.")

    new_cat = input(f"New category (current {item['category']}): ").strip()
    if new_cat:
        item["category"] = new_cat

    print("Item updated.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    for item in inventory:
        print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")

def remove_item():
    name = read_non_empty("Enter item name to remove: ")
    idx = find_item_index(name)

    if idx == -1:
        print("Item not found.")
        return

    inventory.pop(idx)
    print("Item removed.")

def search_by_category():
    category = read_non_empty("Enter category to search: ").strip().lower()

    found = False
    for item in inventory:
        if item["category"].strip().lower() == category:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
            found = True

    if not found:
        print("No items found in that category.")

def main():
    while True:
        print("\n1) Add Item")
        print("2) Update Item")
        print("3) View Inventory")
        print("4) Remove Item")
        print("5) Search by Category")
        print("6) Exit")

        choice = input("Choose an option: ").strip()

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
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
