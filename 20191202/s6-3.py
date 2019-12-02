class Banks():
    bankname = 'Python Bank'

    def __init__(self, uname, money):
        self.name = uname
        self.balance = money

    def hello(sef):
        return "Hello User"

    def get_balance(self):
        return self.balance

    def save_money(self, money):
        self.balance += money
        return "存入%d ,存入完成" % money

    def withdraw_money(self, money):
        self.balance -= money
        return "提款%d ,提款完成" % money


userbank = Banks("Frank", 100)

print("new object is:", userbank.bankname)
print("new Object method is:", userbank.hello())
print(userbank.name, "Account Balance is:", userbank.get_balance())
print(userbank.save_money(1000))
print(userbank.name, "Account Balance is:", userbank.get_balance())

print(userbank.withdraw_money(1000))
print(userbank.name, "Account Balance is:", userbank.get_balance())
