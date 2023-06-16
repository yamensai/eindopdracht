#deze file behoort tot de poging om een interface menu te maken
import asyncio
import time
import random
import pickle
import pickle as pickle_module
import os
from faker import Faker
from classes import *
from data_in import *
from interface import MainMenu
STATIONS_FILE = "stations.pickle"
USERS_FILE = "users.pickle"

# Load stations and users from files or create new ones
def load_data():
    if os.path.exists(STATIONS_FILE):
        with open(STATIONS_FILE, "rb") as f:
            return pickle.load(f)
    else:
        data_instance = velo()
        stations = data_instance.load_stations()

        # Add bikes to stations
        for station in stations:
            for i in range(1, station.capacity // 2 + 1):
                station.add_bike(Bike(i, i), i)
        
        save_data(stations)
        return stations

def save_data(stations):
    with open(STATIONS_FILE, "wb") as f:
        pickle_module.dump(stations, f)

def create_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "rb") as f:
            return pickle_module.load(f)
    else:
        fake = Faker()
        users = []
        for i in range(1, 101):
            name = fake.first_name()
            surname = fake.last_name()
            user = User(id=i, name=name, surname=surname)
            users.append(user)

        with open(USERS_FILE, "wb") as f:
            pickle_module.dump(users, f)
        return users

def create_new_stations():
    data_instance = velo()
    stations = data_instance.load_stations()

    # Add bikes to stations
    for station in stations:
        for i in range(1, station.capacity // 2 + 1):
            station.add_bike(Bike(i, i), i)

    return stations

def main():
    stations = load_data()
    users = create_users()
    mrtrans = Transporter(-1)
    versnelling_factor = 0.0

    while True:
        menu = MainMenu(stations, users, versnelling_factor, mrtrans)
        menu.show()

        choice = menu.get_choice()

        if choice == "1":
            versnelling_factor = float(input("Hoe snel wil je gaan? Geef de versnellingfactor in: "))
            asyncio.run(menu.automatic_simulation(versnelling_factor))
        elif choice == "2":
            menu.user_type_menu()
            user_type_choice = menu.get_choice()

            if user_type_choice == "1":
                menu.user_menu()
                user_choice = menu.get_choice()

                if user_choice == "1":
                    user = None
                    while user is None:
                        user_id = int(input("Enter user ID: "))
                        for u in users:
                            if u.id == user_id:
                                user = u
                                break
                        else:
                            print("Invalid user ID. Please try again.")

                    menu.borrow_bike(user)
                elif user_choice == "2":
                    menu.return_bike()
            elif user_type_choice == "2":
                asyncio.run(menu.transporter_simulation())
        elif choice == "3":
            break

    # Save the updated stations data
    save_data(stations)


if __name__ == "__main__":
    main()
