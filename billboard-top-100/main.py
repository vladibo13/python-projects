import requests
from bs4 import BeautifulSoup
from datetime import datetime

BILLBOARD_URL="https://www.billboard.com/charts/hot-100/"

year = input("what year you would like to travel to in YYYY-MM-DD format \n")

try:
    datetime.strptime(year, "%Y-%m-%d")
except ValueError:
    print('exiting.....')  
    exit(0)

response = requests.get(BILLBOARD_URL + year)

website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

song_names_spans = soup.select("li ul li h3")
artist_name  = [song.find_next_sibling() for song in song_names_spans ]

song_list = [song.getText().strip() for song in song_names_spans]
artist_list = [artist.getText().strip() for artist in artist_name]

tuple_list = list(zip(artist_list, song_list))

with open (f"{year}-billboard-songs.txt", mode = "w") as file:
    for artist, song in tuple_list:
        file.write(f"{artist} - {song}\n")


