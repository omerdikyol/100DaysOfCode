import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies = movies[::-1] 
#print(movies)

with open("movies.txt", mode="w") as file:
  for movie in movies:
    file.write(f"{movie}\n")


