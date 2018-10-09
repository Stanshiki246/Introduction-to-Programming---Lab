# Stanley Tantysco - 2201814670

# import datetime built-ins.
import datetime as dt
# Make a class function of car.
class Car:
    # Define a function to initialize class Car.
    def __init__(self,license,price):
        # Make a self parameter for license
        self.license = license
        # Make a variable for current time.
        now = dt.datetime.now().strftime("%H:%M")
        # self parameter tIN is for variable time-in.
        self.tIn = dt.datetime.strptime(now,"%H:%M")
        # Make a self parameter for price with float type.
        self.price = float(price)
    # Define a function to return tIN value.
    def gettimeIn(self):
        return self.tIn
    # Define a function to return license value.
    def getlicense(self):
        return self.license
    # Define a function to count price based on duration.
    def Count(self,timeOut):
        # Variable for self parameter tIn.
        timeIn = self.tIn
        # Variable for time-out input.
        timeOut = dt.datetime.strptime(timeOut,"%H:%M")
        # Variable for getting duration.
        dur = timeOut - timeIn
        # Variable for splitting hours and minutes from duration.
        timeSp = str(dur).split(":")
        # Variable for getting hours only.
        timeH = int(timeSp[0])
        # When there is remainder in minutes, it will be counted as an hour for duration.
        if int(timeSp[1]) > 0:
            timeH += 1
        # Return result of timeH value timed by self parameter price value.
        return timeH * self.price
# Make a class for parking lot.
class ParkingLot:
    # Make a list of cars.
    carList = []
    # Define a function to initialize class ParkingLot.
    def __init__(self,price):
        self.price = float(price)
    # Define a function to add car.
    def addCar(self,license):
        self.carList.append(Car(license,self.price))
    # Define a function to get parking payment.
    def getPrice(self,index,timePut):
        pay = self.carList[index].Count(timePut)
        return pay
    # Define a function to get queue number of car.
    def getNumofCar(self):
        return len(self.carList)
    # Define a function to return list of cars.
    def getCar(self):
        return self.carList
    # Define a function to delete car after leaving parking lot.
    def rmvCar(self,index):
        del self.carList[int(index)]
# Variable for class ParkingLot with initial price of 1000.
P = ParkingLot(1000)

# while statement is True, it will run until press number "5" to quit.
while True:
    print("Welcome to Fx Sudirman Parking Lot")
    print("1.Input Your Car\n2.Check Car\'s List\n3.Find your Car\n4.Pay and Leave\n5.Exit")
    # Variable for inputting options.
    mode=input(">")
    # When option 1 is chosen, it will add car into carList.
    if mode == "1":
        print("Enter your license car in here: ")
        License=input(">")
        P.addCar(License)
        print("Car with license {} has entered in here.".format(License))
    # When option 2 is chosen, it will show list of cars.
    if mode == "2":
        for i in range(0,P.getNumofCar()):
            print("Number: {} Car \'s License: {}".format(i,P.getCar()[i].getlicense()))
    # When option 3 is chosen, it will search a specific car from carList.
    if mode == "3":
        print("Enter your car\'s queue number: ")
        Number=int(input(">"))
        if P.getNumofCar() > Number:
            print("Your car with license {} has been found.".format(P.getCar()[Number].getlicense()))
        else:
            print("Your car is not in here.")
    # When option 4 is chosen, it will show parking payment and remove a specific car after leaving at a specific time.
    if mode == "4":
        print("Enter your car\'s queue number: ")
        Number=int(input(">"))
        if P.getNumofCar() > Number:
            Mylicense= P.getCar()[Number].getlicense()
            print("Your car with {} is in here.".format(Mylicense))
            print("What time do you want to leave? (Format: HH:MM)")
            TimeLeaving= input(">")
            print("Your parking costs Rp.{}. Thank you for coming here".format(P.getPrice(Number,TimeLeaving)))
            P.rmvCar(Number)
        else:
            print("Your car is not in here.")
    # When option 5 is chosen, it will stop running.
    if mode == "5":
        break




