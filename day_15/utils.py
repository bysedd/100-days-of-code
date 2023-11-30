def check_resources(water: int, milk: int, coffee: int, *, drink: str) -> bool:
    """
    Check if there are enough resources to make a given drink.

    :param drink: The name of the drink.
    :param water: The amount of water available.
    :param milk: The amount of milk available.
    :param coffee: The amount of coffee available.
    :return: True if there are enough resources, False otherwise.
    """
    from day_15.data import menu

    drink_ingredients = menu[drink]["ingredients"]
    current_resources = {
        "water": water,
        "milk": milk,
        "coffee": coffee,
    }

    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > current_resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True
