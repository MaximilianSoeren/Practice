# import all our modules
import openpyxl
from os import path

# # Trying to program a login program

# Write different functions used in the code.


# check if workbook has been created, if so just load it do not make another one
def load_workbook(wb_path):
    if path.exists(wb_path):
        return openpyxl.load_workbook(wb_path)
    return openpyxl.Workbook()


# defining of variables

wb_path = "userdata.xlsx"
wb = load_workbook(wb_path)

ws = wb["userdata"]
# Define home screen, the user is redirected to this in case of an error.
# def home_screen():
#     print("Please select if you want to create an account or log in.")
#     print("(1): Create an account.""\n" "(2): Log in.""\n" "(3) Show Usernames.""\n" "(4) Show Passwords.")
#     print("\n")
#     selection = int(input("Please enter your selection: "))
#     if selection == 1:
#         create_account()
#     elif selection == 2:
#         log_in()
#     elif selection == 3:
#         print(usernames)
#     elif selection == 4:
#         print(passwords)
#

usernames = []
passwords = []


# Function to create an account.
def create_account():
    print("Hello, let's create an account.")
    print("\n")
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    if username in usernames:
        print("This username is already taken")
    else:
        usernames.append(username)

    # passwords.append(password)
    for username in usernames:
        row = 1
        if ws.cell.value is None:
            ws.cell(row=row, column=1, value=username)
        else:
            row += 1

    # for password in passwords:
    #     sheet.cell(sheet, column=2, value=password)

# def log_in():
#     userdata = open("data.txt", "r")
#     username = ("\n" + input("Please enter your username: "))
#     password = ("\n" + input("Please enter your password: "))
#     if username ==



# creating usernames and password lists.

usernames = []
passwords = []

# getting input from the user to put into the lists


create_account()

#

#
#
#     userdata.close()
#
#
#
# if selection == 1:
#     create_account(username,password)
# elif selection == 2:
#     log_in(username, password)
# else:
#     Print("Please select one either (1) or (2).")


wb.save(wb_path)
