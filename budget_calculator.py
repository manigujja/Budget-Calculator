def welcome_greet():
    print("Welcome to budget Calculator!")
    print("This tool will help you calculate your remaining budget and discounts.")
    print("=" * 50)


def budget_status(budget, spent):
    remaining = budget - spent
    percentage = (remaining / budget) * 100

    print(f"Budget is : {budget}")
    print(f"Spent is : {spent}")
    print(f"Remaining is : {remaining}")
    print(f"Remaining percentage is : {percentage:.2f}%")

    return remaining


def discount_calculator(price, discount_percentage):
    discount_amount = (discount_percentage / 100) * price
    final_price = price - discount_amount

    print(f"Original price: {price}")
    print(f"Discount: {discount_percentage}%")
    print(f"Final price: {final_price:.2f}")

    return final_price


def can_buy(item_price, remaining):
    if item_price > 0 and item_price <= remaining:
        return True
    else:
        return False


def main():
    welcome_greet()

    budget = float(input("Enter your total budget: "))

    if budget <= 0:
        print("Budget must be greater than zero.")
        return

    total_spent = 0
    purchases_count = 0
    keep_going = True

    while keep_going:
        remaining = budget_status(budget, total_spent)

        print("\n" + "=" * 40)
        print("MENU:")
        print("1. Add a purchase")
        print("2. Buy multiple items")
        print("3. Calculate discount")
        print("4. Exit")
        print("=" * 40)

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print("\n-------- Add a purchase --------")

            item_name = input("Enter the name of the item: ")
            item_price = float(input("Enter the value of the purchase: "))

            if item_price <= 0:
                print("Price must be greater than zero.")
                continue

            if can_buy(item_price, remaining):
                confirmation = input(
                    f"Buy {item_name} for ${item_price:.2f}? (yes/no): "
                )

                if confirmation.lower() == "yes":
                    total_spent += item_price
                    purchases_count += 1
                    print(f"{item_name} confirmed the purchase.")
                else:
                    print(f"{item_name} purchase cancelled.")

            else:
                print(f"Cannot buy {item_name}. Not enough budget remaining.")
                print(
                    f"You are short of ${item_price - remaining:.2f} "
                    f"to buy {item_name}."
                )

        elif choice == 2:
            # to add multiple items
            print("\n-------- Multiple items --------")
            print("Enter items (or 'done' to finish):")

            item_count = 0
            cart_total = 0

            while True:
                item = input(f"\nItem #{item_count + 1} name (or 'done'): ")

                if item.lower() == "done":
                    break

                if item == "":
                    print("Item name cannot be empty. Please try again.")
                    continue

                item_price = float(input(f"Enter the price of {item}: "))

                if item_price <= 0:
                    print("Price must be greater than zero. Please try again.")
                    continue

                cart_total += item_price
                item_count += 1

                print(f"✓ Added {item}")
                print(f"\nCart: {item_count} items, Total: ${cart_total:.2f}")

            if item_count == 0:
                print("No items added to cart")

            else:
                print(
                    f"\nCart ready: {item_count} items, "
                    f"Total: ${cart_total:.2f}"
                )

                affordable = cart_total <= remaining
                reasonable = cart_total <= remaining * 0.7

                if affordable:
                    confirm = input("Proceed with purchase? (yes/no): ")

                    if confirm.lower() == "yes":
                        total_spent += cart_total
                        purchases_count += item_count
                        print("✓ Purchase complete!")
                    else:
                        print("Purchase cancelled.")

                else:
                    print("Not enough budget for this purchase.")
                    print(
                        f"You are short of "
                        f"${cart_total - remaining:.2f} "
                        f"to complete the purchase."
                    )

                    if not reasonable:
                        print(
                            "This purchase is also not reasonable "
                            "based on your remaining budget."
                        )

        elif choice == 3:
            print("\n-------- Calculate discount --------")

            price = float(input("Enter the original price: "))
            discount_percentage = float(
                input("Enter the discount percentage: ")
            )

            discount_calculator(price, discount_percentage)

        elif choice == 4:
            print("Exiting")
            keep_going = False

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    print("=" * 40)
    print("Final Summary:")
    print(f"Total Budget: ${budget:.2f}")
    print(f"Total Spent: ${total_spent:.2f}")
    print(f"Remaining Budget: ${budget - total_spent:.2f}")
    print(f"Total Purchases: {purchases_count}")
    print("=" * 40)


if __name__ == "__main__":
    main()
