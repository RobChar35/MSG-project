from msg_module import *

#Simple menu
print("""
        Welcome to Minecraft Seed Generator!
    ============================================
    These are the options:
    - Customized.
    - Random.
""")
option = str(input("Just write one of them: "))
if option == "customized" or option == "Customized":
    selection()
elif option == "random" or option == "Random":
    get_lucky()
else:
    print("You need to write 'customized' or 'random' to get a result.")