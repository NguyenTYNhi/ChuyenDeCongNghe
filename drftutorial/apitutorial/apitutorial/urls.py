from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/snippets/', permanent=False)),
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),  # bỏ 'snippets/'
]
