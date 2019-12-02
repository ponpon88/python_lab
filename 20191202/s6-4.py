class Banks():
    def __init__(self, uname):
        self.__name = uname
        self.__balance = 0
        self.__bankname = "Python Bank"
        self.__rate = 30
        self.__service_charge = 0.01

    def get_balance(self):
        return self.balance

    def save_money(self, money):
        self.balance += money
        return "存入%d ,存入完成" % money

    def withdraw_money(self, money):
        self.balance -= money
        return "提款%d ,提款完成" % money

    def usd_to_twd(self, usd):
        self.result = self.__money
        return "提款%d ,提款完成" % money

    def __cal_rate(self, usd):
        return int(usd * self.__rate * (1 - self.__service_charge))


userbank = Banks("Frank")

print(name, "Account Balance is:", userbank.get_balance())
print(userbank.save_money(1000))
print(userbank.name, "Account Balance is:", userbank.get_balance())
