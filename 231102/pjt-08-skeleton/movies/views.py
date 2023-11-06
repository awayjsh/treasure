from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe
from django.http import JsonResponse
from .models import Movie


# Create your views here.
@require_safe
def index(request):
    pass


@require_safe
def detail(request, movie_pk):
    pass


@require_safe
def recommended(request):
    pass


