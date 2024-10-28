import tkinter as tk
from tkinter import messagebox
from db_functions import *

# Function to view existing reservations
def display_reservations():
    reservations = view_reservations()
    display_text = ""
    for res in reservations:
        display_text += f"ID: {res[0]}, Driver: {res[1]}, Car: {res[2]}, Check-Out: {res[3]}, Return: {res[4]}\n"
    messagebox.showinfo("Reservations", display_text)

# Function to view cars and their rates
def display_car_rates():
    car_rates = view_car_rates()
    display_text = ""
    for car in car_rates:
        display_text += f"Car: {car[0]}, Rate: {car[1]}\n"
    messagebox.showinfo("Car Rates", display_text)


# Function to change the modify the car rate
def change_car_rate():
    car_type = entry_change_car_type.get()
    new_rate = entry_new_rate.get()

    if car_type and new_rate:
        try:
            new_rate = float(new_rate)  # Convert rate to float
            result = update_car_rate(car_type, new_rate)
            messagebox.showinfo("Update Status", result)
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid numeric rate.")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

# GUI Setup
root = tk.Tk()
root.title("Car Rental Admin Interface")

# View Car Rates Button
btn_view_reservations = tk.Button(root, text="View Car Rates", command=display_car_rates)
btn_view_reservations.pack()

# View Reservations Button
btn_view_reservations = tk.Button(root, text="View Reservations", command=display_reservations)
btn_view_reservations.pack()


# Labels and Entry Widgets for Changing Car Rate
label_change_car_type = tk.Label(root, text="Car Type to Update Rate")
label_change_car_type.pack()
entry_change_car_type = tk.Entry(root)  # Ensure this is defined here
entry_change_car_type.pack()

label_new_rate = tk.Label(root, text="New Rate Per Day")
label_new_rate.pack()
entry_new_rate = tk.Entry(root)  # Ensure this is defined here
entry_new_rate.pack()

# Update Rate Button
btn_change_rate = tk.Button(root, text="Update Car Rate", command=change_car_rate)
btn_change_rate.pack()

root.mainloop()
