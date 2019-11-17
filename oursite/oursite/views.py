# i have created this file- sanyam
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')
def about(request):
    return HttpResponse('this website is created by sanyam and this is his first website in the platform of the django')
def website(request):
    return HttpResponse('''<h1>GO TO WEBSITE</h1<a href ="https://www.youtube.com/results?search_query=call+of+duty+modern+warfare+playlist+"> Django code</a>''')
def removepunc(request):
    # get the text
    djtext = request.GET.get('text','default')
    print(djtext)
    # analyze the text
    return HttpResponse("remove punc")
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove")
# def charcount(request):
#     return HttpResponse("charcount")
def analyze(request):
    return HttpResponse('analyze')