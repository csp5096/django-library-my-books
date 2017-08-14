from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from django.views import generic
from .models import Book, Author, BookInstance, Genre
# Import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class BookListView(generic.ListView):
    template_name = "catalog/book.html"
    model = Book
    context_object_name = 'book_list' # your own name for the list as a template variable
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.filter(title__icontains='a')[:5] # get 5 books containing the title 'The'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super ( BookListView, self ).get_context_data ( **kwargs )
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    template_name = "catalog/book_detail.html"
    model = Book

class AuthorListView(generic.ListView):
    template_name = "catalog/author.html"
    model = Author
    context_object_name = 'author_list' # your own name for the list as a template variable
    paginate_by = 2

    def get_queryset(self):
        return Author.objects.filter(first_name__icontains='a')[:5] # get 5 books containing the title 'The'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super ( AuthorListView, self ).get_context_data ( **kwargs )
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class AuthorDetailView(generic.DetailView):
    template_name = "catalog/author_detail.html"
    model = Author