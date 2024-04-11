from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

print(f"money_machine {money_machine}")
print(f"coffee_maker {coffee_maker}")
print(f"menu {menu}")

is_on = True

while is_on:
    options = menu.get_items()
    print(f"options are :  {options}")
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        #print(f"coffee_maker.report() : {coffee_maker.report()}")
        coffee_maker.report()
        #print(f"money_machine.report() : {money_machine.report()}")
        money_machine.report()
    else:
        #print(f"menu.find_drink(choice) : {menu.find_drink(choice)}")
        drink = menu.find_drink(choice)
        #print(f"drink : {drink}")
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
