from abc import ABC, abstractmethod
class Payment(ABC):
    def source(self):
        print("Scanner/upiid/mobilenumber")
    def amount(self):
        print("enter a amount")
    def bank(self):
        print("choose your bank")
    def pin(self):
        print("enter a pin")
    @abstractmethod
    def  paymentprocess(self):
        pass
    def paymentstatus(self):
        print("show the payment status success/fail")
class HDFC(Payment):
    def paymentprocess(self):
        print("payment is process through hdfc")
class ICIC(Payment):
    def paymentprocess(self):
        print("payment is process through IcIc")
class Union(Payment):
    def paymentprocess(self):
        print("payment is process through union")
class Axis(Payment):
    def paymentprocess(self):
        print("payment is process through axis")
Lakshmi=HDFC()
Lakshmi.source()
Lakshmi.amount()
Lakshmi.bank()
Lakshmi.pin()
Lakshmi.paymentstatus()

sadhana=ICIC()
sadhana.source()
sadhana.amount()
sadhana.bank()
sadhana.pin()
sadhana.paymentstatus()
vishnu=Union()
vishnu.source()
vishnu.amount()
vishnu.bank()
vishnu.pin()
vishnu.paymentstatus()
baji=Axis()
baji.source()
baji.amount()
baji.bank()
baji.pin()
baji.paymentstatus()


    