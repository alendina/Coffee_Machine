class PiggyBank:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, dollars, cents):
        self.cents += int(cents) % 100
        self.dollars += int(cents) // 100 + int(dollars)
        if self.cents == 100:
            self.cents = 0
            self.dollars += 1


# p = PiggyBank(1, 1)
# p.add_money(1, 99)
# print(p.dollars, p.cents)
# p.add_money(500, 500)
# print(p.dollars, p.cents)
