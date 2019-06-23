import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


cid ="6ac501309e3b4f5c83c9cf0af07ec7d6"
secret = "8e23f5a287ea43b5af5a3d58634299cb"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

track_id = track_name = popularity = artist_name = []

for i in range(0,10000, 50):
    print('=============== Generate data  iterat n° {} / 10000 ==============='.format(i+1))
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)

    for j, t in enumerate(track_results['tracks']['items']):
        # print('=============== Epochs n° {} / {} / 10000 ==============='.format((j+1),(i+1)))
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

    break
        # print('{} - {} - {} - {}'.format(t['artists'][0]['name'], t['name'], t['id'], t['popularity']))

print('\nLen of artist_name = {} \nLen of track_name = {} \nLen of popularity = {} \nLen of track_id = {} '.format(len(artist_name), len(track_name), len(popularity), len(track_id)))

json_track_id = json.loads(track_id)
print(json_track_id)

# for idx in range(len(track_id)):
#
#     print('{} - {} - {} - {}'.format(track_id[idx], track_name[idx], popularity[idx], artist_name[idx]))
