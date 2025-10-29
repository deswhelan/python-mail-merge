with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.read().split("\n")

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    raw_starting_letter = starting_letter.read()

    for name in names:
        personalised_letter_text = raw_starting_letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as personalised_letter:
            personalised_letter.write(personalised_letter_text)