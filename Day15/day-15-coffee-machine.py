import sys
# dictionary
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# variables
loop = True
quarters = float(0.25)
dimes = float(0.10)
nickles = float(0.05)
pennies = float(0.01)
espresso_cost = float((MENU.get('espresso').get('cost')))
latte_cost = float((MENU.get('latte').get('cost')))
cappuccino_cost = float((MENU.get('cappuccino').get('cost')))


def is_resource_sufficient(order_ingredients):
    """Calculate if there is enough resource to brew the selected coffee"""
    global loop
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total of inserted coins"""
    print("Please insert coins")
    total = int(input("How many quarters: ")) * quarters
    total += int(input("How many dimes: ")) * dimes
    total += int(input("How many nickles: ")) * nickles
    total += int(input("How many pennies: ")) * pennies
    total = round(total, 2)
    print(f"You inserted ${total} in coins.")
    return total


def is_transaction_successful(money_received, cost_of_drink):
    global profit
    """Return true if payment accepted, or return false if not accepted."""
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change. Enjoy the {choice} ☕️")
        profit += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name,order_ingredients):
    """Deduct required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


while loop:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        loop = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml ")
        print(f"Coffee: {resources['coffee']}g ")
        print(f"Money: ${profit} ")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
