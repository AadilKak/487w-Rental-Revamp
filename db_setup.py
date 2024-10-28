# File to setup SQL Connection
import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('rentals.db')
cursor = conn.cursor()

# Create a table for Cars
cursor.execute('''CREATE TABLE IF NOT EXISTS Cars (
                    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_type TEXT NOT NULL,
                    available BOOLEAN NOT NULL DEFAULT 1,
                    rate_per_day REAL NOT NULL,
                    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
                 )''')

# Create a table for Reservations
cursor.execute('''CREATE TABLE IF NOT EXISTS Reservations (
                    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    driver_name TEXT NOT NULL,
                    car_type TEXT NOT NULL,
                    check_out DATETIME NOT NULL,
                    return_time DATETIME NOT NULL,
                    extension_requested BOOLEAN DEFAULT 0
                 )''')

# Sample vehicle types and their rates (to populate the table for testing)
cars = [('Sedan', 1, 50.0), ('SUV', 1, 75.0), ('Pick-Up', 1, 80.0), ('Van', 1, 90.0)]

# Insert vehicle data into the Vehicles table
cursor.executemany("INSERT INTO Cars (car_type, available, rate_per_day) VALUES (?, ?, ?)", cars)
conn.commit()

print("Database and tables have been successfully set up.")
