"""
Using the Spotify API

"""
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# import playlist_link from user_input


client_credentials_manager = SpotifyClientCredentials(
    'daf1fbca87e94c9db377c98570e32ece', '1a674398d1bb44859ccaa4488df1aaa9')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_features(track_id):
    features = sp.audio_features('spotify:track:' + track_id)
    return([features[0]['acousticness'], features[0]['danceability'], features[0]['energy'],
            features[0]['duration_ms'], features[0]['instrumentalness'], features[
        0]['valence'], features[0]['tempo'], features[0]['liveness'],
        features[0]['loudness'], features[0]['speechiness'], features[0]['key']])


print(get_features('537l7spEsGg6aWl6Y9eKAs'))
