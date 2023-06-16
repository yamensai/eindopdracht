#Ik probeerde hier een interface te maken maar dat lukte niet helaas
import asyncio
import random
from faker import Faker
import time
from classes import Transporter,User
from program import MainMenu, load_data, save_data



async def transporter_task(self, mrtrans, stations):
    for _ in range(10):
        await asyncio.sleep(60 / self.versnelling_factor)

        station_index = random.randint(0, len(stations) - 1)
        station = stations[station_index]

        station.onderhoud_open(mrtrans)
        time.sleep(random.uniform(1, 10))
        station.remove_bike(mrtrans, len(station.bikes) // 4)
        time.sleep(random.uniform(1, 10))
        station.onderhoud_sluiten(mrtrans)

        await asyncio.sleep(40 / self.versnelling_factor)

        destination_index = random.randint(0, len(stations) - 1)
        while destination_index == station_index:
            destination_index = random.randint(0, len(stations) - 1)
        destination_station = stations[destination_index]

        open_slots = sum(destination_station.open_slots)
        return_bike_count = open_slots // 3
        mrtrans.return_bike_to_station(destination_station, return_bike_count)
        destination_station.return_bike(mrtrans, return_bike_count)

def create_users():
    users = []
    fake = Faker()
    for _ in range(10):
        name = fake.name()
        user = User(name)
        users.append(user)
    return users


def main():
    stations = load_data()
    users = create_users()
    mrtrans = Transporter(-1)

    while True:
        menu = MainMenu(stations, users, mrtrans)
        menu.show()

        choice = menu.get_choice()

        if choice == "1":
            versnelling_factor = float(input("Enter the speed factor: "))
            asyncio.run(menu.automatic_simulation(versnelling_factor))
        elif choice == "2":
            menu.user_menu()
            user_choice = menu.get_choice()

            if user_choice == "1":
                menu.borrow_bike()
            elif user_choice == "2":
                menu.return_bike()
        elif choice == "3":
            break

    save_data(stations)


if __name__ == "__main__":
    main()