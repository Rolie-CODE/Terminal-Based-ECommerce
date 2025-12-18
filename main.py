# Let us build a terminal based e cmmerce to help show our python skills
print("Welcome To SertTek Enterprise")
print("1. Add Products")
print("2. View Products")
print("3. Add to cart")
print("4. View Cart")
print("5. Checkout")
print("6. Exit")

products = {"basketball": 50, 
            "football": 40, 
            "tennis Ball": 30
}

cart = {}

while True:
    option  = input("")
    if option == "6":
        print("Thank you for shopping with us!!!!!" \
        "We hope to see you again")
        break

    if option == "1":
        product_name = input("Enter product name: ").lower()
        product_price = float(input("Enter product price: "))
        products[product_name] = product_price
        print(f"{product_name} added successfully")
        continue

    if option == "2":
        print("Available Products:")
        for product, price in products.items():
            print(f"{product}: ${price}")
        print("Welcome To SertTek Enterprise")
        print("1. Add Products")
        print("2. View Products")
        print("3. Add to cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        continue


    if option == "3":
        product_to_add = input("Enter product name to add to cart: ").lower( )
        if product_to_add in products:
            cart[product_to_add] = products[product_to_add]
            print(f"{product_to_add} added to cart")
        else:
            print(f"{product_to_add} is not available")
        continue

    if option == "4":
        print("Cart Items:")
        for item, price in cart.items():
            print(f"{item}: ${price}")
        continue

    if option == "5":
        total = sum(cart.values())
        print(f"Total amount: ${total}")
        print("Checkout successful! Thank you for shopping with us.")
        cart.clear()
        continue

