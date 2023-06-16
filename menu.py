#deze file behoort tot de poging om een interface menu te maken
import random
class MainMenu:
    def __init__(self, stations, users, transporter):
        self.stations = stations
        self.users = users
        self.transporter = transporter

    def show(self):
        print("Welcome to the Bike Simulation Program!")
        print("Choose an option:")
        print("1. Automatic simulation")
        print("2. Manual simulation")
        print("3. Exit")

    def get_choice(self):
        return input("Choice: ")

    def user_menu(self):
        print("Choose an option:")
        print("1. Borrow a bike")
        print("2. Return a bike")

    def borrow_bike(self):
        print("Borrow a bike")
        print("Borrow a bike")
        user = self.users[int(input("Enter user index: "))]

        if len(user.bike) == 0:
            if len(self.stations) > 0:
                random_station = random.choice(self.stations)
                if len(random_station.bikes) > 0:
                    random_bike = random_station.bikes[0]
                    random_station.remove_bike(user)
                    user.bike.append(random_bike)
                    print(f"Bike {random_bike.id} in slot {random_bike.slot} has been borrowed by {user.name}.")
                else:
                    print("No available bikes to borrow.")
            else:
                print("No stations available.")
        else:
            print(f"User {user.name} already has a bike.")

    def return_bike(self):
        print("Return a bike")
        user = self.users[int(input("Enter user index: "))]

        if len(user.bike) > 0:
            bike = user.bike[0]
            user.bike.remove(bike)
            if len(self.stations) > 0:
                random_station = random.choice(self.stations)
                random_station.return_bike(user, bike)
                print(f"Bike {bike.id} has been returned to Station {random_station.name}.")
            else:
                print("No stations available to return the bike.")
        else:
            print(f"User {user.name} does not have a bike.")

    async def automatic_simulation(self, versnelling_factor):
        for user in self.users:
            await self.simulate_user(user)

        await self.transporter_task(self.transporter, self.stations)
