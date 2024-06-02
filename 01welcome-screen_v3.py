###component 2 welcome screen##


import easygui

# Welcome screen (been well formated)
choices = easygui.buttonbox("                      Welcome to Monster Card Manager\n"
                            "                                Instrutions:\n"
                            "You may Edit and Delete cards, Add new cards, and Print all the existing cards\n"
                            "       When Adding a new card You will be limited to 4 Categories \n"
                            "     (Strength, Speed, Stealth, and Cunning) when Adding a new card",
                            choices=["Add card", "Find card", "Delete card", "Output all", "Exit"],
                            title="Monster Card Manager")

# Loop until the user chooses to exit
while True:
    if choices == "Add card":
        # add a new card
        easygui.enterbox("working", title="add card")
    elif choices == "Find card":
        # find a card
        easygui.buttonbox("working", title="find card")
    elif choices == "Delete card":
        #  delete a card
        easygui.buttonbox("working", title="delete card")
    elif choices == "Output all":
        # output all cards
        easygui.msgbox("working", title="output all")