class Flipkart:
    discount=30

    @classmethod
    def updatediscount(cls):
        cls.discount=40
        print("Updated Discount:",cls.discount)

    def info(self,name,phoneno,address):
        self.name=name
        self.phoneno=phoneno
        self.address=address
        print(f'Welcome to the Flipkart',self.name)
    @staticmethod
    def banner():
        print(f'{Flipkart.discount}% discount is going, grab the products')

vishnu=Flipkart()
vishnu.info('vishnu',9876543210,'Vjwd')
vishnu.updatediscount()
vishnu.banner()
lakshmi=Flipkart()
lakshmi.info('lakshmi',9876543210,'Bang')
lakshmi.updatediscount()
lakshmi.banner()
sadhana=Flipkart()
sadhana.info('sadhana',9876543210,'Hyd')
sadhana.updatediscount()
sadhana.banner()