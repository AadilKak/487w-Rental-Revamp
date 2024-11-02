# **Car Rental Management System**

Welcome to the **Car Rental Management System**! This application allows both drivers and administrators to manage car rentals with ease. The system includes separate functionalities for drivers and admins, providing an efficient and streamlined process for making and managing reservations.

## **Features**

---

### **User Accounts**
The system supports two types of user accounts:
- **Admin Account**: For administrators managing car rates and viewing all reservations.
- **Driver Account**: For drivers creating reservations and managing their own rentals.

**Sample Credentials:**
- **Admin**: Username: `admin`, Password: `password`
- **User**: Username: `user`, Password: `password`

---

### **Driver Features**

#### **1. Make a Reservation**
   - Drivers can reserve a car by selecting from four vehicle types: **Sedan**, **SUV**, **Pick-Up**, and **Van**.
   - **Reservation Policy**: Reservations must be made **at least 24 hours** in advance.

   _(Add image here)_

---

#### **2. Request a Reservation Extension**
   - Drivers can request to extend their rental period. The extension is granted if the vehicle is available (i.e., not reserved by another driver).
   - This feature ensures flexibility for drivers while maintaining vehicle availability for other users.

   _(Add image here)_

---

#### **3. View Current Reservations**
   - Drivers can view their active reservations, including details like car type, check-out time, and return time.

   _(Add image here)_

---

### **Admin Features**

#### **1. View All Reservations**
   - Admins can view all reservations made by drivers, including the driver's name, car type, check-out, and return times.
   - This view helps admins manage vehicle availability efficiently.

   _(Add image here)_

---

#### **2. Update Rental Charges**
   - Rental charges vary based on the car type. Admins can **update the rates** for each vehicle type periodically.
   - Car types and rates are:
     - **Sedan**
     - **SUV**
     - **Pick-Up**
     - **Van**

   _(Add image here)_

---

#### **3. Manage Long-Term Rental Discounts**
   - A reservation that is **one week or longer** may be eligible for a discount, which admins can manage as part of rate settings.
   - This feature is designed to incentivize long-term rentals and offer cost savings to drivers.

   _(Add image here)_

---

### **Technical Specifications**

- **Built With**: Python, Streamlit (for UI), and SQLite (for database).
- **Modular Design**: The app separates database operations and user interface logic for easy maintenance and scalability.
- **Session Management**: The app uses session state to manage user roles and login status, providing a secure and smooth user experience.

---

### **Instructions for Use**

1. **Login**:
   - Start by logging in as either an admin or driver using the sample credentials.
   - Based on your role, the interface will load the appropriate features.

2. **Driver Actions**:
   - Create a reservation by filling in the required fields and selecting a car type.
   - Request a rental extension if needed.
   - View all your current reservations.

3. **Admin Actions**:
   - View the complete list of reservations.
   - Update the rental rates for each car type.
   - Manage discounts for long-term rentals.

---

### **Future Enhancements**
Planned improvements include:
- Notification for drivers on successful reservation extensions.
- Enhanced filtering and search options for admins when viewing reservations.
- Additional customization options for long-term rental discounts.

---

**Thank you for using the Car Rental Management System!**
