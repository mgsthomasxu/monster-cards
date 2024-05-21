###component 2 welcome screen###


import easygui

# Welcome screen
choices = easygui.buttonbox("Welcome to Monster Card Manager\n"
                           "You may Edit and Delete cards, Add new cards, and can Print all the existing cards\n"
                           "You will be limited to 4 categories (Strength, Speed, Stealth, and Cunning) when Adding a new card",
                           choices=["Add card", "Find card", "Delete card", "Output all", "Exit"],
                           title="Monster Card OPTIONS")


# Loop until the user chooses to exit
while True:
    # Code to add a new card
    if choices == "Add card":
        easygui.enterbox
    # Code to find a card
    elif choices == "Find card":
        easygui.buttonbox
    # Code to delete a card
    elif choices == "Delete card":
        easygui.buttonbox 
    # Code to output all cards
    elif choices == "Output all":
       easygui.msgbox 
    # Code to exit the program
    elif choices == "Exit":
       break