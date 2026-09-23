#red bus application
from abc import ABC, abstractmethod
# Parent class
class Redbus:
    bus = {i: "Available" for i in range(1, 11)}
    def displayseats(self):
        print("---------------- XYZ BUS ----------------")
        for i in Redbus.bus:
            print(i, Redbus.bus[i])
    def booking(self, seatno):
        if seatno in Redbus.bus and Redbus.bus[seatno] == "Available":
            Redbus.bus[seatno] = "Booked"
            print(f"Your seat-{seatno} is successfully booked")
        else:
            print(f"Your seat-{seatno} is already booked or invalid")


# Child class
class User(Redbus):
    def __init__(self, name, phono, email):
        self.name = name
        self.phono = phono
        self.email = email
        print(f"Hello {self.name}, welcome to RedBus")

class Driver:

    def __init__(self, name, phno):
        self.__name = name
        self.__phno=phno
    def display_driver_name(self):
        print("Driver Name:", self.__name)
    def display_driver_phno(self):
        print("Driver phno:", self.__phno)

class Payment(ABC):
    def source(self):
        print("Scanner / UPI ID / Mobile Number")
    def amount(self):
        print("Enter an amount")
    def bank(self):
        print("Choose your bank")
    def pin(self):
        print("Enter a PIN")
    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment Status: Success")


class HDFC(Payment):
    def paymentprocess(self):
        print("Payment is processed through HDFC")

class ICIC(Payment):
    def paymentprocess(self):
        print("Payment is processed through ICICI")

class Union(Payment):
    def paymentprocess(self):
        print("Payment is processed through Union Bank")

class Axis(Payment):
    def paymentprocess(self):
        print("Payment is processed through Axis Bank")
# ---------------- MAIN PROGRAM ----------------
# User
lakshmi = User("Lakshmi", 8192087121, "lakshmi@gmail.com")
# Display seats
lakshmi.displayseats()
# Book seat
lakshmi.booking(4)
# Display seats after booking
print("\nSeats after booking:")
lakshmi.displayseats()
# Driver
print("\n------------- DRIVER DETAILS -------------")
d = Driver(
    "xyz",
    "1234567890"
)
# Only driver name is displayed
d.display_driver_name()
d.display_driver_phno()
# Payment
print("\n------------- PAYMENT -------------")
payment = HDFC()
payment.source()
payment.amount()
payment.bank()
payment.pin()
payment.paymentprocess()
payment.paymentstatus()