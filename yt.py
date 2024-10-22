import requests
from environs import Env
import json
env = Env()
env.read_env()

API_KEY = env.str("YT_API")


def get_video_data(url):
    
    if "youtu.be/" in url:
        prepare = url.split('/')[-1]
        video_id = prepare.split('?')[0]
    elif "youtube.com/watch?v=" in url:
        video_id = url.split('v=')[-1].split('&')[0]
    
    
    
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
    querystring = {"videoId": video_id}
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = {}
    if response.json()['status']:
        thumbnail = response.json()['thumbnails'][-1]['url']
        videos = response.json()['videos']['items'][0]['url']
        audios = response.json()['audios']['items'][0]['url']
        title = response.json()['title']
        data = {
            "title" : title,
            "thumbnail": thumbnail,
            "videos": videos,
            "audios": audios
        }
    else:
        thumbnail = None
        videos = None
        audios = None

    return data