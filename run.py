"""
This is a import library
"""

import time
from datetime import datetime
import sys
import pyfiglet
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]


CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("the_scary_movie")


movie_list = {
    "1.": "The Innocents – Eskil Vogt, €12.50, On Monday - 21:00",
    "2.": "Hellbender – J.Adams, €12.50, On Tuesday - 21:00",
    "3.": "You Won’t Be Alone – Goran Stolevski, €12.50, On Wednesday - 21:00",
    "4.": "Pray – Dan Trachtenberg, €12.50, On Thursday - 21:00",
    "5.": "The Black Phone – Scott Derrickson, €12.50, On Friday - 21:00",
    "6.": "The Cursed – Sean Ellis, €12.50, On Saturday - 18:00",
    "7.": "Room 203 – Ben Jagger, €12.50, On Saturday - 21:00",
    "8.": "Studio 666 – BJ McDonnell, €12.50, On Sunday - 21:00",
}


def enter_or_exit():
    """ "
    Function to either continue to reserve
    or leave the Cinema Booking
    """
    while True:
        print("Hey phobophile's fans. Welcome to The Scary Movie! \U0001F3A6")
        decision_user = input(
            """Are you tired of boring movies? """
            """Do you really want to feel scared with some movies? """
            """Enter Y to see our movies this week or N to exit: """
        )
        decision_user = decision_user.strip()
        if decision_user == "Y" or decision_user == "y":
            print("Let me find the movies for you....\n")
            time.sleep(1)
            for index_list, title in movie_list.items():
                print(index_list, title)
            break
        elif decision_user == "N" or decision_user == "n":
            print(
                "Why? Don’t be afraid!!! Take your time! Book whenever you’re already. Enjoy your day! \U0001F64B"
            )
            sys.exit()
        else:
            print("I'm not sure you're want to see the movies! \U0001F914")
            print("Let's try again. Please make sure to enter Y or N")
            print()
            return enter_or_exit()


def order_movie():
    """ "
    Function to select a movie or leave the cinema booking.
    """
    while True:
        print()
        print(
            """If you wish to place a reservation, please """
            """enter the number of the movie you wish """
            """to booking (i.e. 1 for 'The Innocents' """
            """2 for 'Hellbender' and so on.). \n\nIf there """
            """is nothing in our list for you this week, no worries.\n"""
            """Press any other key to leave the reserve. \U0001F642"""
        )
        print()
        global select_movie
        select_movie = input("Please enter the number or other key: ")
        select_movie = select_movie.strip()
        if select_movie == "1":
            select_movie = movie_list.get("1.")
            print(f"You have selected: {select_movie} \U0001F608")
            break
        elif select_movie == "2":
            select_movie = movie_list.get("2.")
            print(f"You have selected: {select_movie} \U0001F608")
            break
        elif select_movie == "3":
            select_movie = movie_list.get("3.")
            print(f"You have selected: {select_movie} \U0001F608")
            break
        elif select_movie == "4":
            select_movie = movie_list.get("4.")
            print(f"You have selected: {select_movie} \U0001F608")
            break
        elif select_movie == "5":
            select_movie = movie_list.get("5.")
            print(f"You have selected: {select_movie} \U0001F608")
            break
        elif select_movie == "6":
            select_movie = movie_list.get("6.")
            print(f"You have selected: {select_movie} \U0001F608")
            break
        elif select_movie == "7":
            select_movie = movie_list.get("7.")
            print(f"You have selected: {select_movie} \U0001F608")
            break
        elif select_movie == "8":
            select_movie = movie_list.get("8.")
            print(f"You have selected: {select_movie} \U0001F608")
            break
        else:
            print("No worries. Have a nice day \U0001F44B")
            sys.exit()

    return select_movie


def user_data():
    """ "
    Function to get and check user's details
    """
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
            return user_data()
        else:
            pass
        lname = input("Please enter your last name: ")
        lname = lname.strip()
        if len(lname) < 1 or lname.isdigit():
            print(
                """Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a name!"""
            )
            print("Let's start again \U0001F60A")
            return user_data()
        else:
            pass
        mnumber = input("Please enter your 10-digit IE mobile number: ")
        mnumber = mnumber.strip()
        if validate_number(mnumber):
            print("Perfect. These are your details:\n")
        else:
            continue
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
    """ "
    Validate mobile phone number
    """
    try:
        if len(numbers) != 10:
            raise ValueError

    except ValueError:
        print("\nWhoops!\U0001F914 Please make sure you enter 10 digits.")
        print("Let's just try this again from the top \U0001F642")
        print()
        return False

    return True


def update_sheet(name1, name2, number, title, worksheet):
    """ "
    Function to update the Google Sheet
    with the user's details and selected movie.
    """
    add_data = SHEET.worksheet(worksheet)
    add_data.append_row([name1, name2, number, title])


def print_receipt():
    """ "
    Function to print the receipt selected by user
    """
    print(
        """Thank you for supporting your local Scary Cinema! \U0001F917\n"""
        """Your reserve has been booked. """
        """Within the next minutes you will receive your reservation.\n"""
        """We'll send to you a text message 1 hour before the movie starts \U0001F4F2"""
    )
    print()
    print("And here is your receipt \U0001F9FE:")
    time.sleep(2)
    print("..........................................")
    print("The Scary Movie")
    print("Cinema Scary 666")
    print("1 Hillview Drogheda Louth")
    print()
    print(f"You booked: {select_movie} \U0001F4D6")
    print()
    now = datetime.now()
    date_format = now.strftime("%d.%m.%Y %H:%M:%S")
    print(date_format)
    print("..........................................")
    print()


def main():
    """ "
    Main function, which includes
    all functions to run the program
    """
    enter_or_exit()
    select_movie = order_movie()
    print()
    print(
        """ ➡️ Please note: for the purpose of this """
        """project your name and number will be\n"""
        """added to an external sheet. So feel """
        """free to add fictional details if """
        """you prefer.\nNo data will be shared """
        """with anyone unless me."""
    )
    time.sleep(5)
    print()
    print("To complete the booking, please enter your details... \U0001F58A")
    fname, lname, mnumber = user_data()
    update_sheet(fname, lname, mnumber, select_movie, "record")
    print_receipt()


while True:
    welcome_title = pyfiglet.figlet_format("The Scary Movie")
    print(welcome_title)
    main()
    print(
        """If you want to place another reservation """
        """enter 1. If not enter any other key."""
    )
    stay_or_leave = input("Please enter now: ")
    stay_or_leave = stay_or_leave.strip()
    if stay_or_leave == "1":
        continue
    else:
        print()
        print("See you next time. Enjoy your day ! \U0001F64B")
        break
