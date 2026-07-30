class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def get_price_category(self, price_limit):
        if self.price >= price_limit:
            return "Expensive"
        else:
            return "Affordable"

    def display(self, price_limit):
        print("-" * 40)
        print("Product ID   :", self.product_id)
        print("Product Name :", self.product_name)
        print("Price        : ₹", format(self.price, ".2f"))
        print("Category     :", self.get_price_category(price_limit))


class Inventory:
    def __init__(self, price_limit):
        self.products = []
        self.price_limit = price_limit

    def product_exists(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return True
        return False

    def add_product(self):
        product_id = input("Enter Product ID: ").strip()

        if self.product_exists(product_id):
            print("Product ID already exists.\n")
            return

        product_name = input("Enter Product Name: ").strip()

        try:
            price = float(input("Enter Product Price: ₹"))

            if price < 0:
                print("Price cannot be negative.\n")
                return

        except ValueError:
            print("Please enter a valid price.\n")
            return

        product = Product(product_id, product_name, price)
        self.products.append(product)

        print("Product added successfully!\n")

    def display_all_products(self):
        if not self.products:
            print("No product records found.\n")
            return

        print("\n" + "=" * 40)
        print("PRODUCT INVENTORY")
        print("=" * 40)
        print(
            "Products costing ₹",
            format(self.price_limit, ".2f"),
            "or more are categorized as Expensive."
        )

        for product in self.products:
            product.display(self.price_limit)

        print("-" * 40)
        print()

    def search_product(self):
        product_id = input("Enter Product ID to search: ").strip()

        for product in self.products:
            if product.product_id == product_id:
                print("\nProduct found:")
                product.display(self.price_limit)
                print()
                return

        print("Product not found.\n")


def main():
    try:
        price_limit = float(
            input("Enter the minimum price for an Expensive product: ₹")
        )

        if price_limit < 0:
            print("Price limit cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid price limit.")
        return

    inventory = Inventory(price_limit)

    while True:
        print("===== Product Inventory System =====")
        print("1. Add Product")
        print("2. Display All Products")
        print("3. Search Product")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            inventory.add_product()

        elif choice == "2":
            inventory.display_all_products()

        elif choice == "3":
            inventory.search_product()

        elif choice == "4":
            print("Exiting Product Inventory System.")
            break

        else:
            print("Invalid choice. Please try again.\n")


main()
