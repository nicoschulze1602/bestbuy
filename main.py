from store import Store
from products import Product

def print_store_menu():
    print('\n   Store Menu   ')
    print('   ----------   ')
    print('1. List all products in store')
    print('2. Show total amount in store')
    print('3. Make an order')
    print('4. Quit')


def start(store_obj):
    while True:
        print_store_menu()
        choice = input('Please choose a number: ')
        if choice == '1':
            print()
            for product in store_obj.get_all_products():
                print(product.show())

        elif choice == '2':
            total = store_obj.get_total_quantity()
            print(f"\nTotal quantity in store: {total}")

        elif choice == '3':
            shopping_list = []
            active_products = store_obj.get_all_products()

            if not active_products:
                print("\nNo active products available.")
                continue

            print("\nAvailable products:")
            for idx, product in enumerate(active_products, start=1):
                print(f"{idx}. {product.show()}")

            print("\nWhen you want to finish order, enter empty text.")
            while True:
                product_number = input("Which product # do you want? ").strip()
                if not product_number:
                    break
                if not product_number.isdigit() or not (1 <= int(product_number) <= len(active_products)):
                    print("Invalid product number.")
                    continue

                product = active_products[int(product_number) - 1]

                quantity_str = input("What amount do you want? ").strip()
                if not quantity_str.isdigit():
                    print("Invalid quantity.")
                    continue

                quantity = int(quantity_str)
                if quantity > product.get_quantity():
                    print(f"Not enough in stock. Only {product.get_quantity()} available.")
                    continue

                shopping_list.append((product, quantity))
                print("Product added to shopping list.")

            try:
                total_price = store_obj.order(shopping_list)
                print(f"\nOrder successful! Total price: {total_price:.2f} $")
            except ValueError as e:
                print(f"Order failed: {e}")

        elif choice == '4':
            print('Bye  (•◡•) /')
            break

        else:
            print("Invalid choice. Please select a valid option.")


def main():
    # setup initial stock of inventory
    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                     Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                     Product("Google Pixel 7", price=500, quantity=250)
                   ]
    best_buy = Store(product_list)
    start(best_buy)

if __name__ == '__main__':
    main()