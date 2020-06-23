import requests
from bs4 import BeautifulSoup as bs

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
headers = { 'user-agent': User_Agent }
url = 'https://maoyan.com/films?showType=3'

def get(url):
    response = requests.get(url,headers = headers)
    return response

def bsinfo(url):
    print(get(url).status_code)
    bs_info = bs(get(url).text,'html.parser')
    for tags in bs_info.find_all('div', attrs = {'class': 'movie-item film-channel'}, limit = 10):
        for tag_a in tags.find_all('a', limit = 1):
            movie_uri = tag_a.get('href')
            movie_url = 'https://maoyan.com'+movie_uri
            print(movie_url)
            #movie_info = bs(get(movie_uri).text,'html.parser')
            #for tag in movie_info.find_all('div', attrs = {'class': 'movie-brief-container'})

bsinfo(url)
