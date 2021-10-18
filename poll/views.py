from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from poll.models import Question
from django.urls import reverse


# 127.0.0.1:8000/poll
def poll_list(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'poll/poll_list.html', context)

def poll_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'poll/poll_detail.html', context)

def poll_vote(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
        choice = request.POST['choice']     # name에서 가져오기
        sel_choice = question.choice_set.get(id = choice)
    except KeyError:
        return render(request, 'poll/poll_detail.html', {
            'question':question,
            'error_message':'항목을 선택을 해주세요'
        })
    else:
        sel_choice.votes += 1
        sel_choice.save()
        return HttpResponseRedirect(reverse('poll:poll_result', args=(question.id,)))
        # poll/results/2

def poll_result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'poll/poll_result.html', context)


