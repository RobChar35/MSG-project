from msg_module import *

#Simple menu
option = str(input("Write something: "))
if option == "Customize":
    selection()
elif option == "random":
    get_lucky()
else:
    print("Error.")