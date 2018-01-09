from django.shortcuts import render, HttpResponse

from .models import Question



def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = ({
		'latest_question_list': latest_question_list,
		})
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	return HttpResponse('Вы смотрите на вопрос %s.' % question_id)


def results(request, question_id):
	response = "Вы смотрите на результат опроса %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("Вы голосуете за этот вопрос %s" % question_id)