from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Curriculum #Curriculum이 아닌 models로 하면 models.Curriculum으로 사용해야 한다.
# Create your views here.
def index1(request):
    return HttpResponse('<h1>Hello</h1>')

def index2(request):
    return HttpResponse('<h1>Hi</h1>')

def main(request):
    curriculum = Curriculum.objects.all() #인스턴스로 메소드를 안불러와도 되는 이유,클래스의 전역변수를 사용한 것
    html = ''
    for c in curriculum:
        html += c.name + '<br>'
    return render(request,'firstapp/main.html',{'list':curriculum})  #list라는 이름으로 curriculum 전달
    