### Component 6 delete card

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
                                choices=["Add card", "Search card","Delete Card", "Output all", "Exit"],
                                title="Monster Card Manager")
    if choices == "Delete Card":
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
                print(exist_cards)
            else:
                # Cancel Deletion
                easygui.msgbox("Card delete canceled.", "Canceled")
        else:
            # Card Not Found
            easygui.msgbox(f"{card_name} not found.", title="Card Not Found")
    elif choices == "Exit":
        break