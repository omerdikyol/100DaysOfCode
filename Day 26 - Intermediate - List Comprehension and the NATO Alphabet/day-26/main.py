# List Comprehension
# new_list = [new_item for item in list if condition]

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# name = "Angela"
# letters_list = [letter for letter in name]
# range_list = [num * 2 for num in range(1,5)]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]

# Challenge 1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# sqrd = [n*n for n in numbers]
# print(sqrd)

# Challenge 2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even = [n for n in numbers if n % 2 == 0]


# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list }
# new_dict ={new_key:new_value for (key, value) in dict.items() if condition}

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# student_score = {name: random.randint(1, 100) for name in names}
# passed_student = {student: score for (student, score) in student_score.items() if score >= 50}

# Challenge 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# new_dict = {word: len(word) for word in sentence.split(' ')}
# print(new_dict)

# Challenge 2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
# print(weather_f)

import pandas as pd
student_data_frame = pd.DataFrame()