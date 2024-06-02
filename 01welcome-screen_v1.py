###component 2 welcome screen###


import easygui


choices = easygui.buttonbox("Welcome to Monster Card Manager\n"
                           "You may Edit and Delete cards, Add new cards, and can Print all the existing cards\n"
                           "You will be limited to 4 categories (Strength, Speed, Stealth, and Cunning) when Adding a new card",
                           choices=["Add card", "Find card", "Delete card", "Output all", "Exit"],
                           title="Monster Card OPTIONS")