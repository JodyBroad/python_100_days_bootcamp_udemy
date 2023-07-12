# 1. print report
# 2. make sure it has sufficient resource to fulfill an order
# 3. process coins
# 4. check transaction successful
# 5. make coffee

menu = {
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
    "money": 0.00
}

complete = False

while not complete:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
    elif choice in menu:
        drink = choice
        if menu[drink]['ingredients']["water"] <= resources["water"]:
            enough_water = True
            if menu[drink]['ingredients']["milk"] <= resources["milk"]:
                enough_milk = True
                if menu[drink]['ingredients']["coffee"] <= resources["coffee"]:
                    enough_coffee = True
                    enough_resources = True

                    print("Please insert coins.")
                    quarters = int(input("How many quarters?: "))
                    dimes = int(input("How many dimes?: "))
                    nickels = int(input("How many nickels?: "))
                    pennies = int(input("How many pennies?: "))
                    input_amount = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
                    print(f"Cost of item: {menu[drink]['cost']}")
                    print(f"Amount entered: {input_amount}")
                    if input_amount >= menu[drink]["cost"]:
                        enough_money = True
                        resources["money"] += menu[drink]["cost"]
                        print(f"Enough money entered, here is {input_amount - menu[drink]['cost']} in change.")
                        resources["water"] -= menu[drink]['ingredients']["water"]
                        resources["milk"] -= menu[drink]['ingredients']["milk"]
                        resources["coffee"] -= menu[drink]['ingredients']["coffee"]
                    else:
                        print("Sorry, that's not enough money. Money refunded")
                else:
                    print("Sorry, there is not enough coffee")
            else:
                print("Sorry, there is not enough milk")
        else:
            print("Sorry, there is not enough water")
    else:
        print("Invalid selection, please try again")