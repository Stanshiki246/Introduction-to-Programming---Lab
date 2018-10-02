# Class Calculator by Stanley Tantysco - 2201814670.
# Make a calculator program by using class function.

# Define a class for Calculator.
class Calculator:
    # Define a function for objects
    def __init__(self,op1,op2,op3):
        self.op1 = op1 # parameter for first input operation number.
        self.op2 = op2 # parameter for second input operation number.
        self.op3 = op3 # parameter for operator.
    # Define a function for choosing operator.
    def operator(self):
        # when inputting "+" in op3.
        if self.op3 == "+":
            # result = op1 + op2
            result = lambda op1,op2:op1+op2
            # print the result after op1 is added by op2.
            print(result(self.op1,self.op2))
        # when inputting "-" in op3.
        elif self.op3 == "-":
            # result = op1 - op2
            result = lambda op1,op2:op1-op2
            # print the result after op1 is subtracted by op2.
            print(result(self.op1,self.op2))
        # when inputting "*" in op3.
        elif self.op3 == "*":
            # result = op1*op2
            result = lambda op1,op2:op1*op2
            # print the result after op1 is multiplied by op2.
            print(result(self.op1,self.op2))
        # when inputting "/" in op3.
        elif self.op3 == "/":
            # result = op1/op2
            result = lambda op1,op2:op1/op2
            # print the result after op1 is divided by op2.
            print(result(self.op1,self.op2))

a=int(input("Enter number: ")) # variable for first input operation number.
b=int(input("Enter number: ")) # variable for second input operation number.
c=input("Enter operator:")   # variable for operator.
C = Calculator(a,b,c) # Variable for class function.
C.operator() # Counting after inputting operator.
