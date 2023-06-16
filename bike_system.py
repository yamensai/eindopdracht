from classes import *
class station_function():
    #beter andere naam
    #def add_bike_in(self,new_bike:Bike):
    #    for individual in new_bike:
    #        for bike in self.bikes:
    #            if bike['bike'] is None:
    #                bike['bike'] = individual
    #                self.empty_space -=1
    #                break


    def borrow_bike(self,user:User| Transporter):
        if not( type(user) == User or type(user) ==Transporter):
            raise Exception("Alleen een user of een transporter kan een fiets lenen.")
        if type(user)==User:
            if user.bike is not None:
                print("U hebt al een fiets ontleend")
                return
            if self.empty_space== self.capacity:
                print("Dit station is leeg!")
                return
    def return_bike(self, user:User|Transporter):
        if not(type(user)==User or type(user) ==Transporter):
            raise Exception(" Alleen een user of een transporter kan een fiets lenen.")
        if self.empty_space ==0:
            print("Dit station is vol.")
            return
        
        for bike in self.bikes:
            if bike['bike'] is None:
                if type(user,User):
                    bike ['bike'] = user.bike
                    user.bike=None
                    print(f"\t Geachte {user.name}, uw fiets werd correct teruggeplaatst")
                self.empty_space -=1
                return


 