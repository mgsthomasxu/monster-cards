# 27/03/2023, 09:37
# contacts_v3.py
# ~\OneDrive
# -
# Middleton Grange School\Resources\12DTC\2.7 and 2.8
# combined unit\6-8 Exercise solutions
# -
# own\contacts_v3.py

import easygui

# Original list

contacts = {
    1: {
        "First Name": "John",
        "Last Name": "Matua",
        "Mobile": "027 121 1245",
        "Email": "matua_j@maximail.com"
    },
    2: {
        "First Name": "Smith",
        "Last Name": "Pearson",
        "Mobile": "029 127 1247",
        "Email": "selat@maximail.co.lt"
    }
}

# Loop till "Quit"
while True:
    result = []
    choice = easygui.buttonbox("What do you want to do:", "Choices",
                               choices=["Search", "New Contact",
                                        "Print All", "Quit"])

    if choice == "Search":
        search_ID = ""
        search_name = easygui.enterbox("Enter name: ", "Search").capitalize()
        for contact in contacts:
            if search_name in contacts[contact]["First Name"] or \
               search_name in contacts[contact]["Last Name"]:
                search_ID = contacts[contact]

        if search_ID:
            for key in search_ID:
                item = f"{key}: {search_ID[key]}"
                result.append(item)
            easygui.msgbox("\n".join(result), "Found")
        else:
            easygui.msgbox(f"\n{search_name} not in contacts", "Not Found")

    elif choice == "New Contact":
        ID_number = ""
        while not ID_number:
            ID_number = easygui.integerbox("Person ID: ", "ID number")
            # Check that ID not already used
            for existingID in contacts:
                if ID_number == existingID:
                    easygui.msgbox(f"{ID_number} is already in use\nUse "
                                   f"another ID number", "ERROR: Duplicate "
                                   "ID number")
                    ID_number = ""
                contacts [ID_number]["First Name"] = first_name
                last_name = easygui.enterbox("Last Name: ", "Last Name") contacts [ID_number]["Last Name"] = last_name

                mobile_phone = easygui.enterbox ("Mobile: ", "Mobile phone")
                contacts [ID_number]["Mobile"] = mobile_phone

                email = easygui.enterbox("Email: ", "Email") contacts [ID_number]["Email"] = email
    elif choice == "Print All":
                    for contact_ID, contact_info in contacts.items():
                        contact = f"\nContact ID: {contact_ID}"
                        result.append(contact)
                        for key in contact_info:
                            result.append(f"{key}: {contact_info[key]}")
