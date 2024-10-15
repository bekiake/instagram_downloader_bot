import requests
def tik_tok_download(video_url):
    url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

    querystring = {"url":f"{video_url}","hd":"1"}

    headers = {
        "x-rapidapi-key": "0f95c9454bmshfbfff6f7be74315p12102djsnc98492887d39",
        "x-rapidapi-host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    media = []
    media.append(response.json()['data']['hdplay'])
    media.append(response.json()['data']['music'])
    return media
