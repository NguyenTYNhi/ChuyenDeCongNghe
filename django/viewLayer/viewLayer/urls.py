from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),  # toàn bộ url của app blog sẽ quản lý trong blog/urls.py
    path("news/", include("news.urls")),  # toàn bộ url của app news sẽ quản lý trong news/urls.py
    path('books/', include('books.urls')),
]