# encoding: utf-8

import spotipy
import spotipy.util as util

import env

f = "resident.txt"

_username = env.username
_scope = env.scope
_playlist = env.playlist
_token = util.prompt_for_user_token(_username, _scope)


if _token:
    spotify = spotipy.Spotify(auth=_token)
    spotify.trace = False

    uri_list = []

    with open(f, "r") as f:
        count = 0

        for line in f:
            line = line.strip()
            # only get the first 100 results
            if count < 100:
                try:
                    spotify_track = spotify.search(q='artist:' + line, limit=1, type='track')
                    uri_list.append(spotify_track['tracks']['items'][0]['uri'])
                    count += 1

                except IndexError:
                    print "Spotify could not find '" + line + "'"

        spotify.user_playlist_add_tracks(_username, _playlist, uri_list)
        print "\nSongs added successfully"
else:
    print "Failed to get token for " + _username
