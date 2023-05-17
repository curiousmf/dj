import imp
from django.shortcuts import render
from the_app.models import Book

# Create your views here.
def test_func(request):

    books = Book.objects.all()
    print(books)

    for book in books:
        print(book)
              
    return render(request, 'index.html')