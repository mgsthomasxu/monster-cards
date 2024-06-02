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
                                choices=["Add card", "Find card", "Delete card", "Edit card", "Output all", "Exit"],
                                title="Monster Card OPTIONS")

    if choices == "Find card":
            card_name = easygui.enterbox("Enter the name of the card you want to find (leave blank to return to the welcome screen):", title="Find Card")
            if card_name is None:  # User canceled or left blank
                continue
            elif not card_name:  # User left blank
                pass  # Return to the welcome screen
            elif card_name not in exist_cards:
                easygui.msgbox(f"Card '{card_name}' does not exist.", "Error")
            else:
                card_stats = exist_cards[card_name]
                card_info = f"## {card_name}\n\n"
                card_info += f"### Strength: {card_stats['Strength']}\n"
                card_info += f"### Speed: {card_stats['Speed']}\n"
                card_info += f"### Stealth: {card_stats['Stealth']}\n"
                card_info += f"### Cunning: {card_stats['Cunning']}\n"
                easygui.msgbox(card_info, f"Card Details: {card_name}")
