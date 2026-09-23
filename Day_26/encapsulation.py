class insta:
    def __init__(self, username, password):
        self.username=username
        self.__password=password
        self._post=[]
    def getpassword(self):
        return self.__password
    @property
    def accesspost(self):
        return self._post  
lakshmi=insta('lakshmi','1234')
print(lakshmi.username)
print(lakshmi.getpassword())
print(lakshmi.accesspost)
'''class insta:
    def __init__(self, username, password):
        self.username=username
        self.__password=password
        self._post=[]
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword  
    @property
    def accesspost(self):
        return self._post
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)  
lakshmi=insta('lakshmi','1234')
print(lakshmi.username)
print(lakshmi.getpassword())
print(lakshmi.accesspost)
lakshmi.username='lakshmi@123'
print(lakshmi.username)
lakshmi.setpassword('lakshmi@123')
print(lakshmi.getpassword())'''