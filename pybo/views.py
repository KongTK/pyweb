from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from pybo.form import QuestionForm
from pybo.models import Question



def index(request):
    # return HttpResponse("Welcome~ mySite!!")
    question_list = Question.objects.all()
    context = {'question_list':question_list}
    return render(request, 'pybo/question_list.html', context)

# 상세 페이지 조회
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request, 'pybo/detail.html', context)

# 질문 등록
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # 임시 저장(등록일이 없으니)
            question.create_date = timezone.now() # 등록일 입력
            question.save() # 실제 저장
            return redirect('pybo:index')
    else: # request.method == 'GET':
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)