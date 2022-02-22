""""Views to render blogs"""
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """A view to return the blog home page"""
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    """A view to return the About blog page"""
    return HttpResponse('<h1>Blog About</h1>')
