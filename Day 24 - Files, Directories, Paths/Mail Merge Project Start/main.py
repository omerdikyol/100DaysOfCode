with open("Input/Letters/starting_letter.txt") as letter:
    lines = letter.read()
    print(lines)

with open("Input/Names/invited_names.txt") as names:
    for name in names:
        temp = lines
        temp = temp.replace("[name]", name.strip())
        with open(f"Output/ReadyToSend/letter_for_{name[:-1]}.txt", mode="w") as file:
            file.write(temp)

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
