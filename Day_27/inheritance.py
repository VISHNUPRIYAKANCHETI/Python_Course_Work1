'''class whatsappv1:
    def status(self):
        print("you can upolad your status for 24hrs")
class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("add music and react the status")
a=whatsappv1()
a.status()
b=whatsappv2()
b.status()'''
class whatsappv1:
    def status(self):
        print("you can upolad your status for 24hrs")
class whatsappv2:
    def status(self):
        print("add music and react the status")
class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("you can remention the status")
a=whatsappv3()
a.status()