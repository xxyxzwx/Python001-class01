from django.shortcuts import render
from .models import QiPaoShui
from django.db.models import Sum, Count

# Create your views here.

def test(request):
    return render(request,'index.html')

def result(request):
    content = QiPaoShui.objects.all()
    count = QiPaoShui.objects.all().count()
    type_comment_count = QiPaoShui.objects.values('productType').annotate(c=Count('*'))
    type_count = QiPaoShui.objects.values('productType').distinct().count()
    user_count = QiPaoShui.objects.values('username').distinct().count()

    queryset = QiPaoShui.objects.values('sentiments')
    good_condtions = {'sentiments__gte': 0.50}
    bad_condtions = {'sentiments__lt': 0.50}
    good_con = QiPaoShui.objects.all().filter(**good_condtions)
    good_con_num = queryset.filter(**good_condtions).count()
    bsd_con = QiPaoShui.objects.all().filter(**bad_condtions)
    bad_con_num = queryset.filter(**bad_condtions).count()
    
    return render(request, 'result.html', locals())

def searchtest(request):
    return render(request, 'searchresult.html')
