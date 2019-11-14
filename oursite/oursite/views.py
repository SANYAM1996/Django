# i have created this file- sanyam
from django.http import HttpResponse
def index(request):
    return HttpResponse('hello Sanyam how are you?')
def about(request):
    return HttpResponse('this website is created by sanyam and this is his first website in the platform of the django')
def website(request):
    return HttpResponse('''<h1>GO TO WEBSITE</h1<a href ="https://www.youtube.com/results?search_query=call+of+duty+modern+warfare+playlist+"> Django code</a>''')