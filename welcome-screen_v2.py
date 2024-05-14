###component 2 welcome screen###


import easygui


choices = easygui.buttonbox("                      Welcome to Monster Card Manager\n"
                            "                                Instrutions:\n"
                            "You may Edit and Delete cards, Add new cards, and Print all the existing cards\n"
                            "       When Adding a new card You will be limited to 4 Categories \n"
                            "     (Strength, Speed, Stealth, and Cunning) when Adding a new card",
                            choices=["Add card", "Find card", "Delete card", "Output all", "Exit"],
                            title="Monster Card OPTIONS")


while True:
    if choices == "Add card":
        # Code to add a new card
        easygui.enterbox
    elif choices == "Find card":
        # Code to find a card
        easygui.buttonbox
    elif choices == "Delete card":
        # Code to delete a card
        easygui.buttonbox
    elif choices == "Output all":
        # Code to output all cards
        easygui.msgbox
    elif choices == "Exit":
        # Code to exit the program
        break