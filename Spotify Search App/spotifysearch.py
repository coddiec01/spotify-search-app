import requests, sys
from spotifysecrets import CLIENT_ID, CLIENT_SECRET
from base64 import b64encode

# Authenticate with Spotify
AUTHENTICATION_URL = 'https://accounts.spotify.com/api/token'
headers = {'Authorization':
           b'Basic ' + b64encode(CLIENT_ID + b':' + CLIENT_SECRET)}
body = {'grant_type': 'client_credentials'}
r = requests.post(AUTHENTICATION_URL, headers=headers, data=body)
token = r.json()['access_token']
token_headers = {'Authorization' : 'Bearer ' + token}

# Album Search
# ----------------------------------------
album_name = ' '.join(sys.argv[1:])
query_search = {'q': album_name, 'type': 'album'}
SEARCH_URL = 'https://api.spotify.com/v1/search'
response_search = requests.get(SEARCH_URL, headers=token_headers, params=query_search)
album = response_search.json()['albums']['items'][0]
query_tracks = {'country': 'US'}
TRACKS_URL = 'https://api.spotify.com/v1/albums/' + album['id'] + '/tracks'
response_tracks = requests.get(TRACKS_URL, headers=token_headers, params=query_tracks)
tracks = response_tracks.json()['items']
print('Album:', album['name'])
print('Tracks:')
for track in tracks:
   print(track['name'])