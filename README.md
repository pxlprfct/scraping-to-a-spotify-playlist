# Scraping to a Spotify Playlist
[Blog Post](http://ollie.work/2017/04/17/Scraping-resident.co.uk-to-a-Spotifty-playlist-of-what-shows-are-playing-in-Brighton)

Scrapes [resident-music/tickets](http://www.resident-music.com/tickets), parses the table data, create a .txt of the acts - and then adds the songs to a Spotify playlist.

Uses python 2.x, [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and [Spotipy](https://spotipy.readthedocs.io/en/latest/).

## How to use
1. Create a file called `env.py`
2. Add your Spotify Applicaton's Credentials to the new `env.py` file (look at `spotify.py` for the required details)
3. Add your Spotify Credentials to the `env.py` file
4. Run `scraper.py`
5. Run `spotify.py`
