学习笔记
1.1 urilib也需要添加header才能请求大部分web，不然也会返回418状态码
添加需要同模块包中Request命令，创建一个request对象再做urlopen
import urllib.request
User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
headers = { 'user-agent': User_Agent }

#res_get = request.urlopen('https://movie.douban.com/top250')
res_get = urllib.request.Request(url='https://movie.douban.com/top250',headers=headers)
response = urllib.request.urlopen(res_get)
print(response.read().decode())

1.2 find_all获取所有find的标签/属性，但find只获取第一个。
还可以通过string = re.compile('xxxxx')过滤关键字

1.3 不同电影详情页标签数量不同，要想拉取所有电影上映时间需要做调整

1.7 cookie中含有密码认证信息，实际使用中可以使用通过认证的cookie请求需要账户的页面内容

1.9 allow_domains只包含允许的主域名，有些页面存在跨域跳转，如果要爬取的页面跨域，还需将跨域的域名加入到allow_domains中。
callback回调函数是用parse函数，beautifulsoup解析页面是用html.parser，注意区分.
