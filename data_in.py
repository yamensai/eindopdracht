import json
from classes import Station
from classes import *

class velo():
    def __init__(self):
        self.users={}
        self.bikes={} # bikes of terwijl aan een user of aan een slot
        self.stations={}# bevat verschillende slot objecten
        self.transporters={}
    def __str__(self):
        for station in self.stations:
            return f"Station: {station}\nLocation: {station}"
    def add_user(self,id,name,surname):
        new=User(id,name,surname)
        self.users[len(self.users)+1]=new
        return new
    def add_bike(self,id,slot,user_id):
        new=Bike(id,slot,user_id)
        self.bikes[len(self.bikes)+1]=new
        return new
    def add_station(self,id,name,location, capacity):
        new=Station(id,name,location,capacity)
        self.stations[len(self.stations)+1]=new
        return new
    def add_transporter(self,name,surname,truck):

        new=Transporter(name,surname,truck)
        self.transporters[len(self.transporters)+1]=new
        return new
        """"def load_station(self):
        stations = []
        with open("velo.geojson","r") as f:
            velo_data = json.load(f)
        for station_new in velo_data["features"]:
            new= self.add_station(id=station_new["properties"]["OBJECTID"],
                                  name=station_new["properties"]["Straatnaam"],
                                  location=station_new["properties"]["Postcode"],
                                  capacity=station_new["properties"]["Aantal_plaatsen"])
            stations.append(station_new)
            print("Added station:", new.name)
            print(new.name)
         """
    def load_stations(self):
        stations = []
        try:
             with open("velo.geojson", "r") as f:
                velo_data = json.load(f)
        except Exception as e:
            print("Error loading JSON file:", str(e))
            return stations

        for station_new in velo_data.get("features", []):
            station = Station(
                id=station_new["properties"].get("OBJECTID"),
                name=station_new["properties"].get("Straatnaam"),
                location=station_new["properties"].get("Postcode"),
                capacity=station_new["properties"].get("Aantal_plaatsen")
            )
            stations.append(station)
            #print("Added station:", station.name)

        return stations
            

