学习笔记
1. path和re_path都是_path函数的偏函数partial实现，固定参数Pattern为RoutePattern/RegexPattern
1) partial第一个参数必须是可调用对象
2) 参数的传递顺序是从左到右，但是不能超过源函数参数个数
3) 关键字参数会覆盖partial中定义好的参数
2. 表单CSRF防护(只防护POST请求)
前端中添加了{% csrf_token %}可以起到csrf防护作用（注：前端Ajax提交的信息也需要添加csrf_token否则也会被拒绝）
查看页面源码会发现token被显示出来；
引擎解析不会显示出来，它会把这个隐含值和网站后台保存的值进行匹配，成功才会处理数据；
如果反复的请求或者再次利用这个内容进行请求则会被认为是伪造的POST请求（攻击），返回403 CSRF verification failed
3. 内建信号：
1) 模型类信号Model signals，发送自模型系统(model system)
2) 管理类信号Management signals，发送自django-admin
3) 请求/返回信号(request/response signals)，发送自处理request时的核心框架(the core framework when processing a request.)
4) pre_xxxx执行xxxx前触发, post_xxxx执行xxxx后触发
5) 信号采用注册机制，把函数注册给事件，事件发生时回调函数