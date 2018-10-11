# Make a class function of vehicles
class Vehicle:
    # Make a counter of passing cars through toll gates.
    Car=0
    # Make a counter of passing buses through toll gates.
    Bus=0
    # Make a counter of passing trucks through toll gates.
    Truck=0
    # Define a function to initialize class Vehicle.
    def __init__(self,vehicle):
        self.vehicle=vehicle
    # Define a function to add number of vehicle whether it is car, bus, or truck.
    def addVehicle(self,vehicle):
        if vehicle == "car" or vehicle == "Car":
            self.Car += 1
            return self.Car
        elif vehicle == "bus" or vehicle == "Bus":
            self.Bus += 1
            return self.Bus
        elif vehicle == "truck" or vehicle == "Truck":
            self.Truck += 1
            return self.Truck
# Make a class function of location which inherits class Vehicle
class Location(Vehicle):
    # Define a function to initialize class Location and inherit class Vehicle
    def __init__(self,name,vehicle,Cprice,Bprice,Tprice):
        super().__init__(vehicle)
        self.Cprice = float(Cprice)
        self.Bprice = float(Bprice)
        self.Tprice = float(Tprice)
        self.name = str(name)
    # Define a function to get fee based on 3 category of vehicles such as cars, buses, and trucks.
    def getPrice(self,type):
        if type == "car" or type == "Car":
            return self.Cprice
        elif type == "bus" or type == "Bus":
            return self.Bprice
        elif type == "truck" or type == "Truck":
            return self.Tprice
    # Define a function to get name of location
    def getName(self):
        return self.name
    # Define a function to get value of car's fee
    def getCar_price(self):
        return float(self.Cprice)
    # Define a function to get value of bus's fee
    def getBus_price(self):
        return float(self.Bprice)
    # Define a function to get value of truck's fee
    def getTruck_price(self):
        return float(self.Tprice)
# Make an object of class Location that inherit class Vehicle
T = Location("Meruya","",6000.0,8000.0,10000.0)

# Make a variable of True statement
isInput = True
#As long as statement is True, it will run until it reaches False statement.
while isInput:
    print("======PT. Jasa Marga======")
    print("Welcome to Toll Gate {}".format(T.getName()))
    print("Category of Vehicle:\n1.Car: Rp. {}\n2.Bus: Rp. {}\n3.Truck: Rp.{}".format(T.getCar_price(),
                                                                                          T.getBus_price(),
                                                                                         T.getTruck_price()))
    # Variable for inputting  1 vehicle based on its category.
    Fee=input(">")
    T.addVehicle(Fee)
    T.getPrice(Fee)
    # print fee based on its vehicle category.
    print("Fee: {}".format(T.getPrice(Fee)))
    print("Is there any vehicle? Y/N")
    # Variable for answer yes or no.
    answer = input(">")
    # When answer is equal to "N" or "n", it will show how many cars, buses, and trucks and sum all fees.
    if answer == "N" or answer == "n":
        # when isInput becomes False, it will stop running.
        isInput = False
    # when answer is equal to "Y" or "y", it will return to start point again.
    elif answer == "Y" or answer == "y":
        isInput = True
