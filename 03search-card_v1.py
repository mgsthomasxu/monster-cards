###component 4 search card

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
                                "You may Edit and Delete cards, Add new cards, and Print all the existing cards\n"
                                "       When Adding a new card You will be limited to 4 Categories \n"
                                "     (Strength, Speed, Stealth, and Cunning) when Adding a new card",
                                choices=["Add card", "search card", "Delete card", "Edit card", "Output all", "Exit"],
                                title="Monster Card Manager")
    if choices == "search card":
    # Get card name from user
        card_name = easygui.enterbox("Enter the card name:", title="Find Card")
        # Check if card exists
        if card_name in exist_cards:
            # Get card stats
            chosen_card = exist_cards[card_name]
            #stat = strings, value = integer
            for stat, value in chosen_card.items():
                card_details = f"{card_name}\n\n"
                card_details += f"{stat}: {value}\n"
            # Show card details and get user choice
            edit_choice = easygui.buttonbox(card_details, title="Card Stats", choices=["Edit Card", "Return"])
            # Handle user choice
            if edit_choice == "Edit Card":
                # Edit card code goes here
                pass
            elif edit_choice == "Return":
                continue
    elif choices == "Exit":
        break