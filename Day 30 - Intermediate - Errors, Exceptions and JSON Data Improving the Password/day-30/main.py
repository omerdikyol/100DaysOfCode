
# try: # Tries
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError: # Works if specific error is found
#     file = open("a_file.txt", "w") # If file DNE, create the file.
#     file.write("smth")
#
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else: # Works if there are no errors occured
#     content = file.read()
#     print(content)
# finally: # Works anyway
#     file.close()
#     print("File was closed")
#     raise KeyError("Bu benim hatam") # Raising our own exceptions

# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)


# Challenge 1
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)


# Challenge 2
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#
# print(total_likes)
