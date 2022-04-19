# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("my_file.txt", mode="w") as file: # Open file in write mode
    file.write("Osman Gultekin sen misin?")

with open("my_file.txt", mode="a") as file: # Open file in append mode
    file.write(" ABOOO")

with open("new_file.txt", mode="w") as file:    # If file doesnt exist, it will create
    file.write("we created new")