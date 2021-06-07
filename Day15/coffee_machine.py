# Coffee Machine Program

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
profit = 0

def generate_report():
    '''Prints the report showing current resource values'''
    for resource, value in resources.items():
        print(f"{resource}: {value}")
    print(f"Money: {profit}")


def check_resource(coffee):
    '''
    Check if there are enough resources to make user's desired coffee.
    '''
    for ingredient, quantity in MENU[coffee]['ingredients'].items():
        if resources[ingredient] < quantity:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def process_coin():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    money = round((quarters * 0.25) + (dimes * 0.10) + (dimes * 0.05) + (pennies * 0.01), 2)
    return money        


def complete_transaction(money, coffee_cost):
    '''Return Boolean value by validating the payment'''
    if money >= coffee_cost:
        change = round(money - coffee_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded!")
        return False
        

def make_coffee(coffee_name, ingredients):
    '''Deduct the required ingredients from the resources.'''
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {coffee_name} ☕. Enjoy!")


def start():
    serving = True

    while serving:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if choice == 'off':
            print("Maintainence Mode!")
            serving = False
        elif choice == 'report':
            generate_report()
        elif choice in MENU.keys():
            coffee = MENU[choice]
            if check_resource(choice):
                money = process_coin()
                if complete_transaction(money, coffee['cost']):
                    make_coffee(choice, coffee['ingredients'])

start()