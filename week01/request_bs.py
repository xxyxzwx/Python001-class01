import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
headers = { 'user-agent': User_Agent }
url = 'https://maoyan.com/films?showType=3'
csv_list = []

def get(url):
    response = requests.get(url,headers = headers)
    return response

def bsinfo(url):
    #print(get(url).status_code)
    bs_info = bs(get(url).text,'html.parser')
    #获取前十个电影
    for tags in bs_info.find_all('div', attrs = {'class': 'movie-item film-channel'}, limit = 10):
        for tag_a in tags.find_all('a', limit = 1):
            #获取每个电影的uri组成需要请求的url
            movie_uri = tag_a.get('href')
            movie_url = 'https://maoyan.com'+movie_uri
            #print(movie_url)

            #请求每个电影的详情页url获取信息
            movie_info = bs(get(movie_url).text,'html.parser')
            for tag in movie_info.find_all('div', attrs = {'class': 'movie-brief-container'}):
                movie_name = tag.find('h1').text
                #print(movie_name)

                movie_label = []
                for label in tag.find_all('li', attrs = {'class': 'ellipsis'}):
                    label = label.text.replace(' ','').replace('\n','')
                    movie_label.append(label)
                movie_list = [movie_name, movie_label[0],movie_label[2]]
                csv_list.append(movie_list)
                
                #print(movie_list)

if __name__ == '__main__':
    bsinfo(url)
    movielist_csv = pd.DataFrame(data = csv_list)
    movielist_csv.to_csv('./request_bs.csv', encoding = 'utf8', index = False, header = False)
