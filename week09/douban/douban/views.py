from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .form import LoginForm
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        #读取表单返回值
        if login_form.is_valid():
            message_dict = login_form.cleaned_data
            user = authenticate(username=message_dict['username'], password=message_dict['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect('/movie/index')
            else:
                return HttpResponse('login failed')

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form.html', {'form': login_form})