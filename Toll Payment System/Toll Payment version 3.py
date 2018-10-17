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
    # Define a function to get number of car.
    def getNumofCar(self):
        return self.Car
    # Define a function to get number of bus.
    def getNumofBus(self):
        return self.Bus
    # Define a function to get number of truck.
    def getNumofTruck(self):
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
    # Define a function to sum up all fees.
    def Revenue(self):
        Ctotal = self.Car*self.Cprice
        Btotal = self.Bus*self.Bprice
        Ttotal = self.Truck*self.Tprice
        return float(Ctotal+Btotal+Ttotal)
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
# Make a class function of TollGate
class TollGate:
    # Make a list of 3 locations
    L1 = Location("Senayan","",5000.0,7000.0,9000.0)
    L2 = Location("Meruya","",6000.0,8000.0,10000.0)
    L3 = Location("Pondok Aren","",18000.0,20000.0,25000.0)
    locations =[L1,L2,L3]
    # Define a function to initialize class TollGate.
    def __init__(self,center):
        self.center = center
    # Define a function to get total number of locations
    def getNumofLoc(self):
        return len(self.locations)
    # Define a function to get a specific location.
    def getLocation(self,index):
        return self.locations[int(index)]
# Define a function to do Toll Payment system.
def checking():
    print("1.Senayan\n2.Meruya\n3.Pondok Aren")
    # Variable for inputting a specific number of location
    numIn=int(input(">"))
    # Variable for getting index of location
    number = numIn - 1
    # Make a variable of True statement
    isInput = True
    #As long as statement is True, it will run until it reaches False statement.
    while isInput:
        print("======PT. Jasa Marga======")
        print("Welcome to Toll Gate {}".format(T.getLocation(number).getName()))
        print("Category of Vehicle:\n1.Car: Rp. {}\n2.Bus: Rp. {}\n3.Truck: Rp.{}".format(T.getLocation(number).getCar_price(),
                                                                                          T.getLocation(number).getBus_price(),
                                                                                          T.getLocation(number).getTruck_price()))
        # Variable for inputting  1 vehicle based on its category.
        Fee=input(">")
        T.getLocation(number).addVehicle(Fee)
        T.getLocation(number).getPrice(Fee)
        print("Fee: {}".format(T.getLocation(number).getPrice(Fee)))
        print("Is there any vehicle? Y/N")
        # Variable for answer yes or no.
        answer = input(">")
        # When answer is equal to "N" or "n", it will show how many cars, buses, and trucks and sum all fees.
        if answer == "N" or answer == "n":
            T.getLocation(number).getNumofCar()
            T.getLocation(number).getNumofBus()
            T.getLocation(number).getNumofTruck()
            print("Car: {}\nBus: {}\nTruck: {}".format(T.getLocation(number).getNumofCar(),T.getLocation(number).getNumofBus(),
                                                       T.getLocation(number).getNumofTruck()))
            T.getLocation(number).Revenue()
            print("Total Revenue of the day: {}".format(T.getLocation(number).Revenue()))
            # when isInput becomes False, it will stop running.
            isInput = False
        # when answer is equal to "Y" or "y", it will return to start point again.
        elif answer == "Y" or answer == "y":
            isInput = True

# Make an object of class TollGate function.
T = TollGate("Jasa Marga")
# Make a variable of True statement
isStarting = True
# As long as statement is True, it will run until it reaches break.
while isStarting:
        print("Is there any location? Y/N")
        # Variable for answer yes or no
        answer=input(">")
        # when answer is equal to "Y" or "y", it will do Toll Payment system based on a specific location.
        if answer == "Y" or answer == "y":
            checking()
            isStarting=True
        # When answer is equal to "N" or "n", it will show the grand total of Toll Fees based on all locations and stop running.
        elif answer == "N" or answer == "n":
            grand_total = 0
            for i in range(T.getNumofLoc()):
                if T.getLocation(i).Revenue() != 0:
                    grand_total += T.getLocation(i).Revenue()
            print("Grand total: {}".format(grand_total))
            print("Exit program")
            break
