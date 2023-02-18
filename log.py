import backend as db

def reader(path):
    directory = "C:/Users/Erik/Desktop/Audi/"
    with open(directory + path, "r") as f:
        content = f.read().split("\n")

        # Every other header starting index 1 is time stamp
        headers = content[5].split(",")[2:][::2]

        # Chop off leading and trailing comma 
        data = content[7:-1]

        # Tag the current session
        sessionID = db.most_recent_session()

        # Loop through all data 
        for record in data:
            line = record.split(",")[1:-1]
            times = line[::2]
            sensors = line[1::2]

            for i, sensor in enumerate(sensors):
                print(f"Sensor Name: {headers[i]} Sensor Value: {sensor} Time: {times[i]}")

                db.add_record(sessionID, headers[i], float(sensor), times[i])

try:
    db.start_engine()
    reader("session3.csv")
finally:
    db.stop_engine()
