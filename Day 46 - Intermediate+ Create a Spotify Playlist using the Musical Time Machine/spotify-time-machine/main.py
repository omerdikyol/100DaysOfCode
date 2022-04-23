from bs4 import BeautifulSoup
import requests

date = input("Which year do yo want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

titles = soup.find_all(name="h3", class_="u-letter-spacing-0021", id="title-of-a-story")

songs = [title.text.strip() for title in titles]

redundant_items = ["Songwriter(s):", "Producer(s):", "Imprint/Promotion Label:", "Gains in Weekly Performance",
                   "Additional Awards", "Songwriter(s): ", " Imprint/Promotion Label:", " Songwriter(s):"]

final_songs = []

for n in songs:
    if n not in redundant_items:
        final_songs.append(n)

final_songs = final_songs[0:100]

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import os


CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
URL_REDIRECT = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
#print(user_id)

song_uris = []
year = date.split('-')[0]

for song in final_songs:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    #pprint.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Song {song} does not exist in Spotify.")

#print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Bilboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)