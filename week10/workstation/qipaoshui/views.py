from django.shortcuts import render
from .models import QiPaoShui
from django.db.models import Sum, Count, Avg
import json, time

# Create your views here.
def common():
    content = QiPaoShui.objects.all()
    count = QiPaoShui.objects.all().count()
    type_count = QiPaoShui.objects.values('productType').distinct().count()
    user_count = QiPaoShui.objects.values('username').distinct().count()
    queryset = QiPaoShui.objects.values('sentiments')
    good_condtions = {'sentiments__gte': 0.50}
    good_con_num = queryset.filter(**good_condtions).count()
    return {'content': content, 'count': count, 'type_count': type_count, 
           'user_count': user_count, 'good_con_num': good_con_num}

def result(request):
    common_data = common()
    content, count, type_count, user_count, good_con_num = common_data.values()
    type_comment_count = QiPaoShui.objects.values('productType').annotate(a=Avg('sentiments'),c=Count('*'))

    queryset = QiPaoShui.objects.values('sentiments')
    good_condtions = {'sentiments__gte': 0.50}
    bad_condtions = {'sentiments__lt': 0.50}
    good_con = QiPaoShui.objects.all().filter(**good_condtions)
    good_con_num = queryset.filter(**good_condtions).count()
    bsd_con = QiPaoShui.objects.all().filter(**bad_condtions)
    bad_con_num = queryset.filter(**bad_condtions).count()
    if request.method == "GET":
        return render(request, 'result.html', locals())

def searchtest(request):
    common_data = common()
    content, count, type_count, user_count, good_con_num = common_data.values()
    common_data['user_count'], common_data['good_con_num']
    if request.method =="GET":
        query_body = None
        return render(request, 'searchresult.html', locals())
    elif request.method =="POST":
        query_body = request.POST.get('query_body')
        query_condition = request.POST.get('query_condition')
        #处理xxxx.xx.xx,xxxx-x-xx,xxxx年x月x日三种格式日期进行查询
        if query_condition == "comment_time":
            try:
                query_body = time.strftime("%Y-%m-%d",time.strptime(query_body,"%Y-%m-%d"))
            except:
                try:
                    query_body = time.strftime("%Y-%m-%d",time.strptime(query_body,"%Y.%m.%d"))
                except:
                    query_body = time.strftime("%Y-%m-%d",time.strptime(query_body,"%Y年%m月%d"))
        infor = QiPaoShui.objects.all().filter(**{query_condition+"__icontains":query_body})
        return render(request, 'searchresult.html', locals())

def allcomment(request):
    common_data = common()
    content, count, type_count, user_count, good_con_num = common_data.values()
    print(len(content))
    return render(request, 'allcomment.html', locals())
