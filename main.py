NAME_PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invited_names_file:
    names = invited_names_file.read().split("\n")

with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
    letter_template = starting_letter_file.read()

    for name in names:
        personalised_letter_text = letter_template.replace(NAME_PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/{name} invite.docx", "w") as personalised_letter:
            personalised_letter.write(personalised_letter_text)