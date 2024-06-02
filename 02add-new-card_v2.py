###component 3 add new card###

import easygui

exist_cards = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

while True:
    # Welcome screenn
    choices = easygui.buttonbox("                      Welcome to Monster Card Manager\n"
                                "                                Instrutions:\n"
                                "You may Edit and Delete cards, Add new cards, and Print all the existing cards\n"
                                "       When Adding a new card You will be limited to 4 Categories \n"
                                "     (Strength, Speed, Stealth, and Cunning) when Adding a new card",
                                choices=["Add card", "Find card", "Delete card", "Output all", "Exit"],
                                title= "Monster Card Manager")
    if choices == "Add card":
        card_name = easygui.enterbox("Enter the new monster card name:")
        # User left blank
        if card_name is None:  # User canceled can be Return to the welcome screen    
            continue 
        # This line checks if the entered card name already exists in the exist_cards dictionary
        elif card_name in exist_cards:
            easygui.msgbox(f"Card '{card_name}' already exists. Please choose a different name.", "Error")
        # continue entering the 4 categories
        else:
            strength = easygui.integerbox("Enter the Strength value (1-25):", lowerbound=1, upperbound=25)
            speed = easygui.integerbox("Enter the Speed value (1-25):", lowerbound=1, upperbound=25)
            stealth = easygui.integerbox("Enter the Stealth value (1-25):", lowerbound=1, upperbound=25)
            cunning = easygui.integerbox("Enter the Cunning value (1-25):", lowerbound=1, upperbound=25)
             # Add the new card to the exist_cards dictionary
            exist_cards[card_name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}
            print(f"Existing cards:", exist_cards)
    elif choices == "Exit":
        break