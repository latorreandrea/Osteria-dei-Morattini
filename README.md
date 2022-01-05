# Osteria dei Morattini

## Code Institute Portfolio 4 Project

Osteria dei Morattini is an imaginary restaurant that gives its customers the opportunity to book a a culinary experience online .
A live website can be found [here](https://osteria-dei-morattini.herokuapp.com/)

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

### User Stories:


- As a userI can register on the site so that I can access to the booking sistem
- As a user I can have multiple table occupancies so that I can eat together with my friends / colleagues / partner etc.
- As a user I can see the menu in the web site so that I already know what cuisine it is, prices, etc. before arriving at the restaurant
- As a user I can cancel my booking so I can free up the places I don't intend to occupy
- As a user I can avoid doble bookings so that I do not create inconvenience in the service
- As a user I can book a seat so that so I can definitely use the restaurant




## Features:
the main features of the site are:

### Home Page:
The landing page where the user will arrive: from here the user access the table reservation system after logging in:
![home](https://user-images.githubusercontent.com/80674568/148095720-93511e80-537f-4999-8fae-1f7171a82d4a.PNG)

### Booking system :
The main part of the reservation system where the user books the table by inserting: the number of seats, the day and time of the meal.
This system does not allow you to make multiple reservations on the same day!
![prenotazione](https://user-images.githubusercontent.com/80674568/148095736-4467b715-1758-4cf0-a7b5-f5c83de70ac4.PNG)

### Reservation List:
After completing the reservation, this screen will summarize the main data of the request, and will collect the user's personal data.
This list also allows you to modify a reservation as well as delete it.
Each user will of course only be able to see their own reservation list with the exception of the Admin
![listaprenotazioni](https://user-images.githubusercontent.com/80674568/148095727-d2b806ef-1701-459c-99bc-eb584e76c3a8.PNG)

### Menu:
A page listing the restaurant menu
![menu](https://user-images.githubusercontent.com/80674568/148095729-39b37156-1838-4b63-b2e9-eab91fea36cb.PNG)

## Features Left to Implement:

- Calendar - use calendar to send a reminder to the user

## Technologies Used:


- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - used to structure the website and create the essential elements of my site. 

- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) 
  - used to style the markup and create custom styling. 

- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - used to create the scripts to delete messages afther 3 second.

- [GitHub](https://github.com/) 
  - used to store the source code and repository. 
- [Heroku](https://www.heroku.com/) 
  - used to deploy my website.

- [Balsamiq](https://balsamiq.com/) 
  - used to help create my wireframes.

- [FontAwe](https://fontawesome.com/)
  - used to use some icons in the site.

- [pixabay](https://pixabay.com/)
  - used for the menu and homepage images.


## Testing:

### Automated Test

I used the Django TestCase estension to test:
- The correct use of the form (i.e. that it was able to collect the right data). You can find it in the *test_forms.py* file
- The correct collection of information and the correct elimination of them. You can find it in the *test_models.py* file
- The correct response of the views. You can find it in the *test_views.py* file

### Manual Test

- Try to create a test account with not matching password and check error status
- Try to miss values in field to see error fields
- Try to edit the reservations
- Check that 'MyReservation' and 'Logout' voices appear on navigation bar

## Deployment
The web site has been deployed on Heroku for hosting and on GitHub to share the full development code.

### Heroku
This page has been deployed to "Heroku"

- Created requirements.txt file with the code ```$ python freeze --local > requirements.txt```
- Created the Procfile with  ```web: gunicorn osteria.wsgi```
- Created a new Heroku App - unique name and EU Server
- Added the Heroku Postgress Database as resource
- Installed the package dj-database-url to allow connection to a database url
- Installed the package psycopg2 for connecting to postgress databases
- Installed the package gunicorn to connect the project to Heroku.
- Setup the default database in settings.py to the postgres database
- Migrated the project in order to use the new postgres datatbase
- Created a superuser
- Set up a AWS S3 bucket to serve the website
- Installed django-storages 
- Disabled collectstatic in Heroku sto prevent uploading static files
- Connected Github repository to Heroku App through 'Deployment Method' in Heroku - App Dashboard
- Deploy Branch through Manual Deploy' in Heroku App Dashboard
- Added the heroku address to valid hosts in settings.py


## Credits

- Favicon
- StackOverflow
- Pixabay for images
- https://ordinarycoders.com/ for the footer
- CodeInstitute tutor support: in particular JoWings to help me to set in the right way static files


