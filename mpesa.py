class Money:
    account = ""
    money = 0
    phone = ""

    def __init__(self, account, money, phone):
        self.phone = phone
        self.account = account
        self.money = money

    def withdraw(self):
        print("withdrawing")

    def buyairtime(self):
        print("buying airtime")

    def send(self, origin,  destination, amount):
        #print current balance 
        print(self.money)
        #check if balance is >= amount 
        print(f"new balance {self.money - amount}")
        #deduct current balance 
        #otherwite print invalid requet issuficient balance ..

        # print("send money")
        # input("Enter the name ")


mympesa = Money("mini", 370, "0768099729")
#print(mympesa.phone)
# mympesa.buyairtime()
print(mympesa.send("07949490260", "07688899728", 100))
