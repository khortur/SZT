from django.shortcuts import render
from django.http import HttpResponse
from store.models import Book
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.

def home(request):
    # return HttpResponse("Hello World");
    user = request.user
    return render(request, 'home.html', {"user":user})

def sklep(request):
    return render(request, 'store.html')

def store(request):
    return render(request, 'index.html')

def books(request):
    books_count = Book.objects.count();
    plural = "książkę"
    if (books_count > 1):
        plural = "książki"

    query_results = Book.objects.all();

    return render(request, 'books.html', {"books_count":books_count, "plural":plural, "query_results":query_results})