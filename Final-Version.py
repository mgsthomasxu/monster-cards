###Final Version

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

# Loop until the user chooses to exit
while True:
    # Welcome screenn
    choices = easygui.buttonbox("                      Welcome to Monster Card Manager\n"
                                "                                Instrutions:\n"
                                "You may Edit and Delete cards, Add new cards, and Print all the existing cards\n"
                                "       When Adding a new card You will be limited to 4 Categories \n"
                                "     (Strength, Speed, Stealth, and Cunning) when Adding a new card",
                                choices=["Add card", "Search card", "Delete card", "Output all", "Exit"],
                                title="Monster Card Manager")
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
            strength = easygui.integerbox(f"Enter {card_name} Strength value (1-25):", lowerbound=1, upperbound=25)
                # If pressed cancel button go back to welcome screen
            if strength is None:
                continue
            speed = easygui.integerbox(f"Enter {card_name} Speed value (1-25):", lowerbound=1, upperbound=25)
            if speed is None:
                continue
            stealth = easygui.integerbox(f"Enter {card_name} Stealth value (1-25):", lowerbound=1, upperbound=25)
            if stealth is None:
                continue
            cunning = easygui.integerbox(f"Enter {card_name} Cunning value (1-25):", lowerbound=1, upperbound=25)
            if cunning is None:
                continue
            # Add the new card to the exist_cards dictionary
            exist_cards[card_name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}
            easygui.msgbox(f"                        Card '{card_name}' added successfully!\n"
                        "                  The full menu is down below In python console", "Success")
    elif choices == "Search card":
    # Get card name from user
        card_name = easygui.enterbox("Enter the card name you would like to find:", title="Search Card")
        # Check if card exists
        if card_name in exist_cards:
            # Get card stats
            chosen_card = exist_cards[card_name]
            card_details = f"{card_name}\n"
            #stat = strings, value = integer
            for stat, value in chosen_card.items():
                card_details += f"{stat}: {value}\n"
            # Show card details and get user choice
            edit_choice = easygui.buttonbox(card_details, title= "Card Stats", choices=["Edit Card", "Cancel"])
            # same as add card
            if edit_choice == "Edit Card":
                strength = easygui.integerbox(f"Enter {card_name} Strength value (1-25):", lowerbound=1, upperbound=25)
                # If pressed cancel button go back to welcome screen
                if strength is None:
                    continue
                speed = easygui.integerbox(f"Enter {card_name} Speed value (1-25):", lowerbound=1, upperbound=25)
                if speed is None:
                    continue
                stealth = easygui.integerbox(f"Enter {card_name} Stealth value (1-25):", lowerbound=1, upperbound=25)
                if stealth is None:
                    continue
                cunning = easygui.integerbox(f"Enter {card_name} Cunning value (1-25):", lowerbound=1, upperbound=25)
                if cunning is None:
                    continue
                # Add the new card to the exist_cards dictionary
                exist_cards[card_name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}
                easygui.msgbox(f"                        Card '{card_name}' added successfully!\n"
                                "                  The full menu is down below In python console", "Success")
            elif edit_choice == "Cancel":
                continue
        else:
            easygui.msgbox(f"Card '{card_name}' not found.", title= "Card Not Found")
    elif choices == "Delete card":
        # Get Card Name to Delete
        card_name = easygui.enterbox(f"Enter the name of the card you want to delete:", title="Delete Card")
        # Check if Card Exists
        if card_name in exist_cards:
            # Confirm Deletion
            confirm = easygui.buttonbox(f"Are you sure you want to delete {card_name}", 
                                       title="Confirm", choices=["Yes", "No"])
            if confirm == "Yes":
                # Delete Card
                del exist_cards[card_name]
                easygui.msgbox(f"{card_name} deleted successfully!", "Success")
            else:
                # Cancel Deletion
                easygui.msgbox("Card delete canceled.", "Canceled")
        else:
            # Card Not Found
            easygui.msgbox(f"{card_name} not found.", title="Card Not Found")
    elif choices == "Output all":
        card_info = ""
        # Loop through each card and its stats
        for card_name, card_stats in exist_cards.items():
            # Build a string with the card name and stats
            card_info += f"# {card_name} = "
            card_info += f"Strength: {card_stats['Strength']}, "
            card_info += f"Speed: {card_stats['Speed']}, "
            card_info += f"Stealth: {card_stats['Stealth']}, "
            card_info += f"Cunning: {card_stats['Cunning']}\n"
        # Print the card info string
        print(card_info)
        easygui.msgbox("Menu has been printed below In Python Console")
    elif choices == "Exit":
        break