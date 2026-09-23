#single inheritance: One child class inherits from one parent class.
'''class whatsappv1:
    def message(self):
        print("you can a send a msg")
class whatsappv2(whatsappv1):
    def status(self):
        print("you can upolad your status for 24hrs")
lakshmi=whatsappv1()
lakshmi.message()
rama=whatsappv2()
rama.message()
rama.status()'''
#multi level inheritance:   A class inherits from another child class, forming a chain.
'''
class whatsappv1:
    def message(self):
        print("you can a send a msg")
class whatsappv2(whatsappv1):
    def status(self):
        print("you can upolad your status for 24hrs")
class whatsappv3(whatsappv2):
    def calls(self):
        print("you can call from whatsapp")

lakshmi=whatsappv1()
lakshmi.message()
rama=whatsappv2()
rama.message()
rama.status()
jyothi=whatsappv3()
jyothi.calls()
jyothi.message()
jyothi.status() '''
#multiple inheritance : One child class inherits from more than one parent class.
'''class whatsappv1:
    def message(self):
        print("you can a send a msg")
class whatsappv2:
    def status(self):
        print("you can upolad your status for 24hrs")
class whatsappv3(whatsappv1, whatsappv2):
    def calls(self):
        print("you can call from whatsapp")


jyothi=whatsappv3()
jyothi.calls()
jyothi.message()
jyothi.status()'''

# Hybrid inheritance  A combination of two or more types of inheritance.
'''class whatsappv1:
    def message(self):
        print("you can a send a msg")
class whatsappv2(whatsappv1):
    def status(self):
        print("you can upolad your status for 24hrs")
class whatsappv3:
    def calls(self):
        print("you can call from whatsapp")
class whatsappv4:
    def groups(self):
        print("in grp we number of people we can chat at a time with all")
class whatsappv5(whatsappv4,whatsappv3,whatsappv2):
    def channel(self):
        print("post anything there are in hug crowd")


vishnu=whatsappv5()
vishnu.calls()
vishnu.message()
vishnu.status()
vishnu.groups()
vishnu.channel()'''
#herirical inheritance: Multiple child classes inherit from the same parent class
class whatsappv1:
    def message(self):
        print("you can a send a msg")
class whatsappv2(whatsappv1):
    def status(self):
        print("you can upolad your status for 24hrs")
class whatsappv3(whatsappv1):
    def calls(self):
        print("you can call from whatsapp")

lakshmi=whatsappv1()
lakshmi.message()
rama=whatsappv2()
rama.message()
rama.status()
jyothi=whatsappv3()
jyothi.calls()
jyothi.message()




