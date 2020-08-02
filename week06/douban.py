import requests,json,pymysql,time,random
import lxml.etree
import pandas as pd
from sqlalchemy import create_engine

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
headers = { 'user-agent': User_Agent }
urls = list(f'https://movie.douban.com/subject/1851857/comments?start={ page * 20 }&limit=20&sort=new_score&status=P' for page in range(5))
url = 'http://movie.douban.com/subject/1851857/comments?start=0&limit=20&sort=new_score&status=P'
n_star={'推荐': 4, '力荐': 5, '还行': 3, '较差': 2, '很差': 1}

def get(url):
    response = requests.get(url,headers=headers)
    return response.text

def select(text):
    selector = lxml.etree.HTML(text)
    user = selector.xpath('//*[@id="comments"]//span[@class="comment-info"]/a/text()')
    star = selector.xpath('//*[@id="comments"]//span[@class="comment-info"]/span[2]/@title')
    content = selector.xpath('//*[@id="comments"]//div[@class="comment"]/p/span/text()')
    return datachange(user,star,content)

def datachange(user,star,content):
    df = pd.DataFrame({
        'user': user,
        'oldstar': star,
        'content': content
    })
    df['star'] = df['oldstar'].map(n_star)
    df = df.fillna('0.0')
    df = df.drop('oldstar', axis=1)
    return df

def insertsql(dataframe):
    with open('/Users/xxyxzwx/python/mysqlconf.json') as f:
        mysqlconf = json.load(f)
    engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % mysqlconf, encoding='utf-8')
    pd.io.sql.to_sql(dataframe, 'movie', con=engine, index=False, if_exists='append')
    print("Write to MySQL successfully!")

if __name__=='__main__':
    for url in urls:
        df = select(get(url))
        insertsql(df)
        time.sleep(random.choice([3,4,5]))
    
    
    