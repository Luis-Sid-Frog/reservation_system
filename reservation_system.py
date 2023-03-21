from datetime import datetime, timedelta
import csv



class ReservationSystem:
    def __init__(self):
        self.schedule = []

    def run(self):
        while True:
            choice = input("What do you want to do:\n"
                           "1. Make a reservation\n"
                           "2. Cancel a reservation\n"
                           "3. Print schedule\n"
                           "4. Save schedule to a file\n"
                           "5. Exit\n")

            if choice == "1":
                self.make_reservation()
            elif choice == "2":
                self.cancel_reservation()
            elif choice == "3":
                self.print_schedule()
            elif choice == "4":
                self.save_schedule()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def make_reservation(self):
        name = input("What's your Name?\n")
        date_str = input("When would you like to book? {DD.MM.YYYY HH:MM}\n")
        date = datetime.strptime(date_str, '%d.%m.%Y %H:%M')

        # Check if user has more than 2 reservations already this week
        reservations_this_week = [r for r in self.schedule if r['name'] == name and r['date'].isocalendar()[1] == date.isocalendar()[1]]
        if len(reservations_this_week) >= 2:
            print("Sorry, you have reached the maximum number of reservations for this week.")
            return

        # Check if court is already reserved for the time user specified
        if any(r for r in self.schedule if r['date'] == date):
            print("Sorry, the court is already reserved at that time.")
            return

        # Check if the date is less than one hour from now
        if date - datetime.now() < timedelta(hours=1):
            print("Sorry, you must reserve the court at least one hour in advance.")
            return

        # Display possible periods in 30 minute intervals up to 90 minutes.
        # If the court is reserved from 17:00 you should only show the first 2 options.
        max_duration = 90 if date.hour < 17 else min(90, (datetime(date.year, date.month, date.day, 17, 0) - date).seconds // 60)
        options = []
        for duration in range(30, max_duration + 1, 30):
            options.append(f"{duration // 60} hour{'s' if duration >= 60 else ''} and {duration % 60} minute{'s' if duration > 1 else ''} ({duration} minutes)")
        options_str = '\n'.join([f"{i+1}) {option}" for i, option in enumerate(options)])
        print("How long would you like to book court?\n" + options_str)

        # Prompt the user to choose a duration and make the reservation
        choice = input()
        duration = int(options[int(choice) - 1].split('(')[1].split(' ')[0])
        self.schedule.append({'name': name, 'date': date, 'duration': duration})
        print("Reservation made successfully.\n")

    def cancel_reservation(self):
        print("Cancel a reservation")
        name = input("What's your name? ")
        reservation_time = input("When was your reservation? {DD.MM.YYYY HH:MM} ")

        # Parse the user's reservation time
        try:
            reservation_datetime = datetime.strptime(reservation_time, "%d.%m.%Y %H:%M")
        except ValueError:
            print("Invalid date/time format. Please enter a date/time in the format: {DD.MM.YYYY HH:MM}")
            return

        # Remove the reservation from the schedule
        for i, reservation in enumerate(self.schedule):
            if reservation["name"] == name and reservation["date"] == reservation_datetime:
                del self.schedule[i]
                break

        print("Reservation successfully canceled!")

    def print_schedule(self):
        print("Print schedule")

        # Prompt user to enter start and end dates
        start_date = input("Enter start date (DD.MM.YYYY): ")
        end_date = input("Enter end date (DD.MM.YYYY): ")
        # Parse the user's start and end dates

        try:
            start_datetime = datetime.strptime(start_date, "%d.%m.%Y")
            end_datetime = datetime.strptime(end_date, "%d.%m.%Y")
        except ValueError:
            print("Invalid date format. Please enter dates in the format: DD.MM.YYYY")
            return

        # Iterate over dates in the specified range and print reservations for each date
        current_date = start_datetime
        while current_date <= end_datetime:
            print(current_date.strftime("%A, %d.%m.%Y"))
            reservations_for_date = []
            for reservation in self.schedule:
                if current_date.date() == reservation["date"].date():
                    reservations_for_date.append(reservation)
            if not reservations_for_date:
                print("No reservations")
            else:
                for reservation in reservations_for_date:
                    start_time_str = reservation["date"].strftime("%H:%M")
                    end_time_str = (reservation["date"] + timedelta(minutes=reservation["duration"])).strftime("%H:%M")
                    print(f"* {reservation['name']} {start_time_str} - {end_time_str}")
            print()
            current_date += timedelta(days=1)

    def save_schedule(self):
        print("Save schedule")

        # Prompt user to enter start and end dates
        start_date = input("Enter start date (DD.MM.YYYY): ")
        end_date = input("Enter end date (DD.MM.YYYY): ")
        # Parse the user's start and end dates

        try:
            start_datetime = datetime.strptime(start_date, "%d.%m.%Y")
            end_datetime = datetime.strptime(end_date, "%d.%m.%Y")
        except ValueError:
            print("Invalid date format. Please enter dates in the format: DD.MM.YYYY")
            return

        # Iterate over dates in the specified range and print reservations for each date
        current_date = start_datetime
        with open('schedule.csv', 'w', newline='') as csvfile:

            fieldnames = ['dates']

            thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            while current_date <= end_datetime:
                current_date.strftime("%A, %d.%m.%Y")
                reservations_for_date = []
                for reservation in self.schedule:
                    if current_date.date() == reservation["date"].date():
                        reservations_for_date.append(reservation)
                        thewriter.writerow({'dates':reservation})
                if not reservations_for_date:
                    print("No reservations")
                else:
                    for reservation in reservations_for_date:
                        start_time_str = reservation["date"].strftime("%H:%M")
                        end_time_str = (reservation["date"] + timedelta(minutes=reservation["duration"])).strftime("%H:%M")
                        print(f"* {reservation['name']} {start_time_str} - {end_time_str}")
                print()
                current_date += timedelta(days=1)







if __name__ == "__main__":
    system = ReservationSystem()
    system.run()