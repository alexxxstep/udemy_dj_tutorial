from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book



def first(request):
    books = Book.objects.all()

    return render(request, 'f_temp.html',{'books': books})
