import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('climate_data.db')
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS stations")
cursor.execute("DROP TABLE IF EXISTS measurements")

# Create stations table
cursor.execute("""
CREATE TABLE stations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    station TEXT UNIQUE,
    latitude REAL,
    longitude REAL,
    elevation REAL,
    name TEXT,
    country TEXT,
    state TEXT
)
""")

# Create measurements table
cursor.execute("""
CREATE TABLE measurements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    station TEXT,
    date TEXT,
    precip REAL,
    tobs REAL,
    FOREIGN KEY (station) REFERENCES stations(station)
)
""")

# Load data from clean_stations.csv
with open('clean_stations.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO stations (station, latitude, longitude, elevation, name, country, state)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (row['station'], row['latitude'], row['longitude'], row['elevation'], 
              row['name'], row['country'], row['state']))

# Load data from clean_measure.csv
with open('clean_measure.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO measurements (station, date, precip, tobs)
            VALUES (?, ?, ?, ?)
        """, (row['station'], row['date'], row['precip'], row['tobs']))

conn.commit()

print("Database created successfully!")

conn.close()
