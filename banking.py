# Make a class function of ATM
class ATM:
    # Define a function to initialize class ATM
    def __init__(self,balance):
        self.balance = float(balance)
    # Define a function to return balance value
    def get_balance(self):
        return float(self.balance)
    # Define a function to deposit money
    def deposit(self,amt):
        # Variable for amount
        self.amt = float(amt)
        self.balance += amt
        # when amt value is greater than or equal to 0, it will become True statement
        if self.amt >= 0:
            return True
        else:
            return False
    # Define a function to withdraw money
    def withdraw(self,amt):
        # Variable for amount
        self.amt=float(amt)
        self.balance -= amt
        # when balance value is less than 0, it will become False statement
        if self.balance < 0:
            return False
        else:
            return True
    # Define a function to transfer money out
    def transferOut(self,amt):
        # Variable for amount
        self.amt=float(amt)
        self.balance -= amt
        # when balance value is less than 0, it will become False statement
        if self.balance < 0:
            return False
        else:
            return True
    # Define a function to get transferred money.
    def transferIn(self,amt):
        # Variable for amount
        self.amt = float(amt)
        self.balance += amt
        # when amt value is greater than or equal to 0, it will become True statement
        if self.amt >= 0:
            return True
        else:
            return False
# Make a class function of Customer
class Customer:
    # Define a function to initialize class Customer
    def __init__(self,fName,lName,Account):
        self.fName = fName
        self.lName = lName
        self.account =Account
    # Define a function to return fname value
    def get_firstName(self):
        return self.fName
    # Define a function to return lname value
    def get_lastName(self):
        return self.lName
    # Define a function to return Account value
    def get_acc(self):
        return self.account
    # Define a function to update Account value
    def set_acc(self,Account):
        self.account = Account
# Make a class function of Bank
class Bank:
    # Make a list of customers
    customers = []
    # Define a function to initialize class Bank
    def __init__(self,bname):
        self.bname = str(bname)
    # Define a function to add customer.
    def addCustomer(self,fName,lName):
        self.customers.append(Customer(fName,lName,ATM(0)))
    # Define a function to delete customer.
    def delCustomer(self,index):
        del self.customers[int(index)]
    # Define a function to change name of customer.
    def changeName(self,index,fName,lName,balance):
        self.customers[index]=Customer(fName,lName,ATM(balance))
    # Define a function to get number of customers
    def get_numOfCus(self):
        return len(self.customers)
    # Define a function to get customer's queue number
    def get_customer(self,index):
        return self.customers[int(index)]
# Variable for class Bank.
b=Bank("Regalia")
# when the statement is True, it will run until it meets break code.
while True:
    print("Welcome to Bank Regalia")
    print("1.Create Account\n2.Check List\n3.Check Balance\n4.Deposit\n5.Withdraw\n6.Transfer\n7.Delete Account\n8.Change Name\n9.Exit")
    # Variable for inputting options
    mode = input(">")
    # when option 1 is pressed, it will add full name of customer into list of customers.
    if mode == "1":
        firstName=input("Enter your first name: ")
        lastName=input("Enter your last name: ")
        b.addCustomer(firstName,lastName)
        print("{} {} has been registered".format(firstName,lastName))
    # when option 2 is pressed, it will show list of customers.
    elif mode == "2":
        for i in range(0,b.get_numOfCus()):
            print("{}.{} {}".format(i,b.get_customer(i).get_firstName(),b.get_customer(i).get_lastName()))
    # when option 3 is pressed, it will search for a specific customer's account.
    elif mode == "3":
        print("Input your bank number")
        BankNum = int(input(">"))
        if b.get_numOfCus() > BankNum:
            print("Name:{}\nBalance: {}".format(b.get_customer(BankNum).get_firstName(),b.get_customer(BankNum).get_acc().get_balance()))
        else:
            print("Not Found")
    # when option 4 is pressed, it will show deposit function.
    elif mode == "4":
        print("Input your bank number")
        BankNum = int(input(">"))
        if b.get_numOfCus() > BankNum:
            MyfName= b.get_customer(BankNum).get_firstName()
            MyBalance= b.get_customer(BankNum).get_acc().get_balance()
            print("Name:{}\nBalance: {}".format(MyfName,MyBalance))
            print("Input the amount of money to be put in deposit")
            value=float(input(">"))
            b.get_customer(BankNum).get_acc().deposit(value)
            print("Name:{}\nBalance: {}".format(MyfName,b.get_customer(BankNum).get_acc().get_balance()))
        else:
            print("Not Found")
    # when option 5 is pressed, it will show withdraw function
    elif mode == "5":
        print("Input your bank number")
        BankNum = int(input(">"))
        if b.get_numOfCus() > BankNum:
            MyfName= b.get_customer(BankNum).get_firstName()
            MyBalance= b.get_customer(BankNum).get_acc().get_balance()
            print("Name:{}\nBalance: {}".format(MyfName,MyBalance))
            print("Input the amount of money to be withdrawn")
            value=float(input(">"))
            b.get_customer(BankNum).get_acc().withdraw(value)
            print("Name:{}\nBalance: {}".format(MyfName,b.get_customer(BankNum).get_acc().get_balance()))
        else:
            print("Not Found")
    # when option 6 is pressed, it will show transfer function
    elif mode == "6":
        print("Input your bank number")
        BankNum = int(input(">"))
        print("Input another bank number")
        # Variable for another bank number
        AnNum = int(input(">"))
        if b.get_numOfCus() > BankNum and b.get_numOfCus() > AnNum:
            MyfName= b.get_customer(BankNum).get_firstName()
            MyBalance= b.get_customer(BankNum).get_acc().get_balance()
            print("Name:{}\nBalance: {}".format(MyfName,MyBalance))
            print("Input the amount of money to be transferred")
            value=float(input(">"))
            b.get_customer(BankNum).get_acc().transferOut(value)
            b.get_customer(AnNum).get_acc().transferIn(value)
            print("Name:{}\nBalance: {}".format(MyfName,b.get_customer(BankNum).get_acc().get_balance()))
        else:
            print("Not Found")
    # when option 7 is pressed, it will delete a specific customer's account.
    elif mode == "7":
        print("Input your bank number")
        BankNum = int(input(">"))
        if b.get_numOfCus() > BankNum:
            MyfName=b.get_customer(BankNum).get_firstName()
            MylName=b.get_customer(BankNum).get_lastName()
            MyBalance= b.get_customer(BankNum).get_acc().get_balance()
            print("Name:{} {}\nBalance: {}".format(MyfName,MylName,MyBalance))
            print("Do you want to delete your account? Y/N")
            answer = input(">")
            if answer == "Y" or answer == "y":
                b.delCustomer(BankNum)
                print("{} {} has been deleted".format(MyfName,MylName))
            else:
                print("invalid input")
        else:
            print("Not Found")
    # when option 8 is pressed, it will change full name of a specific customer's account.
    elif mode == "8":
        print("Input your bank number")
        BankNum = int(input(">"))
        if b.get_numOfCus() > BankNum:
            MyfName=b.get_customer(BankNum).get_firstName()
            MylName=b.get_customer(BankNum).get_lastName()
            MyBalance= b.get_customer(BankNum).get_acc().get_balance()
            print("Name:{} {}\nBalance: {}".format(MyfName,MylName,MyBalance))
            print("Do you want to change your name? Y/N")
            answer = input(">")
            if answer == "Y" or answer == "y":
                NewfName = input("Input your new first name: ")
                NewlName = input("Input your new last name: ")
                b.changeName(BankNum,NewfName,NewlName,MyBalance)
                print("Your name has been changed into {} {}. Balance: {}".format(NewfName,NewlName,MyBalance))
            else:
                print("invalid input")
    # when option 9 is pressed, it will stop running.
    elif mode == "9":
        print("Goodbye")
        break
