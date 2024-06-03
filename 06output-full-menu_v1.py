###component 7###
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
                                choices=["Add card", "Find card", "Delete card", "Output all", "Exit"],
                                title="Monster Card OPTIONS")
    if choices == "Output all":
        card_info = ""
        for card_name, card_stats in exist_cards.items():
            card_info += f"## {card_name}\n"
            card_info += f"### Strength: {card_stats['Strength']}\n"
            card_info += f"### Speed: {card_stats['Speed']}\n"
            card_info += f"### Stealth: {card_stats['Stealth']}\n"
            card_info += f"### Cunning: {card_stats['Cunning']}\n"
            card_info += "\n"
        print(card_info)
        easygui.msgbox("Menu has been printed below In Python Console")
    elif choices == "Exit":
        break
