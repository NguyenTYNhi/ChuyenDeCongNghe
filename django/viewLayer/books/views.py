from django.http import HttpResponse
from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"  # tạo template này

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest("publication_date")
        response = HttpResponse(
            headers={
                "Last-Modified": last_book.publication_date.strftime(
                    "%a, %d %b %Y %H:%M:%S GMT"
                )
            }
        )
        return response
    
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"  # để trong template dùng {{ books }}

