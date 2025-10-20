import requests
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup
 
#Wow trop cool
#https://www.scraperapi.com/web-scraping/youtube/
 

## Extracting YouTube Comments    
def extract_comments(video_url):
    opts = {"getcomments": True}
    with YoutubeDL(opts) as yt:
        info = yt.extract_info(video_url, download=False)
        comments = info["comments"]
        thread_count = info["comment_count"]
        print("Number of threads: {}".format(thread_count))
        for comment in comments:
            print(comment['text'])
  

def extract_metadata(url):
    with YoutubeDL({}) as yt:
        dico = yt.extract_info(url, download=False)
        keys = ['id', 'title', 'thumbnail', 'description', 'channel', 'channel_id', 'channel_url', 'duration', 'view_count', 'average_rating', 'age_limit', 'webpage_url', 'categories', 'tags', 'subtitles', 'comment_count', 'like_count', 'channel_follower_count', 'timestamp', 'was_live', 'aspect_ratio']
        dico = {key:dico[key] for key in dico if key in keys}
        print("Metadata:", dico)
        return dico
  
## Scraping Channel Information
def scrape_channel_info(channel_url, api_key):
    params = {
        'api_key': api_key,
        'url': channel_url,
        'render': 'true'
    }
    response = requests.get('https://api.scraperapi.com', params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        channel_name = soup.find('yt-formatted-string', {'id': 'text', "class":"style-scope ytd-channel-name"})
        channel_desc = soup.find('div', {'id': 'wrapper', "class":"style-scope ytd-channel-tagline-renderer"})
        if channel_name and channel_desc:
            channel_info = {
                "channel_name": channel_name.text.strip(),
                "channel_desc": channel_desc.text.strip(),
            }
            print("Channel Info:", channel_info)
            return channel_info
        else:
            print("Failed to retrieve channel info")
    else:
        print("Failed to retrieve the page:", response.status_code)

# Extract comments
video_url_for_comments = "https://www.youtube.com/watch?v=Fj1EvQIS1Es"
extract_comments(video_url_for_comments)

print("test")

# Extract metadata
video_url_for_metadata = "https://www.youtube.com/watch?v=Fj1EvQIS1Es"
extract_metadata(video_url_for_metadata)

# Scrape channel information
#api_key = 'YOUR_API_KEY'
#channel_url = 'https://www.youtube.com/@scraperapi/about'
#scrape_channel_info(channel_url, api_key)
