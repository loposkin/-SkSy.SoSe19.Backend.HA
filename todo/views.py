from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Here must be your index view")


def about(request):
    return HttpResponse("Here must be your impressum view")


def create_todo(request):
    return HttpResponse("Here must be you create-todo view")


def edit_todo(request):
    return HttpResponse("Here must be you edit-todo view")
