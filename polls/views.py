#oding:utf-8
from socket import socket, AF_INET, SOCK_STREAM
import logging
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .en_xml import makeup_xml
from django.views.decorators.csrf import csrf_exempt 
def index(request):
	return render(request, 'polls/index.html')
	
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	question.choice_set.create(choice_text="jack", votes=0)
	question.choice_set.create(choice_text="rose", votes=0)
	return render(request, 'polls/detail.html')

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question': p, 'error_message': "You didn't select a choice",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
@csrf_exempt 
def en_xml(request):
    message = makeup_xml(request)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("127.0.0.1", 20980))
    s.send(message)
    
    head = s.recv(41).decode('gbk')
    len = head[4:9]
    print(type(len),len, int(len))
    data = s.recv(int(len))
    print(data)
    return render(request, 'polls/en_xml.html', {'message':head+data.decode('gbk')})
'''
	if request.GET.get('TradeCode','' ) == '11005':
		message = 'root'
	    return render(request, 'polls/en_xml.html', {'message': message})
	else:
		pass
'''
def jd(request):
	return render(request, 'polls/jd.mhtml')

logger = logging.getLogger('en_xml')
logger.info('aaa')
logger.error('error')
