from django.shortcuts import render

# Create your views here.

def index(request) :
    # 응답처리
    return render(request, 'articles/index.html')