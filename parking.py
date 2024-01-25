class ParkingGarage():

    """First we will define our attributes
    
    tickets --> list
    parkingSpaces --> list
    currentTicket --> dictionary
    
    """

    def __init__(self, tickets, parkingSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = {}

#We will take a ticket for a parking spot

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop()
            self.parkingSpaces.pop()
            self.currentTicket[ticket] = {'paid': False}
            print(f"{ticket} ticket(s) issued. Parking has been assigned")
    
    def payForParking(self):
        ticket = input("Enter your ticket(s) number please: ")
        amount = input("Please select an amount to pay for your ticket: ")
        if ticket in self.currentTicket and not self.currentTicket[ticket]['paid']:
            self.currentTicket[ticket]['paid'] = True
            print(f"Thank you for paying! you have 15 min to leave")
        else: print("Invalid ticket number, please try again")

    def leaveGarage(self):
        ticket = input("Enter your ticket(s) number please: ")
        if ticket in self.currentTicket:
            if self.currentTicket[ticket]['paid']:
                print("Thank you! Enjoy your day!")
                self.parkingSpaces.append(ticket)
                self.tickets.append(ticket)
            else:
                print("Payment is required to leave")
        else:
            print("Incorrect number")
            self.leaveGarage()

tickets = [f"{i}" for i in range(1,11)]
parkingSpaces = [f"{i}" for i in range (1,11)]

garage = ParkingGarage(tickets, parkingSpaces)

garage.takeTicket()
garage.payForParking()
garage.leaveGarage()