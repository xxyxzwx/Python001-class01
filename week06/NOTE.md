学习笔记
1. django连接docker中的mysql会报如下错，确认pymysql已安装过
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?
查询文档得知需要其他引擎支持，pip安装mysql-connector-python，引擎修改为mysql.connector.django
2. 语言时区问题：
django默认的时区是UTC，使用中国时间要将TIME_ZONE改为Asia/Shanghai，CST无法识别
修改中文语言要将LANGUAGE_CODE改为'zh-hans'，zh_CN无法识别
3. get和filter的区别
get只支持精确匹配，filter可以像sql一样匹配大于小于是否存在等
get返回的是一个model对象；filter返回的是一个QuerySet集合，可以进行遍历操作，获取QuerySet的值需要使用values()函数
get方法是从数据库的取得一个匹配的结果，返回一个对象，如果记录不存在的话，它会报错，有多条记录也会报错。
filter有没有匹配的记录都可以，从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]。
4. 模板跳转到静态资源时，需要在当前页面的head标签中添加{% load staticfiles %}，否则会产生报错Invalid block tag on line 9: 'static'. Did you forget to register or load this tag?
默认静态文件的目录在settings.py中定义STATICFILES_DIRS对象
5. urlconf类似nginx的location和upstream，针对不同的location指定到不同的upstream(app.urls)
6. 前端语言中href标签进行的跳转并不是直接跳转到指定的连接，而是返回到原域名/href标签值的位置，再由urls（location）进行判断跳转到什么位置
7. 搜索功能考虑跨域问题要在<form>标签下添加{% csrf_token %}
