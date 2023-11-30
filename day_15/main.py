from data import menu, resources
from utils import check_resources

coins = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

while True:
    choice = (
        input("\tWhat would you like? (espresso/latte/cappuccino): ").strip().lower()
    )

    match choice:
        case "report":
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${round(coins, 2)}")
        case "off":
            break
        case _:
            if choice in ("espresso", "latte", "cappuccino"):
                if check_resources(water, milk, coffee, drink=choice):
                    print("Please insert coins.")
                    quarters = input("How many quarters?: ")
                    dimes = input("How many dimes?: ")
                    nickles = input("How many nickles?: ")
                    pennies = input("How many pennies?: ")

                    if not all(
                        map(
                            lambda x: x.isdigit(),
                            [quarters, dimes, nickles, pennies],
                        )
                    ):
                        print("Invalid input. Money refunded")
                        continue

                    quarters = int(quarters)
                    dimes = int(dimes)
                    nickles = int(nickles)
                    pennies = int(pennies)

                    total = (
                        quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
                    )
                    if total < menu[choice]["cost"]:
                        print("Sorry that's not enough money. Money refunded.")
                    else:
                        coins += menu[choice]["cost"]
                        water -= menu[choice]["ingredients"]["water"]
                        milk -= menu[choice]["ingredients"].get("milk", 0)
                        coffee -= menu[choice]["ingredients"]["coffee"]
                        print(
                            f"Here is ${round(total - menu[choice]['cost'], 2)} in change."
                        )
                        print(f"Here is your {choice} ☕. Enjoy!")
            else:
                print("Invalid choice.")
