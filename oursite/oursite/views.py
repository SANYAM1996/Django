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
    # check checkbox values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    
    # check which checkbox is on
    if removepunc == 'on':
        Punctuations = '''!()-[]{};:'"\,<>.?@#$%^&*+_~'''
        analyzed = ""
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char
        params = {'purpose':'removed newlines','analyzed_text':analyzed}
        # analyzed the text
        return render('request','analyze.html',params)
    elif(fullcaps == 'on'):
        analyzed = ''
        analyzed = analyzed + char.upper()
    elif(newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char !="\n":



                analyzed = analyzed + char
    elif(extraspaceremover == 'on'):
        analyzed = ''
        for index,char in enumerate (djtext):
            if djtext[index] == ' ' and djtext[index + 1] == " ":
                pass

    else:
        analyzed = analyzed + char
    
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove")
# def charcount(request):
#     return HttpResponse("charcount")
