# Osteria dei Morattini

## Code Institute Portfolio 4 Project

Osteria dei Morattini is an imaginary restaurant that gives its customers the opportunity to book a a culinary experience online .
A live website can be found ![here](https://osteria-dei-morattini.herokuapp.com/)

## Project goal: Make your reservation!

The main purpose of the site is to allow customers to make a reservation.

This is a responsive Web App with collection of data and demonstration of the use of the method **CRUD**:

C = Create 
R = Read 
U = Update 
D = Delete

### User Goals:

The user would like to book one or more guests for a meal in a restaurant and a particular time and date.

### Site owner's goal:

The site owner would like the ability to take online bookings for their eatery, possibly blocking more bookings for the same day from the same user

### Features:

- Date/Time-based bookings
- Avoid double bookings
- Multiple table occupancies
- Cancellations
- Menu




### Home Page:
The landing page where the user will arrive: from here the user access the table reservation system:
![HomePage]()

### Booking system :
The main part of the reservation system where the user books the table, the number of seats, the day and time of the meal
![booking sistem]()

### Reservation List:
After completing the reservation, this screen will summarize the main data of the request, and will collect the user's personal data. 
If a reservation with the same  date, the reservation is blocked.
![summarizing]()

### Menu:
A page listing the restaurant menu
![Group Reservation]()

## Testing

### Automated Test

I used the Django TestCase estension to test:
- The correct use of the form (i.e. that it was able to collect the right data). You can find it in the *test_forms.py* file
- The correct collection of information and the correct elimination of them. You can find it in the *test_models.py* file
- The correct response of the views. You can find it in the *test_views.py* file

### Manual Test

- Try to create a test account with not matching password and check error status
- Try to miss values in field to see error fields
- Check that 'MyReservation' and 'Logout' voices appear on navigation bar
