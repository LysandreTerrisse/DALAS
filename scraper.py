import requests
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup

# python -m venv my-venv
# source my-venv/bin/activate
# python -m pip install yt_dlp
# python -m pip install requests
# python -m pip install bs4

# python -m pip install selenium
# python -m pip install webdriver-manager

#Inspired from https://www.scraperapi.com/web-scraping/youtube/
def extract_metadata(url):
    with YoutubeDL({}) as yt:
        dico = yt.extract_info(url, download=False)
        keys = ['id', 'title', 'thumbnail', 'description', 'channel', 'channel_url', 'duration', 'view_count', 'average_rating', 'age_limit', 'webpage_url', 'categories', 'tags', 'comment_count', 'like_count', 'channel_follower_count', 'timestamp', 'aspect_ratio']
        return {key:dico[key] for key in dico if key in keys}



print(extract_metadata("https://www.youtube.com/watch?v=Fj1EvQIS1Es"))

url = 'https://www.youtube.com'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))


#Useful links:
# https://stackoverflow.com/questions/15512239/python-get-all-youtube-video-urls-of-a-channel
# https://stackoverflow.com/questions/54973419/scraping-youtube-links-from-a-webpage
