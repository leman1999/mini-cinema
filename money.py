from movie import Movie
class Money:
    def __init__(self,current_money):
        self.current_money=current_money

    def get_money(self):
       return (f"current money: {self.current_money}")
    
    def set_money(self, film):
        if self.current_money>int(film.price):
            a=self.current_money-int(film.price)
            return (f"You can buy a ticket:\n\nYour remaining money:{a}")
        else:
            return ("There is no required amount for this film")