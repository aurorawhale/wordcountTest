from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.GET['fulltext']  #본문
    count = len(text)   #글자수
    words = text.split()
    wordsDict = {}

    for word in words:
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    return render(request, 'result.html', {'allText' : text, 'counts' : count, 'wordsDiction' : wordsDict.items})
