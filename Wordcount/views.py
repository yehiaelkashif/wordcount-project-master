from django.http import HttpResponse
from  django.shortcuts import render
def home(request):
    return  render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordList=fulltext.split()
    wordCountDictionary={}
    for word in wordList:
        if word in wordCountDictionary:
            wordCountDictionary+=1
        else:
            wordCountDictionary[word]=1

    return  render(request,'count.html',{"fulltext":fulltext,"count":len(wordList),"wordCountDictionary":wordCountDictionary.items()})
