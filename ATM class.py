# Define a class for ATM.
class ATM:
    # Define a function to initialize ATM class.
    def __init__(self,balance,wallet,another):
        self.balance = float(balance) # Variable for my balance.
        self.wallet = float(wallet) # Variable for my wallet.
        self.another = float(another) # Variable for another balance.
    # Define a function to show my balance and my wallet.
    def get_balance(self):
        return print("Balance:",self.balance,"Wallet:",self.wallet) # print my current balance and wallet.
    # Define a function to add my balance amount from my wallet.
    def deposit(self):
        # print the display of deposit.
        print("Enter the amount of money to be put in")
        amount = float(input(">")) # Variable for input how many money to be put in my balance.
        self.balance += amount # the amount is added to my balance.
        self.wallet -= amount # the amount in my wallet is decreased.
        if self.wallet < 0: # when my wallet is less than 0, it becomes invalid.
            return False
        else: # when my wallet is more than or equal to 0, it will print my new balance and wallet.
            return print("Balance:",self.balance,"Wallet:",self.wallet)
    # Define a function to add my wallet amount from my balance.
    def withdraw(self):
        # print the display of withdraw.
        print("Enter the amount of money to be withdrawn")
        amount =float(input(">")) # Variable for input how many money to be withdrawn from my balance.
        self.balance -= amount # the amount in my balance is decreased.
        self.wallet += amount # the amount is added to my wallet.
        if self.balance < 0: # when my balance is less than 0, it becomes invalid.
            return False
        else:  # when my balance is more than or equal to 0, it will print my new balance and wallet.
            return print("Balance:",self.balance,"Wallet:",self.wallet)
    # Define a function to decrease my balance amount for paying.
    def debit(self):
        # print the display of debit.
        print("Enter the amount of money to be paid")
        amount =float(input(">")) # Variable for input how many money to be paid.
        self.balance -= amount # the amount in my balance is decreased.
        if self.balance < 0: # when my balance is less than 0, it becomes invalid.
            return False
        else: # when my balance is more than or equal to 0, it will print my new balance and current wallet.
            return print("Balance:",self.balance,"Wallet:",self.wallet)
    # Define a function to transfer money from my balance to another balance.
    def transfer(self):
        # print the display of transfer.
        print("Enter the amount of money to be transferred to another user")
        amount=int(input(">")) # Variable for input how many money to be transferred.
        self.balance -= amount # the amount in my balance is decreased.
        self.another += amount # the decreased amount from my balance is added to another user.
        if self.balance < 0: # when my balance is less than 0, it becomes invalid.
            return False
        else:  # when my balance is more than or equal to 0, it will print my balance and another user after transferring.
            return print("Balance:",self.balance,"Another Balance:",self.another)
# Variable for inputiing my initial wallet
setWallet = float(input("My initial wallet: "))
a=ATM(0,setWallet,0) # Variable for ATM class with settings such as my balance=0, my wallet = amount of my initial wallet, another balance = 0.
# while statement is True, it will loop until I press "q" to stop.
while True:
    # to show options in ATM.
    print("1. Check\n2. Deposit\n3. Withdraw\n4. Debit\n5. Transfer")
    # Variable for inputting the number to execute approriated option.
    mode = input(">")
    if mode == "1": # when i press number 1, it will show my balance and wallet.
        a.get_balance()
    elif mode == "2": # when i press number 2, it will show deposit option.
        a.deposit()
    elif mode == "3": # when i press number 3, it will show withdraw option.
        a.withdraw()
    elif mode == "4": # when i press number 4, it will show debit option.
        a.debit()
    elif mode == "5": # when i press number 5, it will show transfer option.
        a.transfer()
    elif mode == "q": # when i press "q", it will be end.
        break
