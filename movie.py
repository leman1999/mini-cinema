class Hours:
    def __init__(self,starttime,endtime):
        self.starttime=starttime
        self.endtime=endtime

class Movie:
     def __init__(self,name,director,year,genre,duration,imdb,hours,price):
         self.year=year
         self.duration=duration
         self.imdb=imdb
         self.price=price
         self.hours=hours
         self.name=name
         self.director=director
         self.genre=genre
        
        
         
     def show_info(self):
         hours = []
         for i in self.hours:
             dic={
                 "start time":i.starttime,
                 "end time":i.endtime,
             }
             hours.append(dic)
             
         return (f"Movie information:\n\nName:{self.name}\nDirector:{self.director}\nYear:{self.year}\nGenre:{self.genre}\nDuration:{self.duration}\nImdb:{self.imdb}\nHours:{hours}\nPrice:{self.price}")
     
             
         
         
             
                 
                  
        
             
         
     def year_info(self):
         if self.year<2000:
             print("Year:Old category")
         else:
             print("Year:New category")
             exit
            
     def duration_info(self):
         if self.duration<120:
             print("Duration:Short movie")
         else:
             print("Duration:Long movie")
             exit
        
     def rating_info(self):
         if self.imdb<6:
             print("imdb:E")
         elif 6<self.imdb<7:
             print("imdb:D")
         elif 7<self.imdb<8:
             print("imdb:C")
         elif 8<self.imdb<9:
             print("imdb:B")
         elif 9<self.imdb<10:
             print("imdb:A")
         else:
             print("imdb:Not found")
             exit
     
             
class Ghajini(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)  
class Ayla(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)
class Suzume(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)    
class Spidarman(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)
class VeerZaara(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)
class DDLJ(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)
class Fanaa(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)
class Peekay(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)
class  Threeidiots(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)
class Devdas(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)

