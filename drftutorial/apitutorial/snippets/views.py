from datetime import datetime
from django.views.decorators.cache import cache_page
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Snippet

from .serializers import SnippetSerializer
from .models import Snippet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'category']
    ordering_fields = ['price', 'name']
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # 🔥 Thêm dòng này
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # 🔥 1. Cho phép filter theo trường cụ thể
    filterset_fields = ['category', 'price', 'in_stock']

    # 🔥 2. Cho phép search theo text (partial match)
    search_fields = ['name', 'description']

    # 🔥 3. Cho phép sắp xếp theo field
    ordering_fields = ['name', 'price']
    ordering = ['name']  # Mặc định sắp xếp theo name
# -----------------------------
# CRUD API cho Snippet
# -----------------------------
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# -----------------------------
# API demo caching
# -----------------------------
@cache_page(60)  # Cache trong 60 giây
@api_view(['GET'])
def cached_hello(request):
    data = {
        "message": "Hello, this response is cached for 60 seconds!",
        "server_time": datetime.now().strftime("%H:%M:%S"),
    }
    return Response(data)
