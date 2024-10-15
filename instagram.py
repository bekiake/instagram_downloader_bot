import requests

def instagram_download(video_url):

    url = "https://instagram-scraper-api2.p.rapidapi.com/v1/post_info"

    querystring = {"code_or_id_or_url":f"{video_url}","include_insights":"true"}

    headers = {
        "x-rapidapi-key": "0f95c9454bmshfbfff6f7be74315p12102djsnc98492887d39",
        "x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()['data']['video_url']