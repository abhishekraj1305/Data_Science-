#WRP rite a class Train Which Has Method To Book A ticket, Get Status (No. of seats Available, Booked, etc), And Can Get The Fare Information Of The Train. Also, Create An Object Of The Train Class And Call The Methods To Book A Ticket, Get Status, And Get Fare Information.
from random import randint

class Train:
    
    def __init__(self, name, total_seats, fare,trainNo):
        self.name = name
        self.total_seats = total_seats
        self.fare = fare
        self.booked_seats = 0
        self.trainNo = randint(169850, 768946)  # Generate a random train number
        
    def book_ticket(self, from_station, to_station):
        self.booked_seats += 1
        print(f"Booking a ticket for train no {self.trainNo} ,{self.name} from {from_station} to {to_station}.")
            
    def get_status(self, from_station, to_station ):
        print(f"train no {self.trainNo} is running from {from_station} to {to_station} and has {self.total_seats - self.booked_seats} seats available, {self.booked_seats} seats booked.")
        
    def get_fare_info(self, from_station, to_station):
        print(f"The fare for train {self.name} number {self.trainNo} from {from_station} to {to_station} is: {self.fare}")
        
train1 = Train("Express", 100, 500, 169850)
train1.book_ticket("Delhi", "Mumbai")
train1.get_status("Delhi", "Mumbai")
train1.get_fare_info("Delhi", "Mumbai")

train2 = Train("Superfast", 150, 800, 768946)
train2.book_ticket("Chennai", "Bangalore")
train2.get_status("Chennai", "Bangalore")
train2.get_fare_info("Chennai", "Bangalore")

train3 = Train("Rajdhani", 200, 1200, 456789)
train3.book_ticket("Kolkata", "Delhi")
train3.get_status("Kolkata", "Delhi")
train3.get_fare_info("Kolkata", "Delhi")


