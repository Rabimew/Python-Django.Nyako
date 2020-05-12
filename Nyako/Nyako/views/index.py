from django.http import  HttpResponse
from django.shortcuts import render ##小猫
def index(request):
    return render(request,'index.html')
def page(request,id):
    return HttpResponse(f"hello Nyako,url参数={id}")
def date(request,year,month,day):
    return HttpResponse(f"hello Nyako,你输入了一个日期：{year}年{month}月{day}日")
def template_exampl(request):
    name='Nyako'
    eatter='电梯'
    data={'脑浆':'好吃'}
    return render(request, "public_exampl.html",locals())