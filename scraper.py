import requests
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# python -m venv my-venv
# source my-venv/bin/activate
# python -m pip install yt_dlp
# python -m pip install requests
# python -m pip install bs4
# python -m pip install playwright
# python -m playwright install


# Inspired from https://www.scraperapi.com/web-scraping/youtube/
def extract_metadata(url):
    with YoutubeDL({}) as yt:
        dico = yt.extract_info(url, download=False)
        keys = ['id', 'title', 'thumbnail', 'description', 'channel', 'channel_url', 'duration', 'view_count', 'average_rating', 'age_limit', 'webpage_url', 'categories', 'tags', 'comment_count', 'like_count', 'channel_follower_count', 'timestamp', 'aspect_ratio']
        return {key:dico[key] for key in dico if key in keys}


# Inspired from https://playwright.dev/python/docs/api/class-browsertype
def scrape_urls():
    with sync_playwright() as p:
        browser = p.firefox.launch_persistent_context("user_data_dir", headless=False)
        page = browser.new_page()
        page.goto("https://www.youtube.com/")
        page.wait_for_selector("a.yt-lockup-metadata-view-model__title", state="attached",  timeout=100000)
        elements = page.query_selector_all("a.yt-lockup-metadata-view-model__title")
        urls = ["https://www.youtube.com" + e.get_attribute("href") for e in elements]
        browser.close()
        return urls


urls = scrape_urls()
print(len(urls))
print(urls)

print(extract_metadata("https://www.youtube.com/watch?v=Fj1EvQIS1Es"))
