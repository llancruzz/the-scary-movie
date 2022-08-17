"""
This is a python application to give users choice to book a scary movie to watch.
"""

import sys
import time
from datetime import datetime

from google.oauth2.service_account import Credentials

import gspread
import pyfiglet

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]


CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("the_scary_movie")


MOVIE_LIST = {
    "1.": "The Innocents - Eskil Vogt, €12.50, On Monday - 21:00",
    "2.": "Hellbender - J.Adams, €12.50, On Tuesday - 21:00",
    "3.": "You Won't Be Alone - Goran Stolevski, €12.50, On Wednesday - 21:00",
    "4.": "Pray - Dan Trachtenberg, €12.50, On Thursday - 21:00",
    "5.": "The Black Phone - Scott Derrickson, €12.50, On Friday - 21:00",
    "6.": "The Cursed - Sean Ellis, €12.50, On Saturday - 18:00",
    "7.": "Room 203 - Ben Jagger, €12.50, On Saturday - 21:00",
    "8.": "Studio 666 - BJ McDonnell, €12.50, On Sunday - 21:00",
}

REPEAT_RESERVATION_MSG = """
If you want to place another reservation,
enter 1. If not, enter any other key.
"""

LIST_MOVIES_MSG = """
Are you tired of boring movies?
Do you want to feel scared in some movies?
Enter Y to see our movies this week or N to exit:
"""

ORDER_MOVIE_MESSAGE = """

If you wish to place a reservation, please enter the number of the movie you
wish to the booking (i.e. 1 for 'The Innocents' 2 for 'Hellbender' and so on.).

If there is nothing on our list for you this week, no worries.

Press any other key to leave the reserve. \U0001F642

"""

BOOKING_CONFIRMATION_MSG = """
Thank you for supporting your local Scary Cinema! \U0001F917

Your reserve has been booked.
Within the next minutes, you will receive your reservation.

We'll send you a text message 1 hour before the movie starts \U0001F4F2

And here is your receipt \U0001F9FE:
"""

BOOKING_RECEIPT = """

..........................................
The Scary Movie
Cinema Scary 666
1 Hillview Drogheda Louth

You booked: {select_movie} \U0001F4D6

{booking_time}
..........................................

"""


def enter_or_exit():
    """Function to either continue to reserve or leave the Cinema Booking."""

    while True:
        print("Hey phobophile's fans. Welcome to The Scary Movie! \U0001F3A6")
        decision_user = input(LIST_MOVIES_MSG)
        decision_user = decision_user.strip().lower()
        if decision_user == "y":
            print("Let me find the movies for you....\n")
            time.sleep(1)
            for index_list, title in MOVIE_LIST.items():
                print(index_list, title)
            break
        elif decision_user == "n":
            print(
                "Why? Don't be afraid!!! Take your time! Book whenever you're "
                "already. Enjoy your day! \U0001F64B"
            )
            sys.exit()
        else:
            print(
                "I'm not sure you want to see the movies! \U0001F914"
                "Let's try again. Please make sure to enter Y or N \n"
            )


def order_movie():
    """
    Function to select a movie or leave the cinema booking.
    """
    while True:
        print(ORDER_MOVIE_MESSAGE)
        select_movie = input("Please enter the number or other key: ").strip() + "."
        if select_movie in MOVIE_LIST:
            selected_movie = MOVIE_LIST[select_movie]
            print(f"You have selected: {selected_movie} \U0001F608")
            return selected_movie

        print("No worries. Have a nice day \U0001F44B")
        sys.exit()


def user_data():
    """Gets and check user's details"""

    print("\nTo complete the booking, please enter your details... \U0001F58A")
    while True:
        print()
        time.sleep(0.5)
        fname = input("Please enter your first name: ")
        fname = fname.strip()
        if len(fname) < 1 or fname.isdigit():
            print(
                """Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a name!"""
            )
            print("Let's start again \U0001F60A")
            continue

        lname = input("Please enter your last name: ")
        lname = lname.strip()
        if len(lname) < 1 or lname.isdigit():
            print(
                """Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a name!"""
            )
            print("Let's start again \U0001F60A")
            continue

        mnumber = input("Please enter your 10-digit IE mobile number: ")
        mnumber = mnumber.strip()
        if not validate_number(mnumber):
            continue

        print("Perfect. These are your details:\n")
        print(f"First name: {fname}\nLast name: {lname}\nPhone: {mnumber}")
        print()
        print("If your details are correct enter 1 and if it is not enter 2")
        check_details = input("Please enter now: ")
        check_details = check_details.strip()
        if check_details == "1":
            print("Alright! \U0001F44D Let's finish your reservation \U0001F642")
            print("...................................")
            time.sleep(2)
            break
        elif check_details == "2":
            print("No problem. Let's figure it out! \U0001F642")
            print("Just enter them again to correct them.")
            print()
        else:
            print("Hmm...that doesn't seem right!\U0001F914")
            print("Please make sure to enter 1 or 2.")
            print("Let's start again from the top \U0001F60A")

    return fname, lname, mnumber


def validate_number(numbers):
    """
    Validate mobile phone number
    """
    if len(numbers) != 10:
        print("\nWhoops!\U0001F914 Please make sure you enter 10 digits.")
        print("Let's just try this again from the top \U0001F642")
        print()
        return False

    return True


def update_sheet(first_name, last_name, mobile_number, title, worksheet):
    """
    Function to update the Google Sheet with the user's details and selected
    movie.
    """
    add_data = SHEET.worksheet(worksheet)
    add_data.append_row([first_name, last_name, mobile_number, title])


def print_receipt(selected_movie):
    """ "
    Function to print the receipt selected by user
    """
    print(BOOKING_CONFIRMATION_MSG)
    time.sleep(2)
    now = datetime.now()
    booking_time = now.strftime("%d.%m.%Y %H:%M:%S")
    print(
        BOOKING_RECEIPT.format(select_movie=selected_movie, booking_time=booking_time)
    )


def start_app():
    """
    Main function, which includes all functions to run the program
    """
    enter_or_exit()
    select_movie = order_movie()
    time.sleep(5)
    fname, lname, mnumber = user_data()
    update_sheet(fname, lname, mnumber, select_movie, "record")
    print_receipt(select_movie)


def main():
    while True:
        welcome_title = pyfiglet.figlet_format("The Scary Movie")
        print(welcome_title)
        start_app()
        print(REPEAT_RESERVATION_MSG)
        stay_or_leave = input("Please enter now: ")
        stay_or_leave = stay_or_leave.strip()
        if stay_or_leave == "1":
            continue
        else:
            print("\nSee you next time. Enjoy your day ! \U0001F64B")
            break


if __name__ == "__main__":
    main()
