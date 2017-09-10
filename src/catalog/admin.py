from django.contrib import admin

from .models import Author, Genre, Book, BookInstance

# Use an inline to associate records with the BookInstance
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Use an inline to associate records with the Book
class BookInline(admin.TabularInline):
    model = Book

# admin.site.register(Book)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

# admin.site.register(Author)
# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# admin.site.register(Genre)
# Define the genre class
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

# admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id')

# admin.site.register(Entry_Views)
# Register the Admin classes for Entry_Views using the decorator
#@admin.register(Entry_Views)
#class Entry_Views_Admin(admin.ModelAdmin):
#   list_display = ("entry", "ip", "session", "created")
#   list_per_page = 20

