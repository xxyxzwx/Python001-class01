from time import sleep
import requests,random,json
from lxml import etree
from queue import Queue
import threading

cookie={
    'JSESSIONID': 'ABAAAECABFAACEA6B4D85165D39E4D662B4FB74382167ED',
    'user_trace_token': '20200712112451-c736f54d-da2b-43e9-9570-fcd9a3fdcb7e',
    'WEBTJ-ID': '20200712112451-173410dd359af-0363aeb097b96f-31627403-1296000-173410dd35a1c',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22173410dd42d37c-0aa93a42109398-31627403-1296000-173410dd42ed46%22%2C%22%24device_id%22%3A%22173410dd42d37c-0aa93a42109398-31627403-1296000-173410dd42ed46%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    'PRE_UTM': '',
    'PRE_HOST': '',
    'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5Fpython%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%2Fp-city%5F3%3Fpx%3Ddefault%23filterBox',
    'LGSID': '20200712112452-335714ae-90f7-4266-91b9-ddfb29bf2f6f',
    'PRE_SITE': 'https%3A%2F%2Fwww.lagou.com',
    'LGUID': '20200712112452-e5f89e12-e340-443d-bddd-505192b8d9b6',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1594524292',
    '_ga': 'GA1.2.641918062.1594524292',
    '_gat': '1',
    '_gid': 'GA1.2.944901011.1594524292',
    'SEARCH_ID': '04dd1ed51c1b45afa77fae2277b8d073',
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1594524301',
    'X_HTTP_TOKEN': '4d54ac52225896565134254951a1a949a7fb33c28e',
    'LGRID': '20200712112516-e5fa38d2-e5dd-4e2e-b3bb-f3597b46804d'
}

class getRequest(threading.Thread):
    def __init__(self,queue,cookie):
        threading.Thread.__init__(self)
        self.cookie = cookie
        self.queue = queue
    def run(self):
        self.getcookie()
        sleep(random.choice([3,4,5]))
        self.schedule()
    def getcookie(self):
        geturl = 'https://www.lagou.com/jobs/list_python%E5%B7%A5%E7%A8%8B%E5%B8%88/p-city_213?px=default'
        header1 = {
            'Origin': 'https://www.lagou.com',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*',
            'Accept-Encoding': 'br, gzip, deflate',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
        }
        response = requests.get(geturl,headers=header1)
        result = requests.utils.dict_from_cookiejar(response.cookies)
        #result["user_trace_token"] = result["LGRID"]
        #result["LGSID"] = result["LGRID"]
        #result["LGUID"] = result["LGRID"]
        self.cookie.update(result)


    def schedule(self):
        while True:
            if self.queue.empty():
                break
            else:
                page = self.queue.get()
                data = {
                    'first': 'false',
                    'pn': page,
                    'kd': 'python工程师'
                    #'sid': 'd73dfe60a72b44689fcc6b730ed91a55',
                }
                posturl = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
                header2 = {
                    'Origin': 'https://www.lagou.com',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept': '*/*',
                    'Accept-Encoding': 'br, gzip, deflate',
                    'Connection': 'keep-alive',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
                    'Referer': 'https://www.lagou.com/jobs/list_python%E5%B7%A5%E7%A8%8B%E5%B8%88/p-city_213?px=default',
                    'X-Anit-Forge-Token': 'None',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-Anit-Forge-Code': '0'
                }
                try:
                    sleep(random.choice([3,4,5]))
                    response = requests.post(posturl, headers= header2, cookies=self.cookie, data=data)
                    response.raise_for_status()
                    response.encoding = response.apparent_encoding
                    result = response.text
                    print(type(json.loads(result)))
                except Exception as e:
                    print('下载出现异常',e)


if __name__ == "__main__":
    queue = Queue()
    
    for page in range(1,2):
        queue.put(page)

    getthread_list=[]
    for _ in range(3):
        thread = getRequest(queue,cookie)
        thread.start()
        getthread_list.append(thread)

    for t in getthread_list:
        t.join()