pip install spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                               client_secret="YOUR_CLIENT_SECRET",
                                               redirect_uri="YOUR_REDIRECT_URI",
                                               scope="YOUR_SCOPE"))
current_track = sp.current_playback()
print(current_track)
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('spotify_data.db')
cursor = conn.cursor()

# Create a table and insert data
cursor.execute('''CREATE TABLE IF NOT EXISTS spotify_tracks
                  (track_id TEXT PRIMARY KEY, track_name TEXT, artist TEXT, duration_ms INT)''')

data = [('track_id1', 'Song 1', 'Artist 1', 200000),
        ('track_id2', 'Song 2', 'Artist 2', 250000)]

cursor.executemany('INSERT INTO spotify_tracks VALUES (?,?,?,?)', data)
conn.commit()

# Close the database connection
conn.close()
