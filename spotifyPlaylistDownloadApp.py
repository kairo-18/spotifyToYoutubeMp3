import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_search import YoutubeSearch
import webbrowser
import json
from pytube import YouTube
import os

auth_manager = SpotifyClientCredentials(client_id='391e34e657254a0389eadc562ed5409c',client_secret='0cb5525fd1bf4a6196ed60e48dbbf53b')
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_URI = "spotify:playlist:3E2xpl4nTYWLNNzgxYFenK"
songsInPlaylist = []


for track in sp.playlist_tracks(playlist_URI)["items"]:
    #Track name
    track_name = track["track"]["name"]
    artist= track["track"]["artists"][0]['name']
    
    songsInPlaylist.append(artist + ' ' + track_name)  
    

links = []

for songs in songsInPlaylist:
    results = YoutubeSearch(songs, max_results=1).to_json()
    results_dict = json.loads(results)
    for v in results_dict['videos']:    
        links.append('https://www.youtube.com' + v['url_suffix'])

for link in links:
    yt = YouTube(str(link))
    track = yt.streams.filter(only_audio=True).first()
    out_file = track.download(output_path= 'C:\\Users\\kairo\\Music\\GYM')
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print("Downloaded")
