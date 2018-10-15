# Make a class function of Room.
class Room:
    # Variables for single-bed and double-bed.
    single = 0
    double = 0
    # Define a constructor for class Room
    def __init__(self,rtype):
        # variable for room type
        self.rtype =  rtype
    # Define a function to add number of single-bed and double-bed
    def addType(self,rtype):
        if rtype == "1":
            self.single += 1
            return self.single
        elif rtype == "2":
            self.double += 1
            return self.double
    # Define a function to show number of single-bed
    def getNumofSingle(self):
        return self.single
    # Define a function to show number of double-bed.
    def getNumofDouble(self):
        return self.double
# Make a class function of Hotel.
class Hotel(Room):
    # Variable for list of room.
    RoomList = []
    # Define a constructor to inherit attributes from class Room
    def __init__(self,name,room,rtype):
        super().__init__(rtype)
        self.name = name
        self.room = room
    # Define a function of check-in
    def checkIn(self,room):
        self.RoomList.append(room)
    # Define a function of check-out
    def checkOut(self,index):
        del self.RoomList[int(index)]
    # Define a function to check whether the room is occupied or not.
    def checking(self,room):
        if room in self.RoomList:
            print("It has been occupied.")
        else:
            print("It is empty.")
    # Define a function to sum all used rooms in a day.
    def Revenue(self,Sprice,Dprice):
        # variables for single-bed price and double-bed price
        self.Sprice=float(Sprice)
        self.Dprice=float(Dprice)
        # variables for total of single-bed prices and total of double-bed prices
        Stotal = self.getNumofSingle()*self.Sprice
        Dtotal = self.getNumofDouble()*self.Dprice
        return float(Stotal + Dtotal)
    # Define a function to show number of used rooms.
    def getNumofRoom(self):
        return len(self.RoomList)
    # Define a function to get room
    def getRoom(self,index):
        return self.RoomList[int(index)]
# Object for class Hotel.
H = Hotel("Hariston Hotel","","")
# It will run as long as statement is True.
while True:
    print("Welcome to Hariston Hotel")
    print("1.Check-in\n2.Check-out\n3.Check room\n4.Revenue\n5.Exit")
    # Variable for inputting option
    mode = input(">")
    # if option 1 is chosen, it will do check-in
    if mode == "1":
        RoomNum = input("Enter your room number: ")
        print("Room type:\n1.Single\n2.Double")
        RType = input(">")
        H.addType(RType)
        H.checkIn(RoomNum)
        print("Successfully checked-in the room {}.".format(RoomNum))
    # if option 2 is chosen, it will do check-out
    elif mode == "2":
        RoomInd = int(input("Enter your room index: "))
        if H.getNumofRoom() > RoomInd:
            MyRoom = H.getRoom(RoomInd)
            print("Your room is number {}".format(MyRoom))
            print("Do you want to leave? Y/N")
            answer =  input(">")
            if answer == "Y" or answer == "y":
                print("Successfully checked-out from room {}".format(MyRoom))
                H.checkOut(RoomInd)
            else:
                print("Invalid input")
        else:
            print('Not Found')
    # if option 3 is chosen, it will do check room
    elif mode == "3":
        RoomInd = int(input("Enter your room index: "))
        if H.getNumofRoom() > RoomInd:
            MyRoom =  H.getRoom(RoomInd)
            print("Room {} has been already occupied.".format(MyRoom))
        else:
            print("No one is in this room.")
    # if option 4 is chosen, it will do revenue.
    elif mode == "4":
        total = H.Revenue(50000,70000)
        print("Total Revenue: {}".format(float(total)))
    # if option 5 is chosen, it will stop running
    elif mode == "5":
        print("Goodbye")
        break
