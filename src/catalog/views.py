from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.conf import settings
from django.views.generic import ListView
from django.views.generic import DetailView
from django.http import request
from django.views import generic
from django.db.models import Q, Count, Aggregate
from .models import Book, Author, BookInstance, Genre, PageView


import datetime

class BaseFields(object):

    base_query = Book.objects.all()

    def counter(base_query, field_name):

        return base_query.values(field_name).annotate(Count(field_name))

    extra_context_dict = {}

    extra_context_dict['num_books'] = base_query.count()
    extra_context_dict['num_instances'] = BookInstance.objects.all().count()
    extra_context_dict['num_instances_available'] = BookInstance.objects.filter(status__exact='a').count()
    extra_context_dict['num_authors'] = Author.objects.count()


class BaseListFields(BaseFields):
    template_name = "index.html"
    model = Book
    context_object_name = "books"

class HomePageView(BaseListFields, ListView):

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super (HomePageView, self ).get_context_data (*args, **kwargs )

        # Here's what it looks like to add that extra context, via the dict .update() method.
        # This is grabbing that dict from the BaseListFields class and merging it into context.
        context.update ( self.extra_context_dict )

        # Here's what it looks like to add some extra arbitrary content to context.
        context['page_class'] = '_home_page_view'

        # Return it
        return context

class AboutFields(object):

    base_query = PageView.objects.all()

    def counter(base_query, field_name):

        return base_query.values(field_name).annotate(Count(field_name))

    def Home(request):

        if (PageView.objects.count () <= 0):
            x = PageView.objects.create ()
            x.save ()
        else:
            x = PageView.objects.all ()[0]
            x.hits = x.hits + 1
            x.save ()
        context = {'num_visits': x.hits}
        return render ( request, context=context )

    extra_context_dict = {}

    extra_context_dict['num_visits'] = base_query.count()

class AboutListFields ( AboutFields ):
        template_name = "about.html"
        model = Book
        context_object_name = "books"

class AboutPageView(AboutListFields, ListView):

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super (AboutPageView, self ).get_context_data (*args, **kwargs )

        # Here's what it looks like to add that extra context, via the dict .update() method.
        # This is grabbing that dict from the BaseListFields class and merging it into context.
        context.update ( self.extra_context_dict )

        # Here's what it looks like to add some extra arbitrary content to context.
        context['page_class'] = '_about_page_view'

        # Return it
        return context

class BookListView(generic.ListView):
    template_name = "catalog/book.html"
    model = Book
    context_object_name = 'book_list' # your own name for the list as a template variable
    paginate_by = 10

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
    paginate_by = 10

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