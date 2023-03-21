# Reservation System

### This is a simple command line application for booking and canceling court reservations. It allows users to make reservations, cancel reservations, view the schedule and save it to a file.

### Usage
To use the program, run the main.py file in your terminal. You will be presented with a menu of options:

##### What do you want to do:
1. Make a reservation
2. Cancel a reservation
3. Print schedule
4. Save schedule to a file
5. Exit

#### Make a reservation
To make a reservation, select option 1 from the main menu. You will be prompted to enter your name and the date and time you would like to book in the following format: DD.MM.YYYY HH:MM. The program will check if you have already made two reservations for the current week and if the court is available at the specified time. You will also be presented with the available time slots for the specified day. Select the desired slot by entering the corresponding number. If the reservation is successful, you will receive a confirmation message.

#### Cancel a reservation
To cancel a reservation, select option 2 from the main menu. You will be prompted to enter your name and the date and time of your reservation in the same format as when making a reservation. If the reservation is found in the system, it will be removed and you will receive a confirmation message.

#### Print schedule
To print the schedule for a specific date range, select option 3 from the main menu. You will be prompted to enter the start and end dates in the format DD.MM.YYYY. The program will then display the reservations for each day in the specified range.

#### Save schedule to a file
To save the schedule to a file, select option 4 from the main menu. You will be prompted to enter the start and end dates in the format DD.MM.YYYY. The program will then save the reservations for each day in the specified range to a CSV file named schedule.csv.

#### Exit
To exit the program, select option 5 from the main menu.

### Dependencies
This program requires Python 3.x and the following modules:

* datetime
* timedelta
* csv