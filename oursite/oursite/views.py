# i have created this file- sanyam
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')
# def about(request):
#     return HttpResponse('this website is created by sanyam and this is his first website in the platform of the django')
# def website(request):
#     return HttpResponse('''<h1>GO TO WEBSITE</h1<a href ="https://www.youtube.com/results?search_query=call+of+duty+modern+warfare+playlist+"> Django code</a>''')
def analyze(request):
    # get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    # analyzed = djtext
    # analyze the text
    if removepunc == 'on':
        Punctuations = '''!()-[]{};:'"\,<>.?@#$%^&*+_~'''
        analyzed = ""
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render('request','analyze.html',params)
    else:
        return HttpResponse('Error')
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove")
# def charcount(request):
#     return HttpResponse("charcount")
