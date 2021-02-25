import hashlib
from time import sleep

from rich.console import Console
from rich.table import Table

import data
import grey

console = Console()


def passwd_verification(uname, passwd):
    key_check = hashlib.pbkdf2_hmac(
        'sha256',
        passwd.encode('utf-8'),
        data.passwords[uname]['hash_key'][:32],
        data.passwords['iterations'],
        dklen=256
    )

    if key_check == data.passwords[uname]['hash_key'][32:]:
        if_validated = True
    else:
        if_validated = False

    return if_validated


def make(coffee):
    def resources_subtract(resource_types):
        for resource_type in resource_types:
            if resource_type in data.MENU[coffee]['ingredients']:
                data.resources[resource_type] -= data.MENU[coffee]['ingredients'][resource_type]

    resources_subtract(['water', 'milk', 'coffee'])


def restock():
    def restock_func(resource, number):
        data.resources[resource] = number

    item_amount = 300

    for item in data.resources:
        restock_func(resource=item, number=item_amount)
        item_amount -= 100


def report_table_func():
    report_table = Table(show_header=True, header_style='bold dodger_blue1')

    report_table.add_column('Name', width=8, justify='left')
    report_table.add_column('Amount', width=10, justify='right')

    report_table.add_row(
        'Water:',
        f'{data.resources["water"]}'
    )
    report_table.add_row(
        'Milk:',
        f'{data.resources["milk"]}'
    )
    report_table.add_row(
        'Coffee:',
        f'{data.resources["coffee"]}'
    )
    report_table.add_row(
        'Money:',
        f'${data.resources["money"]}'
    )

    return report_table


def coffee_table_func(if_in_stock):
    coffee_table = Table(show_header=True, header_style='bold magenta')

    coffee_table.add_column('Coffee', width=12, justify='left')
    coffee_table.add_column('Cost', width=8, justify='center')
    coffee_table.add_column('In Stock', width=10, justify='right')

    coffee_table.add_row(
        "Espresso",
        "$1.50",
        f"{if_in_stock[0]}"
    )
    coffee_table.add_row(
        "Latte",
        "$2.50",
        f"{if_in_stock[1]}"
    )
    coffee_table.add_row(
        "Cappuccino",
        "$3.00",
        f"{if_in_stock[2]}"
    )

    return coffee_table


def money_count():
    print('Please insert your coins.')

    quarters = int(input('Quarters: ') or '0')
    dimes = int(input('Dimes: ') or '0')
    nickles = int(input('Nickels: ') or '0')
    pennies = int(input('Pennies: ') or '0')

    return ((((quarters * 25) + (dimes * 10)) + (nickles * 5)) + (pennies * 1)) / 100


def main():
    data.resources['money'] = 0
    espresso_in_stock = True
    latte_in_stock = True
    cappuccino_in_stock = True

    def resources_sort(water, coffee, milk):
        return data.resources['water'] < water or data.resources['coffee'] < coffee or data.resources['milk'] < milk

    while True:
        grey.clear()
        if resources_sort(50, 14, 0):
            espresso_in_stock = False
        if resources_sort(200, 24, 150):
            latte_in_stock = False
        if resources_sort(250, 24, 100):
            cappuccino_in_stock = False

        console.print('Welcome, please select your [bold magenta]coffee[/bold magenta] from the list below.\n')

        if_in_stock = [espresso_in_stock, latte_in_stock, cappuccino_in_stock]

        coffee_table = coffee_table_func(if_in_stock)

        console.print(coffee_table, '\n')

        user_input = str(input('What would you like? (espresso/latte/cappuccino): ').lower())

        out_of_stock_check = {
            'espresso': espresso_in_stock,
            'latte': latte_in_stock,
            'cappuccino': cappuccino_in_stock
        }

        if user_input == 'report' or user_input == 'restock':
            print('Password verification required for system modification.')
            uname_in = str(input('\nPlease enter your username: '))
            passwd_in = str(input('Please enter your password: '))
            passwd_val = passwd_verification(uname=uname_in, passwd=passwd_in)
            if passwd_val is True:
                if user_input == 'report':
                    report_table = report_table_func()
                    while True:
                        grey.clear()
                        console.print('\nHere is your [bold dodger_blue1]Report[/bold dodger_blue1] Table\n')
                        console.print(report_table)
                        if input(f'\nPlease type "done" to reset: ').lower() == 'done':
                            break
                elif user_input == 'restock':
                    restock()
                    console.print('Successfully registered [bold dark_red]restock[/bold dark_red]')
                    sleep(2)
            else:
                print('Password was incorrect.')
                sleep(14)
        elif user_input in data.MENU and out_of_stock_check[user_input] is True:
            total_money = money_count()
            change = total_money - data.MENU[user_input]['cost']
            if change >= 0:
                print(f'\nYour change is ${change}')
                print(f'\nMaking a {user_input}')
                data.resources['money'] += total_money - change
                make(coffee=user_input)
                sleep(4)
                print('\nHere is your coffee. Remember, share and enjoy!')
                sleep(6)
            else:
                print('\nYou have not provided the required amount of money.')
                sleep(4)
        elif user_input == '':
            continue
        else:
            print('\nThe item you are requesting is either out of stock or not in the menu.')
            sleep(4)


if __name__ == '__main__':
    main()
