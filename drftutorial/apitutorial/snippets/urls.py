from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetail, cached_hello
from .views import ProductListView
urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('cached/', cached_hello, name='cached_hello'),
    path('products/', ProductListView.as_view(), name='product-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
