#  At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk,
#  120 g of coffee beans, and 9 disposable cups.

class CoffeeMachine:

    def __init__(self, amount, water, milk, beans, dis_cups):
        self.amount = amount
        self.water = water
        self.milk = milk
        self.beans = beans
        self.dis_cups = dis_cups

    def print_machine_state(self):
        print('\nThe coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.dis_cups} of disposable cups')
        print(f'${self.amount} of money')

    def check_resources(self, w, m, b, c):
        if self.water - w < 0:
            print('Sorry, not enough water!')
            return False
        elif self.milk - m < 0:
            print('Sorry, not enough milk!')
            return False
        elif self.beans - b < 0:
            print('Sorry, not enough coffee beans!')
            return False
        elif self.dis_cups - c < 0:
            print('Sorry, not enough disposable coffee cups!')
            return False
        else:
            print('I have enough resources, making you a coffee!')
            return True

    def operation_buy(self):
        coffee_type = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')

        if coffee_type == '1':  # espresso
            # 250 ml of water and 16 g of coffee beans. It costs $4.
            if self.check_resources(250, 0, 16, 1):
                self.water -= 250
                self.beans -= 16
                self.amount += 4
                self.dis_cups -= 1
        elif coffee_type == '2':  # latte
            # 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7
            if self.check_resources(350, 75, 20, 1):
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.amount += 7
                self.dis_cups -= 1
        elif coffee_type == '3':  # cappuccino
            # 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6
            if self.check_resources(250, 100, 12, 1):
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.amount += 6
                self.dis_cups -= 1
        elif coffee_type == 'back':  # back - to main menu
            pass

    def operation_fill(self):
        self.water += int(input('\nWrite how many ml of water you want to add: '))
        self.milk += int(input('Write how many ml of milk you want to add: '))
        self.beans += int(input('Write how many grams of coffee beans you want to add: '))
        self.dis_cups += int(input('Write how many disposable coffee cups you want to add: '))

    def operation_take(self):
        print(f'I gave you ${self.amount}')
        self.amount = 0


def main():
    machine = CoffeeMachine(550, 400, 540, 120, 9)
    while True:
        action = input('\nWrite action (buy, fill, take, remaining, exit):\n').lower()
        if action == 'buy':
            machine.operation_buy()
        elif action == 'fill':
            machine.operation_fill()
        elif action == 'take':
            machine.operation_take()
        elif action == 'remaining':
            machine.print_machine_state()
        elif action == 'exit':
            exit()
# ------------


main()
