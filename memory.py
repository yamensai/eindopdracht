import pickle

STATIONS_FILE = "stations.pickle"
TRANSPORTERS_FILE = "transporters.pickle"
USERS_FILE = "users.pickle"

# Function to save data to files
def save_data():
    with open(STATIONS_FILE, "wb") as f:
        pickle.dump([station.serialize() for station in stations], f)
    with open(TRANSPORTERS_FILE, "wb") as f:
        pickle.dump([transporter.serialize() for transporter in transporters], f)
    with open(USERS_FILE, "wb") as f:
        pickle.dump([user.serialize() for user in users], f)

# Function to load data from files
def load_data():
    if os.path.exists(STATIONS_FILE):
        with open(STATIONS_FILE, "rb") as f:
            station_data = pickle.load(f)
        for data in station_data:
            station = Station.deserialize(data)
            stations.append(station)
    # Repeat the same for other files