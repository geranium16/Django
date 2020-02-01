from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from django.utils import timezone
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #진짜 리스트가 아닌 쿼리셋이라고하는 변형리스트
    # output = ', '.join([q.question_text for q in latest_question_list]) #리스트 컴프리헨션,변형리스트를 리스트로 뽑고 거기서 question_text를 뽑음
    # # return HttpResponse("Hello, world. You're at the polls index.")
    #return HttpResponse(output)
    return render(
        request,
        'polls/index.html',
        {
            'latest_question_list': latest_question_list
        })

def enroll(request):
    question = request.POST.get('question') #딕셔너리형태로 가져옴
    q= Question(question_text=question,pub_date=timezone.now())
    q.save()
    return HttpResponse("%s 추가완료 " %question)
def free(request):
    return render(request,'polls/freelancer.html',{})

def detail(request, question_id): # 질문 상세 페이지 이렇게 변수를 사용하려면 주소창에 이 변수가 쓰여야한다.
    question = Question.objects.get(pk=question_id) #choice자체를 가져오지 않는 이유: choice 자체가 question를 가지고 있어서 
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id): #투표결과페이지
    question = Question.objects.get(pk=question_id)
    #choice = question.choice_set.all()을 써서 choice를 넘겨도된다.
    #이런걸 html로 넘기지말고 shell을 통해 확인가능
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id): # 투표 페이지
    num=request.POST['choice']
    choice = Choice.objects.get(pk=num)
    vote=choice.votes+1 # 투표수 1증가
    choice.votes=vote
    choice.save()
    return HttpResponse("You're voting on question %s." %question_id)