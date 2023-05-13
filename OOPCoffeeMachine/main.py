from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

def menu_format(my_menu):
    for i in range(3):
        print(f"{my_menu.menu[i].name} : ${my_menu.menu[i].cost}") 
menu_format(my_menu)
machine_on = True
while machine_on:
    request = input(f"What would you like?")
    if request == "off":
        print("Machine is turning off.")
        machine_on = False
    elif request == "report":
        coffeemaker.report()
        money_machine.report()
    elif request == "refill":
        coffeemaker.refill_resources()
    else:
        drink = my_menu.find_drink(request)
        if coffeemaker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
