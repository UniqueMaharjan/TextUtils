# I created this file - Unique
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')
def analyze(request):
    #get the text
    djtext = (request.POST.get('text','default'))
    #check checkbox value
    removepunc = (request.POST.get('removepunc','off'))
    fullcaps = (request.POST.get('fullcaps','off'))
    newlineremover = (request.POST.get('newlineremover','off'))
    extraspaceremover = (request.POST.get('extraspaceremover','off'))
    charcount = (request.POST.get('charcount','off'))
    #check with checkbox is on
    if removepunc == "on":
        puncuations = '''!()-{}[];:'"/\,<>.?@#^&*$~_'''
        analyzed = ""
        for char in djtext:
            if char not in puncuations:
                analyzed += char
        params = {'purpose':'Removed Punctuation',
              'analyzed_text': analyzed}
        djtext = analyzed


    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose':'Changed to upper case',
                  'analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed += char
        params = {'purpose': 'Remove new line',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Extra Space remover',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = 0
        for char in djtext:
            if not char ==' ':
                analyzed += 1
        params = {'purpose': 'Character count',
                  'analyzed_text': analyzed}

        # return render(request, 'analyze.html', params)
    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return HttpResponse('Error')
    return render(request, 'analyze.html', params)
def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contactus.html')


