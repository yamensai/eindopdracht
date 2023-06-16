#volledige simulatie, zonder een menu interface
import asyncio
import time
import random
import pickle
import pickle as pickle_module
import os
from faker import Faker
from classes import *
from data_in import *


STATIONS_FILE = "stations.pickle"
USERS_FILE = "users.pickle"

# stations laden 
def load_data():
    if os.path.exists(STATIONS_FILE):
        with open(STATIONS_FILE, "rb") as f:
            return pickle.load(f)
    else:
        data_instance = velo()
        stations = data_instance.load_stations()

        # fietsen toevoegen aan stations
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

    # fietsen toevoegen aan stations
    for station in stations:
        for i in range(1, station.capacity // 2 + 1):
            station.add_bike(Bike(i, i), i)

    return stations

def main():
    stations = load_data()
    users = create_users()
    versnelling_factor = float(input("Hoe snel wil je gaan? Geef de versnellingfactor in: "))
    mrtrans = Transporter(-1)

    asyncio.run(simulation(users, stations, versnelling_factor, mrtrans))

    # de stations opslaan
    save_data(stations)

async def simulate_user(user, stations, versnelling_factor):
    station_count = len(stations)
    while True:
        current_station = random.choice(stations)  # kies een random fiets

        # de gebruiker verwijdert de fiets van het station
        current_station.remove_bike(user)
        print(f"User {user.name} removed bike from Station {current_station.name}")

        await asyncio.sleep(random.uniform(1, 30) / versnelling_factor)

        destination_station = random.choice(stations)
        while destination_station == current_station:
            destination_station = random.choice(stations)  # en een andere station kiezen

        destination_station.return_bike(user, user.bike[0])
        print(f"User {user.name} returned bike to Station {destination_station.name}")
        await asyncio.sleep(random.uniform(1, 30) / versnelling_factor)

async def transporter_task(transporter, stations,versnelling_factor):
    for _ in range(10):
        await asyncio.sleep(60/versnelling_factor)  # wacht een minuut

        station_index = random.randint(0, len(stations) - 1)
        station = stations[station_index]

        station.onderhoud_open(transporter)
        time.sleep(random.uniform(1, 10))
        station.remove_bike(transporter, len(station.bikes) // 4)  # neem 1/4de van de fietsen
        time.sleep(random.uniform(1, 10))
        station.onderhoud_sluiten(transporter)

        await asyncio.sleep(40/versnelling_factor)  # wacht 40 seconden

        destination_index = random.randint(0, len(stations) - 1)
        while destination_index == station_index:
            destination_index = random.randint(0, len(stations) - 1)
        destination_station = stations[destination_index]

        open_slots = sum(destination_station.open_slots)
        return_bike_count = open_slots // 3  # zet fietsen terug op basis van 1/3de van de open slots
        transporter.return_bike_to_station(destination_station, return_bike_count)
        destination_station.return_bike(transporter, return_bike_count)

async def simulation(users, stations, versnelling_factor, transporter):
    user_tasks = [simulate_user(user, stations, versnelling_factor) for user in users]
    tasks = user_tasks + [transporter_task(transporter, stations,versnelling_factor)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    main()
