# -*- coding: latin-1 -*-

import spotipy
import spotipy.util as util

import env

# env
# Spotify App Credentials
# os.environ["SPOTIPY_CLIENT_ID"] = ''
# os.environ["SPOTIPY_CLIENT_SECRET"] = ''
# os.environ["SPOTIPY_REDIRECT_URI"] = ''
#
# Spotify Account Credentials
# username = ''
# scope = 'playlist-modify-private'
# playlist = ''


_username = env.username
_scope = env.scope
_playlist = env.playlist
_token = util.prompt_for_user_token(_username, _scope)

f = "Resident.txt"

if _token:
    spotify = spotipy.Spotify(auth=_token)
    spotify.trace = False

    with open(f, "r") as f:

        uri = ""
        uri_list = []
        count = 0

        for line in f:
            # only get the first 100 results
            if count < 100:
                try:
                    song = spotify.search(line, 1, 0, 'track')

                    # gets uri of first returned result - messy but kinda works
                    uri = song['tracks']['items'][0]["uri"]

                    uri_list.append(uri)
                    count += 1
                except IndexError:
                    print line.strip() + " - Act not found (check the formatting)"
            else:
                break

        print "Add songs to playlist? y/n"
        if raw_input() is 'y' or 'Y':
            spotify.user_playlist_add_tracks(_username, _playlist, uri_list)
            print "\nSongs added successfully"

else:
    print "Can't get token for " + _username
