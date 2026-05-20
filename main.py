products = []

def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))

    product = {
        "id": pid,
        "name": name,
        "qty": qty
    }

    products.append(product)
    print("Product Added Successfully")


def view_products():
    if not products:
        print("No products available")
    else:
        for p in products:
            print(p)


def search_product():
    pid = input("Enter Product ID to Search: ")

    for p in products:
        if p["id"] == pid:
            print(p)
            return

    print("Product not found")


def update_quantity():
    pid = input("Enter Product ID: ")

    for p in products:
        if p["id"] == pid:
            new_qty = int(input("Enter New Quantity: "))
            p["qty"] = new_qty
            print("Quantity Updated")
            return

    print("Product not found")


def delete_product():
    pid = input("Enter Product ID: ")

    for p in products:
        if p["id"] == pid:
            products.remove(p)
            print("Product Deleted")
            return

    print("Product not found")


def low_stock_alert():
    print("Low Stock Products")

    for p in products:
        if p["qty"] < 5:
            print(p)


while True:
    print("\n--- Inventory Management ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Delete Product")
    print("6. Low Stock Alert")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_quantity()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        low_stock_alert()

    elif choice == "7":
        break

    else:
        print("Invalid Choice")