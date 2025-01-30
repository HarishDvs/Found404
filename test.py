import serpapi
from api_key import API_KEY

params = {
    "q": "The Nun",
    "engine": "google",
    "hl": 'en',
    "ijn": "0",
    "api_key": API_KEY
}

search = serpapi.search(params)
links = search['available_on']
links_thumbnails = [(item['link'], item['thumbnail']) for item in links]
print(links_thumbnails)