import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# ----------------------------
# Spotify API credentials (replace with your own)
# ----------------------------
SPOTIFY_CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_SPOTIFY_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "YOUR_REDIRECT_URI"
USER_ID = "YOUR_SPOTIFY_USER_ID"

# Authenticate Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-private",
    username=USER_ID
))

# ----------------------------
# User input for date
# ----------------------------
date = input("What date do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# ----------------------------
# Scrape Billboard Hot 100 for that date
# ----------------------------
# ⚠️ Replace with your own User-Agent string if needed
header = {
    "User-Agent": "YOUR_USER_AGENT_STRING"
}

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}", headers=header)
soup = BeautifulSoup(response.text, "html.parser")

song_names = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names]

print(f"Top 100 songs on {date}:")
pprint(song_names)

# ----------------------------
# Search for songs on Spotify and collect URIs
# ----------------------------
song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        track_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(track_uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# ----------------------------
# Create Spotify Playlist and add songs
# ----------------------------
playlist = sp.user_playlist_create(
    user=USER_ID,
    name=f"{date} Billboard 100",
    public=False,
    collaborative=False,
    description=f"Billboard 100 for songs on {date}"
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"Playlist created: {playlist['name']}")
