import random
"""class Slot:
   def __init__(self):
        self.bike = None
    
   def is_empty(self):
        return self.bike is None
    
   def add_bike(self, bike):
        self.bike = bike
"""
class Bike:
    def __init__(self, id,slot):
        self.id = id
        self.slot =slot

class User:
    def __init__(self, id,name, surname):
        self.id=id
        self.name = name
        self.surname = surname
        self.bike = []
    def __str__(self) -> str:
        bike_test = [bike.id for bike in self.bike]
        return f"ik heb fiets(en) met ID(s) {bike_test}"

class Transporter(User):
    def __init__(self, id):
        super().__init__(id, "Trans", "Porter")
    def return_bike_to_station(self, user, bike, n=1):
        if user.id < 0:
            if n > len(self.open_slots):
                print("Je kan je fiets hier niet terugzetten, Mr. Trans!")
            else:
                for _ in range(n):        
                    slot_transporteur = random.choice(self.open_slots)
                    print(f"Je kan je fiets in slot {slot_transporteur} terugzetten")
                    if bike in user.bike:
                        if len(self.open_slots) > 0:
                            self.open_slots.remove(slot_transporteur)
                            self.bikes.append(bike)
                            user.bike.remove(bike)
                            print(f"Fiets {bike.id} is teruggebracht naar het station.")
                            return
                        print("Er zijn geen beschikbare slots om de fiets terug te zetten.")
class Station:
    def __init__(self,id, name, location, capacity):
        self.id = id
        self.name = name
        self.location = location
        self.capacity = capacity
        self.empty_space=capacity
        self.bikes = []
        self.open_slots = list(range(self.capacity))
        # wanneer je fiets leent voeg de slot van die fiets toe in lijst van open slots, als er een fiets in dat slot geplaats wordt dan, haal die slot uit de lijst
    def __str__(self):
        bike_test = [bike.id for bike in self.bikes]
        return f"Station: {self.name}\nLocation: {self.location}\nBike: {bike_test}\nSloten die open zijn: {self.open_slots}"
    def add_bike(self, new_bike: Bike, slot):
        if self.empty_space > 0:
            self.bikes.append(new_bike)
            self.empty_space -= 1
            if slot in self.open_slots:
                self.open_slots.remove(slot)
            else:
                print("Slot is not available.")
        else:
            print("Het station is vol. Kan geen fiets toevoegen.")
        # station kan vol zijn, check eerst of station plaats heeft en geef info met print
    def remove_bike(self, user, n=1):
        if user.id < 0:
            if n > len(self.bikes):
                print("We have no bikes for you, Mr. Trans!")
            else:
                for _ in range(n):
                    random_velo = random.choice(self.bikes)
                    self.bikes.remove(random_velo)
                    user.bike.append(random_velo)
                    print(f"Fiets met id {random_velo.id} aan transporter")
        else:
            if len(self.bikes) > 0:
                random_velo = random.choice(self.bikes)
                self.open_slots.append(random_velo.slot)
                self.bikes.remove(random_velo)
                user.bike.append(random_velo)
                print(f"Fiets {random_velo.id} in slotnummer {random_velo.slot} is uitgeleend aan {user.name}.")
            else:
                print("Er zijn geen beschikbare slots om een fiets te lenen.")
    def return_bike(self, user, bike, n=1):
        if user.id < 0:
            if n > len(self.open_slots):
                print("Je kan je fiets hier niet terugzetten, Mr. Trans!")
            else:
                for _ in range(n):        
                    slot_transporteur = random.choice(self.open_slots)
                    print(f"Je kan je fiets in slot {slot_transporteur} terugzetten")
                    if bike in user.bike:
                        if len(self.open_slots) > 0:
                            self.add_bike(bike, slot_transporteur)
                            self.bikes.append(bike)
                            self.empty_space += 1
                            user.bike.remove(bike)
                            print(f"Fiets {bike.id} is teruggebracht naar het station.")
                            return
                        print("Er zijn geen beschikbare slots om de fiets terug te zetten.")
    
        else:
            slot = random.choice(self.open_slots)
            print(f"Je kan je fiets in slot {slot} terugzetten")
        
            if bike in user.bike:
                if len(self.open_slots) > 0:
                    self.add_bike(bike, slot)
                    self.bikes.append(bike)
                    self.empty_space += 1
                    user.bike.remove(bike)
                    print(f"Fiets {bike.id} is teruggebracht naar het station.")
                    return
                print("Er zijn geen beschikbare slots om de fiets terug te brengen.")
            else:
                print(f"Gebruiker {user.name} heeft geen fiets met ID {bike.id}.")       
        
        #1. variable van een fiets die weg gedaan moet worden
        #2. deze fiets uit lijst halen
        # pak de fiets die geselecteerd is
    def onderhoud_open(self, user):
        if (user.id<0):
            self.open_slots = list(range(self.capacity))
            print("Onderhoudsmodus geactiveerd. Alle beschikbare slots zijn geopend.")
        else:
            print('jij  bent geen transporter')
    def onderhoud_sluiten(self,user):
        if (user.id<0):
            for bike in self.bikes:
                if bike.slot in self.open_slots:
                    self.open_slots.remove(bike.slot)
                    print(f"slot {bike.slot} werd dicht gedaan aangezien dat daar een fiets is")
        else:
            print('jij  bent geen transporter')


    # voeg functie toe zodat user scant -> fiets uitlenen en in self.bikes van user zetten


    #