import imp
from django.shortcuts import render
from the_app.models import Book

# Create your views here.
def test_func(request):
    
    books = Book.objects.all()
    print(books)

    for book in books:
        print(book)
    f_book = Book.objects.filter(page_count__gte(10))
              
    return render(request, 'index.html')