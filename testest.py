import pandas as pd


df = pd.read_excel("userdata.xlsx", "userdata")

username = df["Username"].values.tolist()
password = df["Password"].values.tolist()




def log_in():
    print("Let's log in, please enter your data beneath""\n")
    a = ("\n" + input("Please enter your username: "))
    b = ("\n" + input("Please enter your password: "))
    while True:
        c = 0
        if a == username[c] and b == password[c]:
            print("You have successfully logged in.")
            break
        else:
            c += 1
# #
log_in()







