# Manual Created File...

from django.http import HttpResponse
from django.shortcuts import render
import string

# def index(request):
#     with open('mysite/1.txt', mode='r') as one:
#         texts = one.readlines()
#         return HttpResponse(texts)


def index(request):
    dict = {'name': 'Rafsan', 'class': 'XI'}
    return render(request, 'index.html', dict)


def about(request):
    return HttpResponse("<h1>This is about us page.</h1>")


def form(request):
    text = request.POST.get('text', 'Nothig you write.')
    check = request.POST.get('check', 'off')
    counter = request.POST.get('counter', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    punctuations = string.punctuation
    analyzed_text = ""
    count = 0

    # Remove punction function.

    def remove_punc(str):
        analyzed_str = ''
        for char in str:
            if char not in punctuations:
                analyzed_str += char
        return analyzed_str

    # Character Counter function.
    def counterFun(str):
        str_list = list(str)
        total_char = len(str_list)
        return total_char

    # Uppercase function.
    def toUpperCase(str):
        analyzed_str = str.upper()
        return analyzed_str

    if check == 'on' and uppercase == 'on' and counter == 'on':
        remove_punc = remove_punc(text)
        uppercase = toUpperCase(remove_punc)
        analyzed_text = uppercase
        count = counterFun(analyzed_text)
        params = {'text': analyzed_text, 'total': count}
    elif check == 'on' and uppercase == 'on':
        remove_punc = remove_punc(text)
        uppercase = toUpperCase(remove_punc)
        analyzed_text = uppercase
        params = {'text': analyzed_text}
    elif check == 'on' and counter == 'on':
        analyzed_text = remove_punc(text)
        count = counterFun(analyzed_text)
        params = {'text': analyzed_text, 'total': count}
    elif uppercase == 'on' and counter == 'on':
        analyzed_text = toUpperCase(text)
        count = counterFun(analyzed_text)
        params = {'text': analyzed_text, 'total': count}
    elif check == 'on':
        analyzed_text = remove_punc(text)
        params = {'text': analyzed_text}
    elif uppercase == 'on':
        analyzed_text = toUpperCase(text)
        params = {'text': analyzed_text}
    elif counter == 'on':
        count = counterFun(text)
        print(count)
        params = {'text': analyzed_text, 'total': count}
    else:
        return HttpResponse(text + "<p style='color: red;'>Error!</p>")

    return render(request, 'form.html', params)