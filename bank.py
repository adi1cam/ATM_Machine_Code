class atm:
    def __init__(self):
        self.pin=""
        self.__balance=0
    
    def menu(self):
        user_input=input("""how would you like to proceed?
                         1.enter 1 to create pin
                         2.enter 2 to deposit
                         3.enter 3 to withdraw1
                         4.enter 4 to check balance
                         5.enter 5 to exit
""")
        if user_input=="1":
          self.pin=input("please enter your pin:")
          print("your pin is:",self.pin)
        elif user_input=="2":
            print("deposit")
        elif user_input=="3":
            print("withdraw")
        elif user_input=="4":
            print("balance")
        else:
            print("bye")
    def deposit_amount(self):
        amount=int(input("please enter amount you want to deposit:"))
        self.__balance=int(amount+self.__balance)
        print("your deposited amount:",amount)
    def chk_balance(self):
       enter_pin=input("please enter your pin:")
       if self.pin==enter_pin:
          print("your balance is:",self.__balance)
       else:
          print("wrong pin")
    def withdraw(self):
       enter_pin=input("please enter your pin:")
       if self.pin==enter_pin:
        print("how much do you want to withdraw:")
        amount=int(input("enter the amount to withdraw:"))
        self.__balance=int(self.__balance-amount)
        print("your new balance is",self.__balance)
       else:
          print("wrong pin")
sbi=atm()
sbi.menu()
sbi.deposit_amount()
sbi.chk_balance()
sbi.withdraw()