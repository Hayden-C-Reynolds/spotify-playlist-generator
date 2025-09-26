# Spotify Billboard 100 Playlist

A Python project that scrapes the Billboard Hot 100 for a user-specified date and creates a private Spotify playlist with those songs.

## Features
- Scrapes Billboard Hot 100 website for a given date
- Uses the Spotify API to search for songs
- Automatically creates a private Spotify playlist with the songs
- Handles missing songs gracefully

## Technologies Used
- Python
- `requests` and `BeautifulSoup` for web scraping
- `spotipy` for Spotify API interactions

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
2. Install required packages:
`pip install requests beautifulsoup4 spotipy`
3. Create a Spotify Developer account and generate:
- `Client ID`
- `Client Secret`
- `Redirect URI`
4. Replace the placeholders in main.py:
```python
SPOTIFY_CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_SPOTIFY_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "YOUR_REDIRECT_URI"
USER_ID = "YOUR_SPOTIFY_USER_ID"
```
5. Run the program
`python main.py`
6. Follow the prompt to enter a date in YYYY-MM-DD format.
7. Check your Spotify account for the newly created playlist.

##Notes
- You do not need to include your Spotify API keys in a public repository.
- The project demonstrates web scraping, API interaction, and automation.

##License
This project is licensed under the MIT License.
