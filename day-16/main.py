from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def main():
    while True:
        user_input = str(input(f'Welcome to grey\'s coffee machine\nPlease select your coffee from the list below:\n'
                               f'{menu.get_items()}: '))
        drink = menu.find_drink(user_input)
        if user_input == 'report':
            coffee_maker.report()
            money_machine.report()
        elif user_input == 'off':
            break
        else:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink).cost:
                coffee_maker.make_coffee(drink)


if __name__ == '__main__':
    main()
