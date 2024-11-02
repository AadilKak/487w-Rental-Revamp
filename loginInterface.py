import streamlit as st
from db_functions import create_reservation, view_reservations, view_car_rates, request_extension, update_car_rate

# Function to handle user logout
def logout():
    st.session_state.clear()  # Clear session state
    st.success("You have been logged out.")
    st.markdown("<h3 style='color: black;'>Redirecting to login page...</h3>", unsafe_allow_html=True)
    st.rerun()

# Function for submitting a reservation
def submit_reservation(driver_name, car_type, check_out, return_time):
    if driver_name and car_type and check_out and return_time:
        result = create_reservation(driver_name, car_type, check_out, return_time)
        st.info(f"Reservation Status: {result}")
    else:
        st.warning("Please fill all fields")

# Function to view existing reservations
def display_reservations():
    reservations = view_reservations()
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.markdown("<h4 style='color: black;'>ID</h4>", unsafe_allow_html=True)
    col2.markdown("<h4 style='color: black;'>Driver</h4>", unsafe_allow_html=True)
    col3.markdown("<h4 style='color: black;'>Car</h4>", unsafe_allow_html=True)
    col4.markdown("<h4 style='color: black;'>Check-Out</h4>", unsafe_allow_html=True)
    col5.markdown("<h4 style='color: black;'>Return</h4>", unsafe_allow_html=True)

    for res in reservations:
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.markdown(f"<p style='color: black;'>{res[0]}</p>", unsafe_allow_html=True)
        col2.markdown(f"<p style='color: black;'>{res[1]}</p>", unsafe_allow_html=True)
        col3.markdown(f"<p style='color: black;'>{res[2]}</p>", unsafe_allow_html=True)
        col4.markdown(f"<p style='color: black;'>{res[3][:16]}</p>", unsafe_allow_html=True)
        col5.markdown(f"<p style='color: black;'>{res[4][:16]}</p>", unsafe_allow_html=True)

# Function to view cars and their rates
def display_car_rates():
    car_rates = view_car_rates()
    car_types = [car[0] for car in car_rates]
    rates = [f"${car[1]:.2f}" for car in car_rates]

    col1, col2 = st.columns(2)
    col1.markdown("<h4 style='color: black;'>Car Type</h4>", unsafe_allow_html=True)
    col2.markdown("<h4 style='color: black;'>Rate</h4>", unsafe_allow_html=True)

    for car, rate in zip(car_types, rates):
        col1.markdown(f"<p style='color: black;'>{car}</p>", unsafe_allow_html=True)
        col2.markdown(f"<p style='color: black;'>{rate}</p>", unsafe_allow_html=True)

# Function to extend a reservation
def extend_reservation(reservation_id, new_return_time):
    if reservation_id and new_return_time:
        result = request_extension(reservation_id, new_return_time)
        st.info(f"Extension Status: {result}")
    else:
        st.warning("Please fill all fields")

# Function to change the car rate
def change_car_rate(car_type, new_rate):
    if car_type and new_rate:
        try:
            new_rate = float(new_rate)
            result = update_car_rate(car_type, new_rate)
            st.success(result)
        except ValueError:
            st.warning("Please enter a valid numeric rate.")
    else:
        st.warning("Please fill all fields")

# Streamlit UI Setup for User Interface
def user_interface():
    st.title("Car Rental Driver Interface")

    display_car_rates()

    st.subheader("Create a Reservation")
    driver_name = st.text_input("Driver Name")
    car_type = st.text_input("Car Type (Sedan, SUV, Pick-Up, Van)")
    check_out = st.text_input("Check-Out (YYYY-MM-DD HH:MM)")
    return_time = st.text_input("Return Time (YYYY-MM-DD HH:MM)")

    if st.button("Create Reservation"):
        submit_reservation(driver_name, car_type, check_out, return_time)

    if st.button("View Reservations"):
        display_reservations()

    st.subheader("Extend a Reservation")
    reservation_id = st.text_input("Reservation ID to Extend")
    new_return_time = st.text_input("New Return Time (YYYY-MM-DD HH:MM)")

    if st.button("Extend Reservation"):
        extend_reservation(reservation_id, new_return_time)

    # Logout button
    if st.button("Logout"):
        logout()

# Streamlit UI Setup for Admin Interface
def admin_interface():
    st.title("Car Rental Admin Interface")

    display_car_rates()

    if st.button("View Reservations"):
        display_reservations()

    car_type = st.text_input("Car Type to Update Rate")
    new_rate = st.text_input("New Rate Per Day")

    if st.button("Update Car Rate"):
        change_car_rate(car_type, new_rate)

    # Logout button
    if st.button("Logout"):
        logout()

# Login Page Function
def login_page():
    st.title("Car Rental Login Page")

    # Display sample credentials for testing
    st.markdown("<h4>Sample Usernames and Passwords for Testing:</h4>", unsafe_allow_html=True)
    st.markdown("""
     <ul>
         <li><b>Admin:</b> Username: <code>admin</code>, Password: <code>password</code></li>
         <li><b>User:</b> Username: <code>user</code>, Password: <code>password</code></li>
     </ul>
     """, unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state['logged_in'] = 'admin'
            st.success("Logged in as Admin!")
            st.rerun()

        elif username == "user" and password == "password":
            st.session_state['logged_in'] = 'user'
            st.success("Logged in as User!")
            st.rerun()
        else:
            st.error("Invalid username or password")

# Main Application Logic
def main():
    if 'logged_in' not in st.session_state:
        login_page()  # Show login page if not logged in
    else:
        if st.session_state['logged_in'] == 'admin':
            admin_interface()  # Show Admin Interface

        elif st.session_state['logged_in'] == 'user':
            user_interface()  # Show User Interface

if __name__ == "__main__":
    main()
