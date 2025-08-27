# polls/admin.py

from django.contrib import admin
from .models import Author, Book, Tag

# Tùy chỉnh cách hiển thị cho Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'email', 'birth_date')

# Tùy chỉnh cách hiển thị cho Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'number_of_pages')
    list_filter = ('author', 'tags') # Thêm bộ lọc bên tay phải

# Register your models here, sử dụng các lớp tùy chỉnh ở trên
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Tag)