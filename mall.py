from datetime import datetime
class Mall():
    def __init__(self,location,floor,hallcount) :
        self.location=location
        self.floor =floor
        self.hallcount=hallcount
    
    def working_time(self):
        now=datetime.now()
        current_time= now.hour
        open=now.replace(hour=10)
        close=now.replace(hour=23)
        if open.hour<=current_time<close.hour:
            print("open")
            print("-------------")
        else:
            print("close")
            print("-------------")
            exit
    def person_age(self,age):
        if age>14:
            return "You can continue"
        else:
            exit("You can't enter")

    def vaksinasiya(self,vaksin):
        if vaksin=="Yes":
            return "You can continue" 
        else:
            exit()

    def information(self):
       print("---------------")
       print(f"Mall information:\n\nLocation: {self.location}\nFloor: {self.floor}\nHallcount: {self.hallcount}")
       print("---------------")


class Gencemall(Mall):
    def __init__(self, location, floor, hallcount):
        super().__init__(location, floor, hallcount)
    
class Genclikmall(Mall):
    def __init__(self, location, floor, hallcount):
         super().__init__(location, floor, hallcount)
   
class Denizmall(Mall):
    def __init__(self, location, floor, hallcount):
        super().__init__(location, floor, hallcount)
 
class  Iyirmisekkizmall(Mall):
    def __init__(self, location, floor, hallcount):
        super().__init__(location, floor, hallcount)
 

class  Aygunmall(Mall):
    def __init__(self, location, floor, hallcount):
        super().__init__(location, floor, hallcount)