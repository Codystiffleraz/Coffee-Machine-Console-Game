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
    "coffee": 100,
}
coffee_machine_on = True
while coffee_machine_on == True:

    # Ask customer what drink they would like
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == 'report':
        print(resources)
        drink = input("What would you like? (espresso/latte/cappuccino): ")

    # Create a variable to store drink in 
    user_drink = MENU[drink]
    # Ask Customer to insert coins
    print("Please insert coins.")

    # Ask how many of each coin
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    # Create a wallet to hold coins
    wallet = 0

    # Assign each coin to their amount
    wallet += quarters *.25
    wallet += dimes *.1
    wallet += nickles *.05
    wallet += pennies *.01

    # Create a variable that is true when the drink is completed
    drink_purchased = False

    # Compare to cost of drink selected
    user_drink_cost = user_drink["cost"]
    change = round(wallet - user_drink_cost, 2)
    if wallet < user_drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        coffee_machine_on = False
    elif wallet > user_drink_cost:
        drink_purchased = True
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink}.")
    else:
        drink_purchased = True
        print(f"Here is your {drink}.")
        
    # Users drink ingredients
    user_drink_ingredients = MENU[drink]['ingredients']

    if drink_purchased == True:
        if resources['water'] - user_drink_ingredients['water'] > 0:
            resources['water'] - user_drink_ingredients['water']
        else:
            print("Not enough resources.")
            coffee_machine_on = False
        if resources['coffee'] - MENU[drink]['ingredients']['coffee'] > 0:
           coffee = resources['coffee'] - MENU[drink]['ingredients']['coffee']
        else:
            print("Not enough resources.")
            coffee_machine_on = False
        if drink == 'latte' or drink == 'cappuccino':
            if resources['milk'] - MENU[drink]['ingredients']['milk'] > 0:
                milk = resources['milk'] - MENU[drink]['ingredients']['milk']
            else:
                print("Not enough resources.")
                coffee_machine_on = False
        