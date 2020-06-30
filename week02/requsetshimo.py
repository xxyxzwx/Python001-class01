import requests
from fake_useragent import UserAgent
import json
from selenium import webdriver
import time
ua = UserAgent(verify_ssl=False)
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'User-Agent': ua.random,
    'Referer': 'https://shimo.im/login?from=home',
    'x-requested-with': 'XmlHttpRequest'
}
#个人账号真实登陆，密码从文件中读取
file = open('/Users/xxyxzwx/python/shimo.json')
post_data = json.load(file)
mobile = post_data['mobile']
password = post_data['password']
file.close()
#print(post_data)

def req():
    loginurl = 'https://shimo.im/lizard-api/auth/password/login'

    loginsession = requests.session()
    loginresponse = loginsession.post(loginurl, data = post_data, headers = headers)
    print(loginresponse.status_code)
    url2 = 'https://shimo.im/dashboard/used'
    useresponse = loginsession.get(url2, headers = headers)
    print(useresponse.status_code)
    print(useresponse.text)
    
def webclick(url):
    browser = webdriver.Chrome()
    try:
        browser.get(url)
        #time.sleep(1)
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('18521949342')
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(password)
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
        cookies = browser.get_cookies()
        print(cookies)
    except Exception as e:
        print(e)
    finally:
        browser.close()

if __name__ == '__main__':
    req()
    #webclick(headers['Referer'])