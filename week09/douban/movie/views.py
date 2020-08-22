from django.shortcuts import render
from .models import Movie
from django.db.models import Avg
# Create your views here.

def pinglun(request):
    content = Movie.objects.all()
    count = Movie.objects.all().count()
    #提取评分三星以上的作为好评
    condtions = {'star__gte': 4.0}
    plus = Movie.objects.all().filter(**condtions)

    star_avg =f" {Movie.objects.aggregate(Avg('star'))['star__avg']:0.1f} "
    print(star_avg)
    # 情感倾向
    sent_avg =f" {Movie.objects.aggregate(Avg('star'))['star__avg']:0.2f} "

    #好评
    queryset = Movie.objects.values('star')
    condtions = {'star__gte': 4.0}
    plus = Movie.objects.all().filter(**condtions)
    plusnum = queryset.filter(**condtions).count()
    #差评
    queryset = Movie.objects.values('star')
    condtions = {'star__lt': 4.0}
    minus = queryset.filter(**condtions).count()

    return render(request,'result.html',locals())


def search(request):
    message = request.GET.get('message',None)
    #if not message:
    #    error_msg = '请输入关键词'

    infor = Movie.objects.all().filter(content__icontains=message)
    return render(request, 'searchresult.html', {'error_msg': 'error',
                                            'infor': infor})
