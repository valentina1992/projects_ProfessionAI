########################################################################################################################
# Vegan product store software

# This project consists of creating software for managing a vegan product shop.
# The software must have the following features:
# 1) Register new products, with name, quantity, selling price and purchase price.
# 2) List all the products present.
# 3) Record the sales you make.
# 4) Show gross and net profits.
# 5) Show a help menu with all available commands.
########################################################################################################################

# -------------------------------------------------------------------------------
# Name:        Vegan product store software
# Date:        16/05/2024
# Final
# -------------------------------------------------------------------------------

class VeganProducts:
    """
    Class for managing a vegan product shop.
    """

    def __init__(self):
        self.products = {}  # Dictionary for storing products {product name: [quantity, purchase price, sale price]}
        self.sales = []  # List for recording sales [product name, quantity sold]

    def add_product(self, name, quantity, purchase_price, selling_price):
        """
        Adds a new product to the store.

        Parameters:
        name (str): The name of the product.
        quantity (int): The quantity of the product.
        purchase_price (float): The purchase price of the product.
        selling_price (float): The selling price of the product.

        Raises:
        ValueError: If the quantity, purchase price or selling price is negative.
        """

        if (quantity < 0):
            raise ValueError("The quantity must be positive.")
        if (purchase_price < 0):
            raise ValueError("The purchase price and selling price must be positive.")
        if (selling_price < 0):
            raise ValueError("The selling price must be positive.")
        if (quantity < 0 or purchase_price < 0 or selling_price < 0):
            raise ValueError("The quantity, purchase price and selling price must be positive.")


        #Se inserisci di nuovo un prodotto che esiste aggiorna la quantità
        #if name in self.products:
         #   self.products[name][0] += quantity
        #else:
         #   self.products[name] = [quantity, purchase_price, selling_price]

        if name not in self.products:
            purchase_price = float(input("Enter the purchase price: "))
            selling_price = float(input("Enter the sales price: "))
            self.products[name] = [quantity, purchase_price, selling_price]
        else:
            #If you enter a product that already exists, only update the quantity
            print(f'The product {name} is already present in the list')
            self.products[name][0] += quantity
    def list_products(self):
        """
        Shows all products in the shop.
        """
        print("Products available in the shop:")
        for name, details in self.products.items():
            if self.products[name][0] > 0:
                print(f"{name}  {details[0]}    €{details[2]}")

    def register_sale(self):
        """
        Record a product sale.

        Parameters:
        name (str): The name of the product sold.
        quantity (int): The quantity sold.

        Raises:
        ValueError: If the quantity is negative or if the product does not exist in the store.
        """

        response = 'Y'
        vendita = []
        while response.upper() == 'Y':
            name = str(input("Enter the product name: "))
            quantity = int(input("Enter the available quantity: "))
            if name in self.products:
                if self.products[name][0] >= quantity:
                    self.products[name][0] -= quantity
                    vendita.append([name, quantity])
                else:
                    print(f'Quantità eccessiva, disponibile {self.products[name][0]}')
            else:
                print(f'{name} : prodotto non disponibile.')
            response = str(input("Do you want to add a new product to sell? \n Press Y or N:   "))

        print('VENDITA REGISTRATA')
        total_price = 0
        for name, quantity in vendita:
            total_price += self.products[name][2] * quantity
            print(f"{quantity} X {name} : € {self.products[name][2]}")
        print(f"Totale € {total_price}")
        self.sales += vendita

    def show_profits(self):
        """
        Shows the store's gross and net profits.
        """

        gross_profits = 0
        net_profits = 0
        for sale in self.sales:
            selling_price = self.products[sale[0]][2]
            costo = self.products[sale[0]][1]
            gross_profits += selling_price * sale[1]
            net_profits += selling_price * sale[1] - costo * sale[1]
        print(f"Gross profits: {gross_profits}")
        print(f"Net profits:: {net_profits}")

    def show_help_menu(self):
        """
        Shows the help menu with all available commands.
        """

        print("Available commands:")
        print("1. Add product")
        print("2. Product list")
        print("3. Record sale")
        print("4. Help")
        print("5. Profits")
        print("0. Close")

    def exit(self):
        """
        Exits the program.
        """

        print("Exiting the program.")
        exit()


def main():
    """
    Main function for program execution.
    """

    store = VeganProducts()
    store.show_help_menu()
    while True:
        choice = input("Enter the number corresponding to the desired action: ")
        if choice == "1":
            try:
                name = input("Enter the product name: ")
                quantity = int(input("Enter the available quantity: "))
                purchase_price = 0
                selling_price = 0
                store.add_product(name, quantity, purchase_price, selling_price)
            except ValueError as e:
                print(e)
        elif choice == "2":
            store.list_products()
        elif choice == "3":
            store.register_sale()
        elif choice == "4":
            store.show_help_menu()
        elif choice == "5":
            store.show_profits()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

