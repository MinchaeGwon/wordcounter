from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for w in words:
        if w in word_dictionary:
            word_dictionary[w] += 1
        else:
            word_dictionary[w] = 1

    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})    