from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'homepage.html', {'hithere':'This is me!'})

def about(request):
    return render(request, 'about.html', {'aboutme':'My first django about page!!'})

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext) # prints to terminal

    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increment
            worddictionary[word] += 1
        else:
            # Add
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})



# silly ones
def home_silly(request):
    return render(request, 'home_silly.html', {'hithere':'This is me!'})

def eggs(request):
    return HttpResponse('<h1>Eggs!</h1>')
