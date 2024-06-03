###component 5 edit card
# Improve that user know what card name is entering
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
    choices = easygui.buttonbox("                      Welcome to Monster Card Manager\n"
                                "                                Instructions:\n"
                                "                     You may search cards (Edit and Delete),\n"
                                "               Add new cards, and Print all the existing cards\n"
                                "         When Adding a new card You will be limited to 4 Categories \n"
                                "       (Strength, Speed, Stealth, and Cunning) when Adding a new card",
                                choices=["Add card", "Search card", "Delete card", "Output all", "Exit"],
                                title="Monster Card Manager")
    if choices == "Search card":
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
                print(exist_cards)
            elif edit_choice == "Cancel":
                continue
        else:
            easygui.msgbox(f"Card '{card_name}' not found.", title= "Card Not Found")
    elif choices == "Exit":
        break