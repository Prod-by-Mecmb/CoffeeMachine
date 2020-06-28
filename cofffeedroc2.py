class CoffeeMachine:

    resources = ['water', 'milk', 'beans', 'cups']
    at_resources, at_money = [400, 540, 120, 9], 550
    espresso, latte, cappuccino, check = [250, 0, 16, 1], [350, 75, 20, 1], [200, 100, 12, 1], []

    def __init__(self):
        self.newsum = 0

    def checky(self):
        self.n = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if self.n == 'back':
            return
        if self.n == '1':
            CoffeeMachine.check = [a - b for a, b in zip(CoffeeMachine.at_resources, CoffeeMachine.espresso)]
            self.newsum = 4
        elif self.n == '2':
            CoffeeMachine.check = [a - b for a, b in zip(CoffeeMachine.at_resources, CoffeeMachine.latte)]
            self.newsum = 7
        elif self.n == '3':
            CoffeeMachine.check = [a - b for a, b in zip(CoffeeMachine.at_resources, CoffeeMachine.cappuccino)]
            self.newsum = 6
        for id, item in enumerate(CoffeeMachine.check):
            if item < 0:
                print(f'Sorry, not enough {self.resources[CoffeeMachine.check.index(item)]}!')
                break
            else:
                CoffeeMachine.at_resources = CoffeeMachine.check
                CoffeeMachine.at_money += self.newsum
                print('I have enough resources, making you a coffee!\n')
                break


    def fill(self):
        CoffeeMachine.at_resources[0] += int(input('\nWrite how many ml of water do you want to add:\n'))
        CoffeeMachine.at_resources[1] += int(input('Write how many ml of milk do you want to add:\n'))
        CoffeeMachine.at_resources[2] += int(input('Write how many grams of coffee beans do you want to add:\n'))
        CoffeeMachine.at_resources[3] += int(input('Write how many disposable cups of coffee do you want to add:\n'))

    def take(self):
        print(f'I gave you ${self.at_money}')
        CoffeeMachine.at_money = 0

    def method(self, user_input):
        self.user_input = user_input
        if self.user_input == 'remaining':
            print(f'\nThe coffee machine has:\n'
                  f'{CoffeeMachine.at_resources[0]} of water\n'
                  f'{CoffeeMachine.at_resources[1]} of milk\n'
                  f'{CoffeeMachine.at_resources[2]} of beans\n'
                  f'{CoffeeMachine.at_resources[3]} of cups\n'
                  f'${CoffeeMachine.at_money} of money\n')
        if self.user_input == 'buy':
            self.checky()
        if self.user_input == 'fill':
            self.fill()
        if self.user_input == 'take':
            self.take()

cm = CoffeeMachine()

while True:
    cm.method(input('\nWrite action (buy, fill, take, remaining, exit):\n'))
    if cm.user_input == 'exit':
        break