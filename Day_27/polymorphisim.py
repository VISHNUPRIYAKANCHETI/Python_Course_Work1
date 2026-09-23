class hotstar:
    def __init__(self,name):
        print(f"welcome to the hotstar,{name}----------------")
    def login(self):
        print("login the hotstar")
    def dashboard(self):
        print("you have home page")
    def search(self):
        print("you can search a movie or webseries")
    def histroy(self):
        print("you can see your history")
    def playcontrollers(self):
        print("you can resume the video")
    def download(self):
        print("you can't down load the video")
    def device(self):
        print("Limited access for login")
    def adds(self):
        print("adds will be  run ")
    def quality(self):
        print("limited quality")
class premimumhotstar(hotstar):
    def __init__(self,name):
        print(f"welcome to the hotstar,{name}----------------")
    def login(self):
        print("login the hotstar")
    def dashboard(self):
        print("you have home page")
    def search(self):
        print("you can search a movie or webseries")
    def histroy(self):
        print("you can see your history")
    def playcontrollers(self):
        print("you can resume the video")
    def download(self):
        print("you can down load the video")
    def device(self):
        print(" no Limited access for login")
    def quality(self):
        print("Hd quality")
    def adds(self):
        print("limited adds")
lakshmi=hotstar('lakshmi')
lakshmi.login()
lakshmi.dashboard()
lakshmi.histroy()
lakshmi.download()
lakshmi.playcontrollers()
lakshmi.adds()
lakshmi.search()
lakshmi.device()
lakshmi.quality()
sadhana=premimumhotstar("sadhana")
sadhana.login()
sadhana.dashboard()
sadhana.histroy()
sadhana.download()
sadhana.playcontrollers()
sadhana.adds()
sadhana.search()
sadhana.device()
sadhana.quality()