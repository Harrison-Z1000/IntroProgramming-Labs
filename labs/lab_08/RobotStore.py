# CMPT 120 Intro to Programming
# Lab #8 - Working with Objects
# Author: Harrison Zheng
# Date: 2019-11-17


from product import Product

# Instantiates each product
products = [Product("Ultrasonic range finder", 2.50, 4),
            Product("Servo motor", 14.99, 10),
            Product("Servo controller", 44.95, 5),
            Product("Microcontroller Board", 34.95, 7),
            Product("Laser range finder", 149.99, 2),
            Product("Lithium polymer battery", 8.99, 8)]


def print_stock():
    # Prints the name and price of each product that is in stock
    print("\nAvailable Products")
    print("------------------")
    for i in range(0, len(products)):
        if products[i].quantity > 0:
            # Begins listing products with 1st not 0th
            print(i + 1, ") ", products[i].name, "$", products[i].price)
    print()


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break

        prod_id = int(vals[0]) - 1
        count = int(vals[1])

        # Checks that the product the user wants is in stock
        if Product.inStock(products[prod_id], count):
            # Checks that the user has enough money to make the purchase
            if cash >= products[prod_id].price:
                Product.removeFromStock(products[prod_id], count)
                cash -= Product.totalCost(products[prod_id], count)
                print("You purchased", count, products[prod_id].name + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prod_id].name)


main()
