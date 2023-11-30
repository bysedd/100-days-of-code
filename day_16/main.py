from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    choice = input(f"What would you like? ({menu.get_items()}): ").strip().lower()

    match choice:
        case "report":
            coffee_maker.report()
            money_machine.report()
        case "off":
            break
        case _:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
