from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = Menu.find_drink(order_name=choice)
        if CoffeeMaker.is_resource_sufficient(drink):
            payment = MoneyMachine.process_coins()
            if MoneyMachine.make_payment():
                CoffeeMaker.make_coffee()

