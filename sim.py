from program import *
import asyncio
import time
versnelling_factor = int(input("hoe snel wil je gaan?"))

"""def progess_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '+' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}|{percent:.2f}%", end="\r")
"""
async def vis():
    for _ in range(1000):
        progess_bar(len(Station1.bikes), Station1.capacity)

async def user_1(user, station1, station2,station3):
    for _ in range(1000):
        station1.remove_bike(user)
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station2.return_bike(user, user.bike[0])
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station2.remove_bike(user)
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station3.return_bike(user, user.bike[0])
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station3.remove_bike(user)
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station2.return_bike(user, user.bike[0])
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
async def user_2(user, station1, station2,station3):
    for _ in range(1000):
        station2.remove_bike(user)
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station3.return_bike(user, user.bike[0])
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station3.remove_bike(user)
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station2.return_bike(user, user.bike[0])
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station2.remove_bike(user)
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station1.return_bike(user, user.bike[0])
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station1.remove_bike(user)
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station2.return_bike(user, user.bike[0])
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station2.remove_bike(user)
        await asyncio.sleep(random.uniform(1, 10) / versnelling_factor)
        station1.return_bike(user, user.bike[0])
async def trans(user, station1, station2,station3):
    for _ in range(10):
        await asyncio.sleep(60 / versnelling_factor)
        station1.onderhoud_open(user)
        time.sleep(random.uniform(1, 10) / versnelling_factor)
        station1.remove_bike(user, 2)
        time.sleep(random.uniform(1, 10) / versnelling_factor)
        station1.onderhoud_sluiten(user)
        await asyncio.sleep(20 / versnelling_factor)
        station2.return_bike(user,2)
        await asyncio.sleep(60 / versnelling_factor)
        station3.onderhoud_open(user)
        time.sleep(random.uniform(1, 10) / versnelling_factor)
        station3.remove_bike(user, 3)
        time.sleep(random.uniform(1, 10) / versnelling_factor)
        station3.onderhoud_sluiten(user)
        await asyncio.sleep(20 / versnelling_factor)
        station1.return_bike(user,2)
async def call_users():
    await asyncio.gather(user_1(uuser1, Station1, Station2,Station3), user_2(uuser2, Station1, Station2,Station3),trans(mrtrans, Station1, Station2,Station3))

asyncio.run(call_users())
