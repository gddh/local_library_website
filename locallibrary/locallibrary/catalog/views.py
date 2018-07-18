from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    View function for home page of site.
    """
    num_books = Book.objects.all().count()
    num_books_with_word = Book.objects.filter(summary__contains='Harry Potter').count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
            request,
            'index.html',
            context={'num_books':num_books,
                'num_instances':num_instances,
                'num_instances_available': num_instances_available,
                'num_authors':num_authors,
                'num_genres':num_genres,
                'num_books_with_word':num_books_with_word,
                'num_visits':num_visits})

class BookListView(generic.ListView): 
    model = Book
    context_object_name = 'my_book_list'
    paginate_by = 3
    #queryset = Book.objects.filter(title__icontains='war')[:5]

    #def get_queryset(self):
    #    return Book.objects.filter(title__icontains='Harry')[:5]

    def get_content_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'my_author_list'
    pageinate_by = 2

class AuthorDetailView(generic.DetailView):
    model= Author
