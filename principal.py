from msg_module import *
import random

#Simple menu
option = str(input("Write something: "))
while option is True:
    if option == "Customize":
        selection()
    elif option == "random":
        get_lucky()
    else:
        print("Error.")