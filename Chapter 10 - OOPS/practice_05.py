from random import randint
class Train:
    def __init__(self):
        self.trainNo = 12809

    def bookTicket(self,boarding,dest):
        print(f"The train has beend successfully booked from {boarding} to {dest}")

    def getStatus(self):
        print(f"No of seats available in train no {self.trainNo} are {randint(1,75)}")

    def getFare(self,boarding,dest):
        print(f"Fare for train no {self.trainNo} from {boarding} to {dest} is {randint(2000,2500)} rupees")

ticket = Train()
ticket.bookTicket("Delhi","Mumbai")
ticket.getStatus()
ticket.getFare("Delhi","Mumbai")