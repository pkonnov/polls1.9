from django.shortcuts import render, HttpResponse



def index(request):
	return HttpResponse("Hello pshtet")


def detail(request, question_id):
	return HttpResponse('Вы смотрите на вопрос %s.' % question_id)


def results(request, question_id):
	response = "Вы смотрите на результат опроса %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("Вы голосуете за жтот вопрос %s" % question_id)