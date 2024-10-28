from datetime import datetime
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('rentals.db')
cursor = connection.cursor()

def create_reservation(driver_name, car_type, check_out, return_time):
    """Create a new reservation for a vehicle."""
    # Convert string dates to datetime objects for comparison
    check_out_time = datetime.strptime(check_out, "%Y-%m-%d %H:%M")
    return_time = datetime.strptime(return_time, "%Y-%m-%d %H:%M")

    # Ensure the reservation is made at least 24 hours in advance
    if (check_out_time - datetime.now()).total_seconds() < 86400:
        return "Error: Reservation must be made at least 24 hours in advance."

    # Calculate the number of days the vehicle is rented
    days_rented = (return_time - check_out_time).days

    # Retrieve the daily rental rate for the selected car type
    cursor.execute("SELECT rate_per_day FROM Cars WHERE car_type = ?", (car_type,))
    rate_result = cursor.fetchone()

    # Get rate of car for calculating cost
    rate = rate_result[0]
    total_cost = rate * days_rented  # Calculate total cost

    # Apply discount if days rented is 7 or more
    discount = 0
    if days_rented >= 7:
        discount = total_cost * 0.10  # Apply a 10% discount
        total_cost -= discount  # Subtract the discount from total cost

    # Check if the selected car type is available
    cursor.execute("SELECT available FROM Cars WHERE car_type = ? AND available = 1", (car_type,))
    if cursor.fetchone() is None:
        return "Error: No available cars of the selected type."

    # Check for overlapping reservations
    cursor.execute('''
            SELECT * FROM Reservations
            WHERE car_type = ? AND (
                (check_out <= ? AND return_time >= ?) OR
                (check_out <= ? AND return_time >= ?)
            )
        ''', (car_type, return_time, return_time, check_out, check_out))

    overlapping_reservations = cursor.fetchall()
    if overlapping_reservations:
        return "Error: This car type is already reserved during that time."

    # Insert the reservation into the Reservations table
    cursor.execute('''INSERT INTO Reservations(driver_name, car_type, check_out, return_time)
                      VALUES (?, ?, ?, ?)''', (driver_name, car_type, check_out, return_time))
    connection.commit()
    return f"Reservation created successfully! Total cost: ${total_cost:.2f}"

def view_reservations():
    # Get all reservations
    cursor.execute("SELECT * FROM Reservations")
    reservations = cursor.fetchall()
    return reservations

def request_extension(reservation_id, new_return_time):
    # Check if extension is possible (no conflicting reservations)
    cursor.execute("SELECT car_type, return_time FROM Reservations WHERE reservation_id = ?", (reservation_id,))
    result = cursor.fetchone()
    if not result:
        return "Reservation not found."

    car_type, current_return_time = result
    cursor.execute('''SELECT * FROM Reservations 
                      WHERE car_type = ? AND check_out < ? AND return_time > ?''',
                   (car_type, new_return_time, current_return_time))

    if cursor.fetchone():
        return "Error: Extension denied due to another reservation."

    # Update reservation with the new return time
    cursor.execute("UPDATE Reservations SET return_time = ?, extension_requested = 1 WHERE reservation_id = ?",
                   (new_return_time, reservation_id))
    connection.commit()
    return "Extension granted successfully!"

def update_car_rate(car_type, new_rate):
    # Check if the car type exists
    cursor.execute("SELECT * FROM Cars WHERE car_type = ?", (car_type,))
    if cursor.fetchone() is None:
        return "Error: Car type does not exist."

    # Update the rate for the specified car type
    cursor.execute("UPDATE Cars SET rate_per_day = ? WHERE car_type = ?", (new_rate, car_type))
    connection.commit()
    return "Car rate updated successfully!"
def view_car_rates():
    # Get all Cars and their Rates
    cursor.execute("SELECT car_type, rate_per_day FROM Cars")
    carRates = cursor.fetchall()
    return carRates



