# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
import pandas as pd

#data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
# temp_list = data["temp"].to_list()
# print( sum(temp_list)/len(temp_list)) # average temp
# print(data["temp"].mean()) # average temp
#
# # Get Data in Columns
# print(data["condition"]) # Both are same
# print(data.condition)


# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# Create a Datarame from Scratch
# data_dict = {
#     "students": ["Amy","James", "Angela"],
#     "scores": [76,56,65]
# }
#
# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
# data_frame.to_csv("new_data.csv")


# Squirrel Challenge
# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# gray_count = len(data[data["Primary Fur Color"] == "Gray"])
# black_count = len(data[data["Primary Fur Color"] == "Black"])
# cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Black", "Cinnamon"],
#     "Count": [gray_count, black_count, cinnamon_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

